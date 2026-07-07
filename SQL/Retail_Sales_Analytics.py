import numpy as pd
import pandas as pd

file="Retail_Sales_Analytics_Enterprise_Dataset.xlsx"

customers=pd.read_excel(file, sheet_name="Customers")
products=pd.read_excel(file, sheet_name="Products") 
orders=pd.read_excel(file, sheet_name="Orders") 

print(customers.head()) 

print(customers.shape)
print(customers.columns)
print(customers.info())
print(customers.describe())
print(customers.head())
print(customers.tail())


print(products.head()) 

print(products.shape)
print(products.columns)
print(products.info())
print(products.describe())
print(products.head())
print(products.tail())

print(orders.head())

print(orders.shape)
print(orders.columns)    
print(orders.info())
print(orders.describe()  ) 
print(orders.head())
print(orders.tail())


# Data Cleaning

#Missing Values

print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())


#duplicate rows

print(customers.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())

#convert dates
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
print(orders.dtypes)

#Create new column

#Month
orders["Month"]=orders["OrderDate"].dt.month_name()
#Year
orders["Year"]=orders["OrderDate"].dt.year
#Quarter
orders["Quarter"]=orders["OrderDate"].dt.quarter    


#Merge Data
#Join Orders to Products

sales=pd.merge(orders, products, how="left", on="ProductID")
print(sales)

#Join customers

sales=pd.merge(sales, customers, how="left", on="CustomerID")
print(sales)

#Creating Bussiness Metrics
#Revenue
sales["Revenue"]=sales["Quantity"]*sales["SellingPrice"]
print(sales)

#Discount Amount
sales["DiscountAmount"]=sales["Revenue"]*sales["DiscountPct"]/100
print(sales)

#Final Sales
sales["FinalSales"]=sales["Revenue"]-sales["DiscountAmount"]
print(sales)

#Cost
sales["Cost"]=sales["Quantity"]*sales["CostPrice"]
print(sales)

#Profit
sales["Profit"]=sales["FinalSales"]-sales["Cost"]   
print(sales)




df = pd.read_csv("Retail_Sales_Analytics_Enterprise_Dataset.csv")

print(df.columns.tolist())
print(df.head())