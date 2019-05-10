from bs4 import BeautifulSoup
from get_intro import simple_get

raw_html = simple_get('https://www.pythonforbeginners.com')
html_soup = BeautifulSoup(raw_html, 'html.parser')


print(html_soup.title.string)

#p tags (none exist here)
#print(html_soup.p)

#first a tag
#print(html_soup.a)

#get all tags
#for tag in html_soup.find_all(True):
#    print(tag.name)

#extract all urls that have an a tag - a = anchor element, usually a link to another object
for link in html_soup.find_all('a'):
    print("-"*20)
    print("Link variable: {}".format(link))
    print("Get href: {}".format(link.get('href')))
    print("-"*20)
