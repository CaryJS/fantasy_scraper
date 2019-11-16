import requests
from bs4 import BeautifulSoup

# This is the football player page for letter of alphabet
url_list_file= "player_urls.txt"
# we need to declare this base url because in order to access each player's year,
# we grab the hyperlinks from the soup. and the hyperlinks add onto this base URL.
BASE_URL = 'https://www.pro-football-reference.com{0}'

class Scraper:
	"""
	This class is used to scrape data from PFR's website.
	"""

	def __init__(self):
		self.player_urls = []
		self.player_stats = []

	def get_soup(self, url):
		# if self.simulate == "True":
			# with open("players_A.html", encoding="utf8") as f:
				# self.filecontent = f.read
				# soup = BeautifulSoup(self.filecontent, "html.parser")
				# print("did sim")
		# else:
		r = requests.get(url)
		webcontent = r.content
		soup = BeautifulSoup(webcontent, "html.parser")
		return soup

	def get_player_URLs(self, url_list):
		with open(url_list, "r") as f:
			self.player_urls = f.read().splitlines()
		return self.player_urls[0:5]

	def get_player_soup(self, player_url):
		r = requests.get(player_url)
		webcontent = r.content
		soup = BeautifulSoup(webcontent, "html.parser")
		return soup

	def get_player_stats(self, player_urls):
		player_ID = 0
		for player_url in player_urls:
			# here we have the URL, this is where we do the big magic part.
			# instantiate the player class here, and have the player class do the parsing.
			player = Player(player_url, player_ID)
			player_ID += 1
			soup = self.get_player_soup(player_url)
			print(player.get_years_active(soup))

			for
			# with the years active, we want to scrape the stats for each of those years and store them into the player instance
			# for season in seasons active
			#	if the list is not empty
			#		scrape, scrape, scrape

	def get_stats_from_gamelog(self, year_gamelog_url, year):
		"""
		:param year_gamelog_url: pass in the year's gamelog.
		:param year:
		:return:
		"""


	def get_season_stats(self,season_url):
		r = requests.get
		webcontent = r.content
		soup = BeautifulSoup(webcontent, "html.parser")
		# now how do we parse the information out of here and place it into the year stats for a player?

class Player():

	"""
	This class is constructed with the url for the player. A player object is in
	"""
	# This class is instantiated when the player URL is called. Once instantiated, the goals are to scrape all of the
	# relevant stats. So we ultimately need to get a get_player_stats method, which we call for every year.
	# TODO
	# 		Create method that returns years active in a list
	# TODO
	# 		Create method that can be used to return all the stats in a year
	# TODO
	# 		Figure out how we're creating and storing the dataset. The example script uses a staticmethod to generate
	# 		the dataset in a dict, such that the calling method can store it straight to a variable and key in the
	# 		parse information.
	# TODO
	# 		Create method that returns some unique number relative to the player such that it can be used to compare
	# 		to fantasy. Should be related to the players stats because those'll

	def __init__(self, player_url, player_id):
		self.url = player_url
		self.player_id = player_id

	def get_url_id(self):
		print(self.url)
		print(self.player_id)

	#In order for this to work, we get to get the soup for each profile from the URL.
	def get_years_active(self, profile_soup):
		"""Scrape a list of seasons that has stats for the player

			Args:
				- profile_soup (obj): The BeautifulSoup object for the player profile page

			Returns:
				- seasons (dict[]): List of dictionaries with meta information about season stats
		"""
		seasons = []
		gamelog_list = profile_soup.find('div', {'id': 'inner_nav'}).find_all('li')[1].find_all('li')
		if len(gamelog_list) > 0 and gamelog_list[0].contents[0].contents[0] == 'Career':
			for season in gamelog_list:
				seasons.append({
					'year': season.contents[0].contents[0],
					'gamelog_url': BASE_URL.format(season.contents[0]['href'])
				})
		return seasons

	@staticmethod
	def create_year_stats(self, player_id, year):
		return {
			'player_id': player_id,
			'year': year,
			# General stats
			'game_id': None,
			'date': None,
			'game_number': None,
			'age': None,
			'team': None,
			'game_location': None,
			'opponent': None,
			'game_won': None,
			'player_team_score': 0,
			'opponent_score': 0,
			# Passing stats
			'passing_attempts': 0,
			'passing_completions': 0,
			'passing_yards': 0,
			'passing_rating': 0,
			'passing_touchdowns': 0,
			'passing_interceptions': 0,
			'passing_sacks': 0,
			'passing_sacks_yards_lost': 0,
			# Rushing stats
			'rushing_attempts': 0,
			'rushing_yards': 0,
			'rushing_touchdowns': 0,
			# Receiving stats
			'receiving_targets': 0,
			'receiving_receptions': 0,
			'receiving_yards': 0,
			'receiving_touchdowns': 0,
			# Kick return stats
			'kick_return_attempts': 0,
			'kick_return_yards': 0,
			'kick_return_touchdowns': 0,
			# Punt return stats
			'punt_return_attempts': 0,
			'punt_return_yards': 0,
			'punt_return_touchdowns': 0,
			# Defense
			'defense_sacks': 0,
			'defense_tackles': 0,
			'defense_tackle_assists': 0,
			'defense_interceptions': 0,
			'defense_interception_yards': 0,
			'defense_interception_touchdowns': 0,
			'defense_safeties': 0,
			# Kicking
			'point_after_attemps': 0,
			'point_after_makes': 0,
			'field_goal_attempts': 0,
			'field_goal_makes': 0,
			# Punting
			'punting_attempts': 0,
			'punting_yards': 0,
			'punting_blocked': 0
		}

if __name__ == "__main__":
	scraper = Scraper()
	scraper.get_player_stats(scraper.get_player_URLs(url_list_file))

