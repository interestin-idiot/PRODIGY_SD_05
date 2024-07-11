# Software Development Intern At Prodify Infotech 
## Task 5 : Web Scraping

Create a program that extracts product information, such as names, prices, and ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.

# Objectives:

1. **Extract Product Information**: Collect product names, prices, ratings, review counts, and availability from an e-commerce website.
2. **Data Storage**: Save the extracted data in a structured format like a CSV file for further analysis or use.
3. **Automation**: Automate the process of scraping data from multiple product pages.

# Dependencies:

1. **BeautifulSoup**: For parsing HTML and extracting data.
2. **Requests**: For making HTTP requests to retrieve web pages.
3. **Pandas and NumPy**: For data manipulation and storage.
4. **Python 3.12**

# Project Structure

## Main Components:

1. Functions to extract product details (title, price, rating, review count, availability).
2. Main script to handle web requests, parse HTML, and store extracted data in a CSV file.

# Implementation Details
## Functions for Data Extraction:

1. **getTitlesprod(soup)**: Extracts the product title from a given HTML soup.
2. **getpricing(soup)**: Extracts the product price from a given HTML soup.
3. **getRating(soup)**: Extracts the product rating from a given HTML soup.
4. **getrevCount(soup)**: Extracts the number of reviews for a product from a given HTML soup.
5. **getavail(soup)**: Extracts the availability status of a product from a given HTML soup.

## Main Script:

1. **Headers and URL Setup**: Define the user-agent and the URL to scrape.
2. **Initial Web Request**: Retrieve the main search results page containing links to individual product pages.
3. **Extract Links**: Extract links to individual product pages from the search results.
4. **Iterate Through Links**: For each product link, make a web request and extract product details using the defined functions.
5. **Data Storage** Store the extracted data in a Pandas DataFrame and save it to a CSV file.