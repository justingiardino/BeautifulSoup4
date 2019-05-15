import json
with open('players.json', 'r') as players_in:
    pretty_json = json.load(players_in)
with open('players_new.json ', 'w') as players_out:
    json.dump(pretty_json, players_out, indent=2, sort_keys=True)
