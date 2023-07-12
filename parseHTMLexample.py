import bs4, requests

def getEbayPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()  #this will crash, Amazon needs some user header to avoid bot detection
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # some warnings may pop up when running bs4, pass "html.parser" as second arugment 

    elems = soup.select('#prcIsum')
    # find the css path/selector for the elemnent of interest from website
    # using soup.select('address for price element of website')
    # should return a list of element objects matching
    # should only be one in our example

    return elems[0].text.strip()
    # string value of element within elems[0]
    # strip removes whitespace

price = getEbayPrice('https://www.ebay.co.uk/itm/153951705175')
print('The price is ' + price)




"""
AMAZON CODE DOESNT WORK
def getAmazonPrice(productURL):
    headers = {'User-Agent':'Mozilla/5.0(Macintosh;Intel Mac OS X 10_9_5)'
               'AppleWebkit 537.36(KHTML,like Gecko) Chrome',
               'Accept':'text/html,application/xhtml+xml,application/xml;' 
               'q=0.9,image/webp,*/*;q=0.8'}
    # headers avoid bot detection
    
    res = requests.get(productURL, headers)
    res.raise_for_status()  #this will crash, Amazon needs some user header to avoid bot detection
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # some warnings may pop up when running bs4, pass "html.parser" as second arugment 

    elems = soup.select('#buyNewSection > div > div > span > span')
    # find the css path/selector for the elemnent of interest from website
    # using soup.select('address for price element of website')
    # should return a list of element objects matching
    # should only be one in our example

    return elems[0].text.strip()
    # string value of element within elems[0]
    # strip removes whitespace

price = getAmazonPrice('https://www.amazon.co.uk/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?crid=10BABFLQMFMDN&dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1591451047&sprefix=automate+%2Caps%2C158&sr=8-1')
print('The price is ' + price)

"""
