# DiNotify_amazon_Scrapper
Assigned By DiNotify
The project is an amazon web scrapper which extracts the product details(title,reviews,rating,price etc.) from Amazon.com of the product it recieves from the front end. Extracting details from amazon is challenging because the webpages are created dynamically and the functionaries are placed to classify requests as bot and blocking them.
As amazon prevents crawling on its website the project randomises the headers of the rquest sent to Amazon in order to make it more of natural requests and hereby preventing it from being classified as bot.
The project uses selectorlib,re,Yaml,requests of python as major libraries and language.
The output of the project is a json file containig all the product details in json format which can be integrated into backend.
