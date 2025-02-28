import requests
from bs4 import BeautifulSoup

rofl = requests.get("https://opennav.com/waypoint/US/")
soup = BeautifulSoup(rofl.text, "html.parser")

for row in soup.find_all("tr"):
    print (row.find("td").text)