import requests
from bs4 import BeautifulSoup
import random

plant_list = [
    ["Columbine", "c"],
    ["Wild Ginger", "wg"],
    ["Butterfly Weed", "bw"],
    ["White Wood Aster", "wwa"],
    ["New England Aster", "nea"],
    ["Aromatic Aster", "aa"],
    ["Blue Wild Indigo", "bwi"],
    ["Turtlehead", "t"],
    ["Green-and-Gold", "gag"],
    ["Bugbane", "bb"],
    ["Tall Coreopsis", "tc"],
    ["Wild Bleeding Heart", "wbh"],
    ["Joe-pye Weed", "jpw"],
    ["Cranesbill", "cr"],
    ["Common Sneezeweed", "cs"],
    ["Swamp Sunflower", "ss"],
    ["False Sunflower", "fs"],
    ["Alumroot", "al"],
    ["Dwarf Crested Iris", "dci"],
    ["Gayfeather", "g"],
    ["Michigan Lily", "ml"],
    ["Great Blue Lobelia", "gbl"],
    ["Virginia Bluebells", "vb"],
    ["Beebalm", "beebalm"],
    ["Wild Bergamot", "wb"],
    ["Beardtongue", "b"],
    ["Summer Phlox", "sp"],
    ["Jacob's Ladder", "jl"],
    ["Solomon's Seal", "sos"],
    ["Slender Mountain Mint", "smm"],
    ["Black-Eye Susan", "bes"],
    ["Golden Ragwort", "gr"],
    ["Narrow-leaved Blue-Eyed Grass", "nlbeg"],
    ["False Solomon's Seal", "fss"],
    ["Showy Goldenrod", "sg"],
    ["Foam Flower", "ff"],
    ["New York Ironweed", "nyi"],
    ["Culver's Root", "cur"],
]

def scrapeWikiArticle(url):
	response = requests.get(
		url=url,
	)
	
	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

	allLinks = soup.find(id="bodyContent").find_all("a")
	random.shuffle(allLinks)
	linkToScrape = 0

	for link in allLinks:
		# We are only interested in other wiki articles
		if link['href'].find("/wiki/") == -1: 
			continue

		# Use this link to scrape
		linkToScrape = link
		break

	scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/")