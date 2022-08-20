import streamlit as st 
import pandas as pd 

st.title('Inventory discrepancy')

df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)

df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)

st.write('Sample df_expected')
df_expected.sample(2).T

st.write('Shape df_expected')
df_expected.shape

st.write('Number of unique values : Retail pdt sku')
df_expected["Retail_Product_SKU"].nunique()

st.write('Sample df_counted')
df_counted.sample(2).T

st.write('Shape df_counted')
df_counted.shape

#removing duplicates RFID
st.write('Removing RFID duplicates')
df_counted = df_counted.drop_duplicates("RFID")

st.write('Group by')
df_B = df_counted.groupby("Retail_Product_SKU").count()[["RFID"]].reset_index().rename(columns={"RFID":"Retail_CCQTY"})
df_B.sample(10)

my_cols_selected = ["Retail_Product_Color",
"Retail_Product_Level1",
"Retail_Product_Level1Name",
"Retail_Product_Level2Name",
"Retail_Product_Level3Name",
"Retail_Product_Level4Name",
"Retail_Product_Name",
"Retail_Product_SKU",
"Retail_Product_Size",
"Retail_Product_Style",
"Retail_SOHQTY"]

st.write('Head')
df_A = df_expected[my_cols_selected]
df_A.head().T

st.write('Discrepancy head')
df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU")
df_discrepancy.head()



