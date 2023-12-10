import locale
from os import name

import pandas as pd
from bs4 import BeautifulSoup
from pyexpat import features
from selenium import webdriver

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#Initialize the browser driver
#driver = webdriver.Chrome()
driver = webdriver.Firefox()

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

driver.get('https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq')
contenido = driver.page_source
soup = BeautifulSoup(contenido, features='html.parser')
productos = soup.find_all(name='div',attrs={"class": "_4rR01T"})
precios = soup.find_all(name='div',attrs={"class": "_30jeq3 _1_WHN1"})
estrellas = soup.find_all(name='div',attrs={"class": "_3LWZlK"})
for producto in productos:
    products.append(producto.text)
for precio in precios:
    precio_sin_coma = precio.text.replace(",", "")
    precio_sin_simbolo = precio_sin_coma.replace("₹", "")
    print(precio_sin_simbolo)
    en_dolares = 0.012 * float(precio_sin_simbolo)
    prices.append(en_dolares)

#for s in estrellas:
#    ratings.append(s.text)
#    print(s.text)

print(products)
print(prices)
print(ratings)

for i, s in enumerate(estrellas):
    if i < 24: #Limita a 24 iteraciones
        ratings.append(s.text)
        print(s.text)
    else:
        break #Sale del bucle despues de 24 iteraciones

print(len(products))
print(len(prices))
print(len(ratings))

df = pd.DataFrame({'Producto':products,'Precio':prices,'Rating':ratings})
df.to_csv(path_or_buf='products.csv', index=False, encoding='utf-8')



