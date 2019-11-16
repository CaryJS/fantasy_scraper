import requests
from bs4 import BeautifulSoup
from AssignID import Counter

# r = requests.get("https://archive.fantasysports.yahoo.com/archive/nfl/2014/990684/draftresults?drafttab=team")
# content = r.content

playerID = Counter()

with open("top 300 2015.html", encoding = "utf8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

table = soup.find_all("aside", {"class":"inline inline-table"})

row = table[1].find_all("tr", {"class":"last"})

player_names = []
player_URL = []
player_pos = []
for player in row:
    player_names.append(player.find("a").contents[0])
    player_URL.append(player.find("a")["href"].replace("_", "stats/_"))
    player_pos.append(player.find("td").contents[2].replace(", ", ""))

# for name, pos in player_names, player_pos:
# ranked_players["position"] = player_pos

zipped = zip(player_names, player_URL, player_pos)


#trim the list down to the top 10 players
ranked_players = list(zipped)[0:10]

def get_player_page():
    pass

def get_years_active(stattable):
    table = stattable.find_all("td", {"class":"Table2__td"})

    years_active = []

    for i in table:
        if i.text == "Career":
            break
        elif i.text.isalpha():
            pass
        else:
            years_active.append(i.text)
    return years_active

def get_rushing_stats(stattable):
    table = stattable.find_all("tbody", {"class":"Table2__tbody"})

    # get all of the rows within the table. Only need the one table, index out.
    row = table[1].find_all("tr", {"class":"Table2__tr Table2__tr--sm Table2__even"})

    # delete the career stats row from the table.
    data = row[:-1]

    career_rushing_stats = []
    keys = ["GP", "RUSHATT", "RUSHYDS", "RUSHAVG", "RUSHTD", "RUSHLNG", "RUSHFD", "RUSHFUM", "RUSHLST"]
    for year in data:
        year_stats = []
        year_stat_soup = year.find_all("td", {"class":"Table2__td"})

        # Need to pull out the numbers from the soup into a list
        # before assembling into the year stats dictionary.
        for stat_soup in year_stat_soup:
            year_stats.append(stat_soup.text)

        #zip up the stats with the headers into a dictionary.
        # Append the dictionaries into a list. Return the list.
        career_rushing_stats.append(dict(zip(keys, year_stats)))

    return(career_rushing_stats)


def get_receiving_stats(stattable):
    table = stattable.find_all("tbody", {"class":"Table2__tbody"})

    # get all of the rows within the table. Only need the one table, index out.
    row = table[1].find_all("tr", {"class":"Table2__tr Table2__tr--sm Table2__even"})

    # delete the career stats row from the table.
    data = row[:-1]

    career_receiving_stats = []
    keys = ["GP", "REC", "TGTS", "RECYDS", "RECAVG", "RECTD", "RECLNG", "RECFD", "RECFUM", "RECLST"]
    for year in data:
        year_stats = []
        year_stat_soup = year.find_all("td", {"class":"Table2__td"})

        # Need to pull out the numbers from the soup into a list
        # before assembling into the year stats dictionary.
        for stat_soup in year_stat_soup:
            year_stats.append(stat_soup.text)


        # zip up the stats with the headers into a dictionary.
        # Append the dictionaries into a list. Return the list.
        career_receiving_stats.append(dict(zip(keys, year_stats)))
    return(career_receiving_stats)

def get_passing_stats(stattable):
    table = stattable.find_all("tbody", {"class":"Table2__tbody"})

    # get all of the rows within the table. Only need the one table, index out.
    row = table[1].find_all("tr", {"class":"Table2__tr Table2__tr--sm Table2__even"})

    # delete the career stats row from the table.
    data = row[:-1]

    career_passing_stats = []
    keys = ["GP", "CMP", "ATT", "CMP%", "PASSYDS", "PASSAVG", "PASSTD", "INT", "PASSLNG", "SACK", "FUM", "RTG", "QBR"]
    for year in data:
        year_stats = []
        year_stat_soup = year.find_all("td", {"class":"Table2__td"})

        # Need to pull out the numbers from the soup into a list
        # before assembling into the year stats dictionary.
        for stat_soup in year_stat_soup:
            year_stats.append(stat_soup.text)

        # zip up the stats with the headers into a dictionary.
        # Append the dictionaries into a list. Return the list.
        career_passing_stats.append(dict(zip(keys, year_stats)))
    return career_passing_stats


def build_player_stats(ranked_player, player_years, rushing_stats, receiving_stats, passing_stats):
    """
    Goal is to build a list of dicts of the following format:

    Player ID, Player Name, Player Year, Rushing Stats, Receiving Stats, Passing Stats
    Do I have to put in the same size

    """

    print(rushing_stats)

    all_player_stats = []

    # initialize a year list
    # Initialize a dict with the player name, player ID, because those are the only parameters that
    # do not change every year
    # Use playerID.getID() to enumerate the players
    all_year_stats = []
    year_stats = {"PLAYERID": playerID.getID(), "PLAYERNAME": ranked_player[0]}
	for year in player_years:
		# Add in the year
		 year_stats["YEAR"] = year
		# year_stats["RUSHYDS"] = rushing_stats

    # print(rushing_stats)

for ranked_player in ranked_players:
	if (ranked_player[2] == "DST") or (ranked_player[2] == "K"):
        pass
    else:
        r = requests.get(ranked_player[1])
        content = r.content
        soup = BeautifulSoup(content, "html.parser")

        # metric here is code for the tables of rushing, receiving, passing.

        stattables = soup.find_all("section", {"class":"Table2__responsiveTable Table2__table-outer-wrap Table2--hasFixed-left pt4"})

        stattables = stattables[0:3]

        # Send in only the rushing table
        # Returns the years active in a list.
#        get_years_active(stattables[0])

        # Send in only the Rushing table.
        # Returns rushing stats in a list of dicts
#        get_rushing_stats(stattables[0])

        # Send in only the Receiving table.
        # Returns receiving stats in a list of dicts
#        get_receiving_stats(stattables[1])

        # Send in only the Passing table.
        # Returns passing stats in a list of dicts
#        get_passing_stats(stattables[2])

        build_player_stats(ranked_player, get_years_active(stattables[0]), get_rushing_stats(stattables[0]), get_receiving_stats(stattables[1]), get_passing_stats(stattables[2]))
        break
