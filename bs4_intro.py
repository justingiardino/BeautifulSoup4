from bs4 import BeautifulSoup
from get_intro import simple_get

def demo_select():
    raw_html = open('example.html').read()
    #pass the raw html into the Beautiful Soup constructor, if you omit the html.parser then you will get a warning
    html = BeautifulSoup(raw_html, 'html.parser')
    #use select to locate the elements in the document, in this case looking for p for paragraph elements
    for p in html.select('p'):
        if p['id'] == 'walrus':
            print(p.text)
    for tag in html.find_all(True):
        print(tag.name)

def math_names():
    #Using mathemetician site to get names
    math_raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
    math_html = BeautifulSoup(math_raw_html, 'html.parser')
    #to determine what tag you want to select, use the F12 dev tools in your browser and find the tag that you want, usually an id or class element
    #in this lase we are using li as our select
    #use a set to get rid of duplicates
    names = set()
    #using enumerate function, which will loop through the list of math_html.select values and store each element as li, and also keep a counter in i
    #for  i, li in enumerate(math_html.select('li')):
    for li in math_html.select('li'):
        #print(i, li.text)
        for name in li.text.split('\n'):
            if len(name) > 0:
                names.add(name.strip())
    print(list(names))


if __name__ == '__main__':
    demo_select()
    #math_names()
