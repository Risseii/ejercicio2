import streamlit as st 
import pandas as pd 

st.title('Inventory discrepancy')

df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)

df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)


df_expected.sample(2).T

#shape - df_expected
df_expected.shape

#number of unique values : Retail pdt sku
df_expected["Retail_Product_SKU"].nunique()


df_counted.sample(2).T

#shape - df_counted
df_counted.shape

#removing duplicates RFID
df_counted = df_counted.drop_duplicates("RFID")

#group by
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

df_A = df_expected[my_cols_selected]

df_A.head().T

df_discrepancy = pd.merge(df_A, df_B, how="outer", left_on="Retail_Product_SKU", right_on="Retail_Product_SKU", indicator=True)

df_discrepancy.head()

