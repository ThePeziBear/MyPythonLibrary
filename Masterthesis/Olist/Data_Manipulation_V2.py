# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Import all datasets
df_customers=pd.read_csv('olist_customers_dataset.csv')
df_geolocation=pd.read_csv('olist_geolocation_dataset.csv')
df_order_items=pd.read_csv('olist_order_items_dataset.csv')
df_order_pay=pd.read_csv('olist_order_payments_dataset.csv')
df_order_reviews=pd.read_csv('olist_order_reviews_dataset.csv')
df_orders=pd.read_csv('olist_orders_dataset.csv')
df_products=pd.read_csv('olist_products_dataset.csv')
df_sellers=pd.read_csv('olist_sellers_dataset.csv')
df_product_cat=pd.read_csv('product_category_name_translation.csv')


#Merge datasets for one big with all informations
df=pd.merge(df_orders,df_order_items,on='order_id', how='right')
df=df.merge(df_products, on='product_id')
df=df.merge(df_order_reviews,on='order_id')
df=df.merge(df_sellers,on='seller_id')
df=df.merge(df_customers,on='customer_id')
df = df.rename(columns={'price':'product_price','order_item_id':'quantity'})
df = df.drop(['review_id', 'review_creation_date','review_answer_timestamp','review_comment_title','review_comment_message','customer_id'], axis=1)

print(df.groupby(by='order_status').count()) #Take look at the distribution of order status

df = df[df['order_status'] == 'delivered'] # just delivered products are relevant for rating_review

# Creating Features for Dataset: Product avg Score, Product Price avg, Seller Score avg
product_scored=df.groupby(by='product_id')['review_score'].mean()
product_avg_price=df.groupby(by='product_id')['product_price'].mean()

df_product_calc=pd.concat([product_scored,product_avg_price],axis=1)
df_product_calc=df_product_calc.reset_index()
df_product_calc=df_product_calc.rename(columns={'review_score':'score_product_avg','product_price':'product_price_avg'})

seller_scored=df.groupby(by='seller_id')['review_score'].mean()
df_seller_scored=pd.DataFrame(data=seller_scored)
df_seller_scored=df_seller_scored.reset_index()
df_seller_scored=df_seller_scored.rename(columns={'review_score':'seller_score_avg'})



df=df.merge(df_product_calc, on='product_id')
df=df.merge(df_seller_scored, on='seller_id')







#dfnull=df[df['order_status']=='nan']

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='RdBu')
