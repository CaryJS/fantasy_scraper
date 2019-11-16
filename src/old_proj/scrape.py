import requests
from bs4 import BeautifulSoup

#r = requests.get("https://archive.fantasysports.yahoo.com/archive/nfl/2014/990684/draftresults?drafttab=team")
#content = r.content

with open("2014draft.html", encoding = "utf8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

clean = soup.prettify()

draft_rounds = soup.find_all("div", attrs={"class":"yui-u"})

players = []
for draft_round in draft_rounds:
    even_players.append(draft_round.find_all("td",attrs={"class":"player"}))


print(players)

# Get Names of players

all_players = []
for round in even_players:
    for player in round:
        all_players.append(player.find("a").contents[0])

print(all_players)
