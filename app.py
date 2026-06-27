import streamlit as st
import pandas as pd

# 1. Set up the page
st.set_page_config(page_title="Product Recommender", page_icon="🛒")
st.title("🛒 E-Commerce Product Recommender")
st.markdown("Discover new products tailored to individual user preferences based on collaborative filtering.")

# 2. Load the data (Cache it so it only loads once)
@st.cache_data
def load_data():
    preds = pd.read_pickle('predictions.pkl')
    history = pd.read_pickle('user_history.pkl')
    return preds, history

try:
    preds_df, user_history_df = load_data()
except FileNotFoundError:
    st.error("Could not find the data files. Make sure predictions.pkl and user_history.pkl are in the same folder.")
    st.stop()

# 3. Create the Recommendation Function
def get_recommendations(user_id, num_recs):
    if user_id not in preds_df.index:
        return None
        
    # Get user's predicted scores
    user_preds = preds_df.loc[user_id].sort_values(ascending=False)
    
    # Get items the user has already bought
    user_past_items = user_history_df[user_history_df['UserId'] == user_id]['ProductId'].tolist()
    
    # Filter out past items
    recommendations = user_preds[~user_preds.index.isin(user_past_items)].head(num_recs)
    
    # Format as a dataframe for Streamlit
    rec_df = pd.DataFrame({
        'Product ID': recommendations.index,
        'Predicted Match Score': recommendations.values
    })
    return rec_df

# 4. Build the Sidebar / UI Inputs
st.sidebar.header("User Settings")

# Let's provide a list of sample users so you don't have to guess IDs
sample_users = preds_df.index[:100].tolist()
selected_user = st.sidebar.selectbox("Select a User ID to preview:", ["-- Select User --"] + sample_users)

# Allow custom input in case they want to paste a specific ID
custom_user = st.sidebar.text_input("Or type a specific User ID:", value="")

num_recommendations = st.sidebar.slider("Number of Recommendations", min_value=1, max_value=10, value=5)

# 5. Display Recommendations
user_to_predict = custom_user if custom_user != "" else selected_user

if st.button("Generate Recommendations"):
    if user_to_predict == "-- Select User --" or user_to_predict == "":
        st.warning("Please select or enter a valid User ID.")
    else:
        with st.spinner(f"Analyzing preferences for {user_to_predict}..."):
            results = get_recommendations(user_to_predict, num_recommendations)
            
            if results is None:
                st.error(f"User ID '{user_to_predict}' not found in the database.")
            else:
                st.success("Recommendations Generated!")
                st.write(f"### Top {num_recommendations} Picks for User: `{user_to_predict}`")
                
                # Display as a styled table
                st.dataframe(
                    results.style.format({'Predicted Match Score': '{:.4f}'}), 
                    use_container_width=True,
                    hide_index=True
                )