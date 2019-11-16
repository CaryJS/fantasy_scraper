import requests
from bs4 import BeautifulSoup
import string #allows an import of the alphabet
import urllib.parse
import json

# This is the football player page for letter of alphabet
all_players_url_template = "https://www.pro-football-reference.com/players/[*]/"
# list of template url's for every player.
single_player_url_template = "https://www.pro-football-reference.com/[*]"
# this is the only edit I am making, made it in the browser

class Scraper:
	"""
	This class is used to scrape data from PFR's website.

	"""

	def __init__(self, master_url):
		self.url = master_url

	def get_soup(self, url):
#		if self.simulate == "True":
#			with open("players_A.html", encoding="utf8") as f:
#				self.filecontent = f.read
#				soup = BeautifulSoup(self.filecontent, "html.parser")
#				print("did sim")
#		else:
		r = requests.get(url)
		self.webcontent = r.content
		soup = BeautifulSoup(self.webcontent, "html.parser")
		return soup

	def get_players_in_letter(self, letter):
		current_url = self.url.replace("[*]", letter)
		letter_page = self.get_soup(current_url)
		# class="section_content" id="div_players"
		# .find_all("td", {"class":"Table2__td"})
		h2_list = letter_page.find_all("h2")
		if h2_list[1].text == "0":
			return
		else:
			player_section = letter_page.find("div", {"class": "section_content", "id": "div_players"})
			players_in_letter = player_section.find_all("a")
			player_URLs_in_letter = []
			for player in players_in_letter:
				suffix = player["href"]
				suffix = suffix.replace("'", "%27")  # this is messy. why don't urllib include the percent encoding?
				url = single_player_url_template.replace("[*]", suffix)
				player_URLs_in_letter.append(url)
			return player_URLs_in_letter

if __name__ == "__main__":
	scraper = Scraper(all_players_url_template)

	for letter in list(string.ascii_uppercase):
		player_urls = scraper.get_players_in_letter(letter)
		with open("newfile.txt", "a") as f:
			for player in player_urls:
				print(player)
				f.write(player)
#				f.write("\n")
