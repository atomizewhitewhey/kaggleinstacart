#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:05:46 2017

@author: matthewyeozhiwei
"""
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
import seaborn as sns

aisles = pd.read_csv('/Users/matthewyeozhiwei/datasets/KaggleInstacart/aisles.csv')
departments = pd.read_csv('/Users/matthewyeozhiwei/datasets/KaggleInstacart/departments.csv')
products = pd.read_csv('/Users/matthewyeozhiwei/datasets/KaggleInstacart/products.csv')
orderprior = pd.read_csv('/Users/matthewyeozhiwei/datasets/KaggleInstacart/order_products__prior.csv')
ordertrain = pd.read_csv('/Users/matthewyeozhiwei/datasets/KaggleInstacart/order_products__train.csv')


orderspriorprod = pd.merge(orderprior, products, how = 'inner', on = 'product_id')
orderstrainprod = pd.merge(ordertrain, products, how = 'inner', on = 'product_id')

orderspriorprod.product_name.value_counts().head(100)
orderstrainprod.product_name.value_counts().head(100)

def numberitemshist(df):
    fig = plt.figure(figsize = (15,10))
    ax = fig.gca()
    sns.barplot(df.groupby('order_id')['add_to_cart_order'].aggregate('max').reset_index().add_to_cart_order.value_counts().index.values,
                df.groupby('order_id')['add_to_cart_order'].aggregate('max').reset_index().add_to_cart_order.value_counts().values)
    ax.set_title('Histogram of No. Of Products Purchased')
    
## numberitemshist(orderstrainprod)

def popularitemplot(df, N):
    fig = plt.figure(figsize = (10,10))
    ax = fig.gca()
    sns.barplot(df.product_name.value_counts().head(N).index.values,
                df.product_name.value_counts().head(N).values)
    ax.set_title('Top ' + str(N) + 'Products Purchased')
    ax.set_ylabel('Number of Products')
    
## popularitemplot(orderstrainprod, 10)

def cartorderplot(df, N):
    for n in range(1, N):
        fig = plt.figure(figsize = (10,10)) 
        ax = fig.gca()
        sns.barplot(df[df['add_to_cart_order'] == n].product_name.value_counts().head(10).values,
                    df[df['add_to_cart_order'] == n].product_name.value_counts().head(10).index.values)
        ax.set_title('Top 10 products ordered ' + str(n) + ' place')

## cartorderplot(orderspriorprod, 5)
## cartorderplot(orderstrainprod, 5)

def summary_prods(df):
    df = df.groupby('reordered')['product_id'].aggregate({'TotalCount': 'count'}.reset_index())
    df['Percentage'] = df['TotalCount'].apply(lambda x: (x / (df['TotalCount'].sum()) * 100))
    print(df)


