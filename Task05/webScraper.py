from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


def getTitlesprod(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

def getpricing(soup):
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
    except AttributeError:
        try:
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
        except:
            price = ""
    return price

def getRating(soup):
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	
    return rating

def getrevCount(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count = ""	
    return review_count

def getavail(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()
    except AttributeError:
        available = "Not Available"	
    return available


if __name__ == '__main__':

    HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})
    URL = "https://www.amazon.com/s?k=graphics+card&ref=nb_sb_noss"
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    links_list = []
    for link in links:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[],"availability":[]}
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        d['title'].append(getTitlesprod(new_soup))
        d['price'].append(getpricing(new_soup))
        d['rating'].append(getRating(new_soup))
        d['reviews'].append(getrevCount(new_soup))
        d['availability'].append(getavail(new_soup))

    amazonDataframe = pd.DataFrame.from_dict(d)
    amazonDataframe['title'].replace('', np.nan, inplace=True)
    amazonDataframe = amazonDataframe.dropna(subset=['title'])
    amazonDataframe.to_csv("productsandDetails.csv", header=True, index=False)