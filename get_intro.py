from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#using HTTP GET to return text contents of a website
def simple_get(url):
    try:
        #function closing will free up any network resources once they leave this block of code
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                print("Good response")
                return resp.content
            else:
                return None
    except RequestException as e:
        print("Error during request to {} : {}".format(url, str(e)))

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

if __name__ == '__main__':
    raw_html = simple_get('https://realpython.com/python-web-scraping-practical-introduction/')
    print(len(raw_html))
    #print(raw_html)
