from bs4 import BeautifulSoup
import requests
import csv


#Function to retreive Item's name
def ItemName_element_verification(Item_element, writer):
    if Item_element:
        Item_Name = Item_element.text.strip()
        writer.writerow({'Item Name': Item_Name})
        return Item_Name
    else: 
        print("Item Name Element was not found")


#Function to retreive Item's price
def ItemPrice_element_verification(Item_element, writer):
    if Item_element:
        Item_Price = Item_element.text.strip()
        writer.writerow({'Item Price': Item_Price})
        return Item_Price
    else: 
        print("Item Price Element was not found")


#Function to retreive Item's specs
def Spec_Table_verification(Spec_Table_element, writer):
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
                    writer.writerow({label: content})
    else:
        print("Table not found.")
