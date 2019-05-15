from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import collections
import json

class HallOfFame(object):
    def __init__(self):
        #player_dict keeps track of each HOF player and what years that they played
        self.player_dict = {}
        #year_count keeps track of each yar and how many HOF players played that season
        self.year_count = {}
        self.start_action()

        self.print_all_years()
        self.print_all_players()

    def start_action(self):
        user_in = 0
        valid_options = [1,2]
        while user_in not in valid_options:
            user_in = int(input("How would you like to load the data?\n1)Website\n2)Json\n>"))
        if user_in == 1:
            print("Loading from website, please wait...")
            self.build_player_dict()
        elif user_in == 2:
            print("Loading from json, please wait...")
            self.read_from_json()
        else:
            print("Something went wrong...")
        print("Data loaded successfully")

    def view_action(self):
        print("What would you like to see")
        #1) Year with most players
        #2) Years by Player


    def build_player_dict(self):
        raw_html = simple_get('https://www.basketball-reference.com/')
        html_soup = BeautifulSoup(raw_html, 'html.parser')
        class_find = html_soup.find('form', class_='srbasic sr_goto no-deserialize single')
        #print(class_find)
        class_options = class_find.find_all('option')
        for option in class_options:
            player_name = option.text.strip()
            if player_name != 'Select a player':
                player_link = "https://www.basketball-reference.com{}".format(option.get("value"))
                #player_name = row.text.strip()
                # print("Link: {}".format(player_link))
                # print("Player Name: {}".format(player_name))
                # print("Opening new page..")
                player_html = simple_get(player_link)
                player_soup = BeautifulSoup(player_html, 'html.parser')
                #print(player_soup)
                table_find = player_soup.find('table', class_='row_summable sortable stats_table')
                #print("table_find:{}".format(table_find))
                table_tbody = table_find.find('tbody')
                #print("-!-"*10)

                temp_years = []
                for row in table_tbody.find_all('tr'):
                    if row.get('id'):
                        year = int(row.get('id').split('.')[1])
                        #add to year list that is added as the value in the player dictionary
                        temp_years.append(year)
                        self.update_year_count(year)

                self.player_dict[player_name] = temp_years
                #print(self.player_dict[player_name])
                print("Finished adding:{}".format(player_name))
                #input("Checking after row loop..\n>")#pause
        #want the year dictionary ordered
        self.year_count= collections.OrderedDict(sorted(self.year_count.items()))
        self.write_to_json()

    def update_year_count(self,current_year):
        #check to see if year is in dictionary yet
        if current_year not in self.year_count.keys():
            self.year_count[current_year] = 0
        self.year_count[current_year] += 1

    def print_all_years(self):
        for year in self.year_count.keys():
            print("Year:{}\nNum Players:{}".format(year,self.year_count[year]))

    def print_all_players(self):
        for player in self.player_dict.keys():
            print("Player:{}\nYears:{}".format(player,self.player_dict[player]))


    def write_to_json(self):
        #write playes and years
        with open('players.json', 'w') as player_json:
            json.dump(self.player_dict, player_json, indent=2, sort_keys=True)

        #write years and counts
        with open('years.json', 'w') as year_json:
            json.dump(self.year_count, year_json, indent=2, sort_keys=True)

    def read_from_json(self):

        with open('players.json', 'r') as players_in:
            self.player_dict = json.load(players_in)

        with open('years.json', 'r') as years_in:
            self.year_count = json.load(years_in)





#website open functions

def simple_get(url):
    try:
        #function closing will free up any network resources once they leave this block of code
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                #print("Good response")
                return resp.content
            else:
                return None
    except RequestException as e:
        print("Error during request to {} : {}".format(url, str(e)))

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)


if __name__ == '__main__':
    HallOfFame()
