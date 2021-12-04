# This is a script which main focus is to get the current price of a given cryptocoin

#Importing the requered modules
from bs4 import BeautifulSoup
import time
import requests

#Creating the function that will get the price of a cryptocurrency
def get_crypto_price(coin):
#Get the URL
    #url = "https://www.google.com/search?q="+coin+"+price"
	url = "https://www.google.com/search?channel=fs&client=ubuntu&q="+coin+"+price"
    
    #Making the request to the website
    HTML = requests.get(url) 
  
    #Parse the HTML
    soup = BeautifulSoup(HTML.text, 'html.parser') 
  
    #Finding the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
	
	return string
