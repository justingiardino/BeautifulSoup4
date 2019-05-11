from bs4 import BeautifulSoup
from get_intro import simple_get

raw_html = simple_get('https://en.wikipedia.org/wiki/List_of_players_in_the_Naismith_Memorial_Basketball_Hall_of_Fame')
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
# for span in html_soup.find_all('span'):
#     print("-"*20)
#     print("Span variable: {}".format(span))
#     print("Get data-sort-value: {}".format(span.get('data-sort-value')))
#     print("-"*20)

soup_table = html_soup.find('table')
table_body = soup_table.find('tbody')
table_rows = table_body.find_all('tr')
for row in table_rows:
    name = row.find('a')
    if name:
        name_out = name.get('title')
        if "(" in name_out:
            name_out = name_out.split("(")[0]
        print(name_out)


raw_html = simple_get('https://www.basketball-reference.com/')
html_soup = BeautifulSoup(raw_html, 'html.parser')

#form name  you are looking for is class="srbasic sr_goto no-deserialize single"
