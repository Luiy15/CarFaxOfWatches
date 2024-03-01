from bs4 import BeautifulSoup
import requests
# import main

url = 'https://www.ebay.com/itm/116010623346?itmmeta=01HQSNF4JDAQ4ZPZ2J283T8BZT&hash=item1b02c5a172:g:DJcAAOSw1N5le6so&itmprp=enc%3AAQAIAAAA4AWANgxJSbTfzRUukiiVqlrjbTxE0thUXFSEeQP5iIXGpLkT6uiYK%2BGrqH3xK891h9ENee5JOlYkxjxN%2F3da1q5wkIEgZW2ANVCAalgMIbA3npfAIjz0INnCgRGm%2B11szeKw96t1vriB9AkdOPVRWLeYvYP9VhyO57Nnx6co8rxTyawQRH3lJBlt%2B%2Bf8UgwCrP2ZF%2FRoDc%2FKXTj0PiWpVNaDtjMXOuPZclsXsif7I56Rg5IFri7vCZgATCAOfSJZyqGTqsXZAJihzDXVPHfQGuP15gD6wEnn8xtojr1%2Bi07k%7Ctkp%3ABk9SR8jJvLW-Yw'
response =  requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')  

def ItemName_element_verification(Item_element):
    if Item_element:
        Item_Name = Item_element.text.strip()
        print("Item Name:", Item_Name)
        return Item_Name
  
    else: 
        print("Item Element was not found")
        
def ItemPrice_element_verification(Item_element):
    if Item_element:
        Item_Price = Item_element.text.strip()
        print("Item Price:", Item_Price)
        return Item_Price
  
    else: 
        print("Item Element was not found")
        



def Spec_Table_verification(Spec_Table_element):
    table = Spec_Table_element
    # checks table element 
    if table:
    # Loop through each row in the table
        for row in table.find_all('div', class_='ux-layout-section-evo__row'):
            # Find all columns within the row
            columns = row.find_all('div', class_='ux-layout-section-evo__col')
            # Iterate through each column
            for col in columns:
                # Find label and content elements within the column
                label_element = col.find('div', class_='ux-labels-values__labels-content')
                content_element = col.find('div', class_='ux-labels-values__values-content')
                # Extract text from label and content elements
                if label_element and content_element:
                    label = label_element.text.strip()
                    content = content_element.text.strip()
                    print(f"{label}: {content}")
    else:
        print("Table not found.")
