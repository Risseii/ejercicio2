import streamlit as st 
import pandas as pd 

st.title('Inventory discrepancy')

df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)

df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)

#df_expected.sample(2).T
df_expected.sample(2).T

#removing duplicates Reatil product SKU
df_expected.drop_duplicates(subset='Retail_Product_SKU',keep='first')

#removing duplicates RFID
df_counted.drop_duplicates(subset='RFID',keep='first')

#shape
df_expected.shape

#group by
df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
