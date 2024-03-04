from bs4 import BeautifulSoup
import requests
import FunctionsFile
import csv

# Function to scrape and process eBay search results page
def scrape_ebay_search(url,writer):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser') 
    overall_items = soup.find_all(class_='s-item s-item__pl-on-bottom')
    
    for item in overall_items:   
        # Extract item URL
        item_url = item.find('a', class_='s-item__link')['href']
        # Make a separate request to the item URL
        item_response = requests.get(item_url)
            
        if item_response.status_code == 200:
            item_soup = BeautifulSoup(item_response.text, 'html.parser')
            # Extract item information from the item webpage
            item_name_element = item_soup.find(class_='x-item-title__mainTitle')
            item_price_element = item_soup.find(class_='x-price-primary')
            spec_table_element = item_soup.find('div', class_='ux-layout-section-evo__item--table-view')
            # Process item information
            FunctionsFile.ItemName_element_verification(item_name_element, writer)
            FunctionsFile.ItemPrice_element_verification(item_price_element, writer)
            FunctionsFile.Spec_Table_verification(spec_table_element, writer)
        else:
            print(f'Failed to fetch item page: {item_url}')     

##############################################################################################
#start of code: 

# URL of eBay search results page for Rolex men's watches
url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=rolex+mens+watch&_sacat=0&_ipg=240'
response = requests.get(url)


if response.status_code == 200:  
    soup = BeautifulSoup(response.text, 'html.parser') 
     #This creates and opens a csv with permission to write in it. 
    with open('EbayRolex_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # column names
        fieldnames = ['Item Name', 'Item Price', 'Specifications']
        # makes writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writes column names in the csv file
        writer.writeheader()

    # Start scraping eBay search results
    scrape_ebay_search(url,writer)
    
    #loops through function
    next_page_link = soup.find('a', class_='pagination__next icon-link')
    if next_page_link:
        next_page_url = 'https://www.ebay.com' + next_page_link['href']
        scrape_ebay_search(next_page_url,writer)
else: 
        print('Failed to fetch the website:', response.status_code)

