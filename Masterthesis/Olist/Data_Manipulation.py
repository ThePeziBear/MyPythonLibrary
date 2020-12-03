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

df_products
df_order_items

df_count_items=df_order_items.groupby('product_id').count()
df_count_items=df_count_items.sort_values(by='order_id', ascending=False)
df_count_items=(df_count_items.iloc[:5000000]).sort_values(by='order_id', ascending=False)
df_count_items

#barblot_product1 = df_count_items['order_id'].plot.bar(stacked=True)

#Merge dataframes by 'product_id','product_category_name','order_item_id','price','seller_id','freight_value','product_description_lenght','product_photos_qty','review_score','review_comment_title','review_comment_message'
dfmerge = pd.merge(df_order_items,df_products, how='inner', left_on='product_id', right_on='product_id')#.set_index('Auswahl Spalte als Index')

dfmerge2=pd.merge(dfmerge,df_order_reviews,on='order_id')
dfmerge2_count=dfmerge2.groupby('review_score').count()


dfmerge3=dfmerge2[['product_id','product_category_name','order_item_id','price','seller_id','freight_value','product_description_lenght','product_photos_qty','review_score','review_comment_title','review_comment_message']]
dfset_1=dfmerge3

barblot_product2 = df_count_items['order_id'].plot.bar(stacked=True)

df_cool_stuff=df_merge2[df_merge2['product_category_name']=='cool_stuff']

# Predictive Opportunities

#1 Predict score_reviews
df_count_reviews=df_order_reviews.groupby('review_score').count()
barplot_review1 = df_count_reviews['review_id'].plot.bar(stacked=True)
#Features:product_id,

#Datavisualierung dfset_1

subset1=dfset_1[['product_description_lenght','product_photos_qty','review_score']]

sns.lmplot(x='product_description_lenght',y='product_photos_qty',data=dfset_1,hue='review_score',palette='coolwarm'),#hue: Trennung von kategorischen Parameter
            #markers=['o','v'], #Veränderung der Symbole
            #scatter_kws={'s':100}) #scatter_kws: Definition von der Göße der Symbole
plt.show()


X=dfset_1[['product_description_lenght','product_photos_qty']]
y=dfset_1['review_score']





#2 Predict Sales aufgrund von Produktfotos Und/Oder Länge Produktnamen


#3??