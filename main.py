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

#Create a main function to consistently show the price of the cryptocurrency
def main():
  #Set the last price to negative one
  last_price = -1
  #Create an infinite loop to continuously show the price
  while True:
    #Choose the cryptocurrency that you want to get the price of (e.g. bitcoin, litecoin)
    crypto = input("Please, enter the cryptocoin: ")
    #Get the price of the crypto currency
    price = get_crypto_price(crypto)
    #Check if the price changed
    if price != last_price:
      print(crypto+' price: ',price) #Print the price
      last_price = price #Update the last price
    time.sleep(3) #Suspend execution for 3 seconds.

main()
