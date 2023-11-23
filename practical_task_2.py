import pandas as pd

import matplotlib.pyplot as plt

MyDF=pd.read_csv("shopping_trends.csv", delimiter=",")

print(MyDF)

print(MyDF.describe())

print(MyDF.info())

# Подсчет количества заказов, совершенных мужчинами и женщинами 

gender=MyDF.groupby(['Gender'])['Gender'].count()

print (gender)

# Подсчет количества заказов по отдельным категориям заказов

category=MyDF.groupby(['Category'])['Category'].count()

print (category)

# Подготовка поля для диаграмм

fig, ax = plt.subplots(1,2)

fig.set_size_inches(10.5, 6)

fig.show()

# выведение диаграммы распределения заказов в зависимости от пола покупателей

ax[0].pie(gender.values, labels=gender.index, autopct='%1.1f%%')

ax[0].set(title='Purchases by gender')

# выведение диаграммы распределения заказов по категории товаров

ax[1].pie(category.values, labels=category.index, autopct='%1.1f%%')

ax[1].set(title='Purchases by category')
