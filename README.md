# E-commerce_Product_Recommendation_System

# 🛒 E-Commerce Product Recommender

An interactive Web App built with **Streamlit** that delivers personalized product suggestions using collaborative filtering. By analyzing historical purchase data and predicted match scores, the app filters out items users have already bought and surfaces their next favorite products.

---

## 🚀 Features

* **Smart Filtering:** Recommends new products by automatically excluding items the user has already purchased.
* **Flexible Inputs:** Select from a quick dropdown of sample users or look up a specific `User ID`.
* **Customizable Results:** Dynamic slider to adjust the number of recommendations ($1$ to $10$) on the fly.
* **Polished UI:** Displays results in a clean, interactive data table with formatted match scores.
* **Performance Optimized:** Utilizes Streamlit's `@st.cache_data` to ensure data models load instantly after the first initialization.

---

## 🛠️ Tech Stack

* **Frontend/App Framework:** [Streamlit](https://streamlit.io/)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
* **Serialization:** Pickle (`.pkl`)

---

## 📁 Dataset link: 

https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews
