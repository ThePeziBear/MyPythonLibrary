# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df_customers=pd.read_csv('olist_customers_dataset.csv')
df_geolocation=pd.read_csv('olist_geolocation_dataset.csv')
df_order_items=pd.read_csv('olist_order_items_dataset.csv')
df_order_pay=pd.read_csv('olist_order_payments_dataset.csv')
df_order_reviews=pd.read_csv('olist_order_reviews_dataset.csv')
df_orders=pd.read_csv('olist_orders_dataset.csv')
df_products=pd.read_csv('olist_products_dataset.csv')
df_sellers=pd.read_csv('olist_sellers_dataset.csv')
df_product_cat=pd.read_csv('product_category_name_translation.csv')

df_products
df_order_items

df_count_items=df_order_items.groupby('product_id').count()
df_count_items=df_count_items.sort_values(by='order_id', ascending=False)
df_count_items=(df_count_items.iloc[:50]).sort_values(by='order_id', ascending=False)
df_count_items

barblot_product1 = df_count_items['order_id'].plot.bar(stacked=True)


dfmerge = pd.merge(df_order_items,df_products, how='inner', left_on='product_id', right_on='product_id')#.set_index('Auswahl Spalte als Index')
df_merge2=dfmerge[['product_id','product_category_name','order_item_id','price','seller_id']]
barblot_product2 = df_count_items['order_id'].plot.bar(stacked=True)

df_cool_stuff=df_merge2[df_merge2['product_category_name']=='cool_stuff']

# Predictive Opportunities

#1 Predict score_reviews
df_count_reviews=df_order_reviews.groupby('review_score').count()
barplot_review1 = df_count_reviews['review_id'].plot.bar(stacked=True)
#Features:product_id,










