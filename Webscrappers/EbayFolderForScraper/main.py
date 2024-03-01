from bs4 import BeautifulSoup
import requests
import FunctionsFile

#URL that it's scraping from
url = 'https://www.ebay.com/itm/116010623346?itmmeta=01HQSNF4JDAQ4ZPZ2J283T8BZT&hash=item1b02c5a172:g:DJcAAOSw1N5le6so&itmprp=enc%3AAQAIAAAA4AWANgxJSbTfzRUukiiVqlrjbTxE0thUXFSEeQP5iIXGpLkT6uiYK%2BGrqH3xK891h9ENee5JOlYkxjxN%2F3da1q5wkIEgZW2ANVCAalgMIbA3npfAIjz0INnCgRGm%2B11szeKw96t1vriB9AkdOPVRWLeYvYP9VhyO57Nnx6co8rxTyawQRH3lJBlt%2B%2Bf8UgwCrP2ZF%2FRoDc%2FKXTj0PiWpVNaDtjMXOuPZclsXsif7I56Rg5IFri7vCZgATCAOfSJZyqGTqsXZAJihzDXVPHfQGuP15gD6wEnn8xtojr1%2Bi07k%7Ctkp%3ABk9SR8jJvLW-Yw'
response =  requests.get(url)

if response.status_code == 200: 
    #assigns website url to soup
    soup = BeautifulSoup(response.text, 'html.parser') 
     
    #grabs and sets the element of the wanted to a var
    Item_Name_element = soup.find(class_='x-item-title__mainTitle') 
    Item_Price_element = soup.find(class_='x-price-primary')
    
    #Looks for the table that has all the wathces info and grabs it's element
    # Spec_Table_element = soup.find(class_='ux-layout-section-evo__item ux-layout-section-evo__item--table-view')
    Spec_Table_element = soup.find('div', class_='ux-layout-section-evo__item--table-view')
    
    # This is so the program checks if the elements/table is fetchable
    FunctionsFile.ItemName_element_verification(Item_Name_element)
    FunctionsFile.ItemPrice_element_verification(Item_Price_element)
    FunctionsFile.Spec_Table_verification(Spec_Table_element)
    

    
else: 
    print('Failed to fetch the website:', response.status_code)
    
    
