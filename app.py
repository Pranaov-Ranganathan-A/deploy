import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("C://Users//apran//Desktop//Python_Diwali_Sales_Analysis//Diwali Sales Data.csv",encoding="ISO-8859-1")

# Data cleaning
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype(int)

# Set Streamlit page config
st.set_page_config(page_title="Diwali Sales Analysis", layout="wide")

# Title
st.title("Diwali Sales Data Analysis")

# Gender Distribution
st.subheader("Gender Distribution")
fig, ax = plt.subplots()
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(fig)

# Sales by Gender
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.subheader("Total Sales by Gender")
fig, ax = plt.subplots()
sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=ax)
st.pyplot(fig)

# Sales by Age Group and Gender
st.subheader("Sales by Age Group and Gender")
fig, ax = plt.subplots()
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(fig)

# Total Sales by Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.subheader("Total Amount vs Age Group")
fig, ax = plt.subplots()
sns.barplot(x='Age Group', y='Amount', data=sales_age, ax=ax)
st.pyplot(fig)

# Orders by Top 10 States
sales_state_orders = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
st.subheader("Total Orders by Top 10 States")
fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_orders, x='State', y='Orders', ax=ax)
st.pyplot(fig)

# Sales by Top 10 States
sales_state_amount = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
st.subheader("Total Sales by Top 10 States")
fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_amount, x='State', y='Amount', ax=ax)
st.pyplot(fig)

# Marital Status Distribution
st.subheader("Marital Status Distribution")
fig, ax = plt.subplots()
ax = sns.countplot(data=df, x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(fig)

# Sales by Marital Status and Gender
sales_marital_gender = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.subheader("Sales by Marital Status and Gender")
fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(data=sales_marital_gender, x='Marital_Status', y='Amount', hue='Gender', ax=ax)
st.pyplot(fig)

# Sales by Occupation
sales_occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.subheader("Sales by Occupation")
fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_occupation, x='Occupation', y='Amount', ax=ax)
st.pyplot(fig)

# Product Category Distribution
st.subheader("Product Category Distribution")
fig, ax = plt.subplots(figsize=(15, 5))
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(fig)

# Sales by Top 10 Product Categories
sales_product_category = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
st.subheader("Sales by Top 10 Product Categories")
fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_product_category, x='Product_Category', y='Amount', ax=ax)
st.pyplot(fig)

# Top 10 Most Sold Products by Orders
sales_top_products = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
st.subheader("Top 10 Most Sold Products by Orders")
fig, ax = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_top_products, x='Product_ID', y='Orders', ax=ax)
st.pyplot(fig)
