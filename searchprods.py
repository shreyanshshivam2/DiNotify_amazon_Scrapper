from selectorlib import Extractor
import requests
import random
import json
import re
from time import sleep


def link_generate(product_name):
    try:
        empty_str=" "
        empty_str=empty_str.join(product_name.split())
        print(empty_str)
        product_name=empty_str.replace(" ",'+')
        print(product_name)
        url_search="https://www.amazon.in/s?k="+product_name

        print(url_search)
        fref= open("search_url.txt","w")
        fref.write(url_search)
        fref.close()
    except:
        print("link was not generated")


# as Amazon do not allow the scraping we need to make our requests look more like it
# is coming from actual PC so modifying the header by alternating the user-agent

def random_user_agent():
    try:
        user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        ]
        for i in range(1, 4):
            # Pick a random user agent
            user_agent = random.choice(user_agent_list)
            # Set the headers

            return user_agent
    except :
        print("user - agent not created")


def scrape(url):
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
          "User-Agent":random_user_agent(),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.amazon.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
         }

        print("Downloading %s"%url)  # downloading the HTML contents of the url.
        r = requests.get(url, headers=headers)

        # returning the error when the page was actually blocked.
        if r.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in r.text:
                print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
            else:
                print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
            return None
        # Pass the HTML of the page and create
        return e.extract(r.text)
    except :
        print("scraping function failed")


# the entry point of the application which will be recieved from the front end
print("Enter the product name")
product_name = str(input())


link_generate(product_name)  # the function will generate the url and store the URL in search_results.txt which will be used for later references.

e = Extractor.from_yaml_file('search_results.yml') # Creating the YAML file extractor
print(e)

with open("search_url.txt",'r') as urllist, open('search_results_output.jsonl','w') as outfile:
    for url in urllist.read().splitlines():
        data = scrape(url)
        if data:
            for product in data['products']:
                product['search_url'] = url
                product['price']=str(product['price']).lstrip("\u20b9")

                json.dump(product,outfile)
                outfile.write("\n")
            print("product details stored in json format in search_results_output.jsonl")


