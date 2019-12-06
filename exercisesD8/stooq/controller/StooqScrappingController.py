import requests
from bs4 import BeautifulSoup
import re

class StooqScrappingController:
    def __init__(self):
        # wykonanie żądania metodą GET na adres url -> obiekt strony
        stooq_page = requests.get("https://stooq.pl/n/?s=2&p=4+22&c=0")
        # na zwróconym obiekcie strony parsujemy do formatu html
        self.stooq_html = BeautifulSoup(stooq_page.content, 'html.parser')

    def filterDateAndTitle(self):
        date_pattern = re.compile(".{3}, [0-9]{1,2} .{3}, [0-9]{1,2}:[0-9]{1,2}")
        title_pattern = re.compile("^.{20,}$")
        # pobieramy dane z znaczników tr
        rows = self.stooq_html.find_all("tr")
        self.result = [[],[]]

        for index, row in enumerate(rows):
            if(index > 4):
                # filtrowanie daty
                date = str(row.find("td", {"id": "f13"})).replace('<td id="f13" nowrap="">', "").replace("</td>", "")
                if (len(str(row.a).split(">")) > 1):
                    title = str(row.a).split(">")[1].replace("</a","")
                    # szukanie tylko dat zgodnych z regexp
                    if(re.search(date_pattern, date) is not None):
                        self.result[1].append(date)
                    # szukamt tylko tytułów zgodnych z regexp
                    if(re.search(title_pattern,title) is not None and title[0:4] != "<img"):
                        self.result[0].append(title)
                    if(title[0:4] == "<img"):
                        title = "obrazek"
                        self.result[0].append(title)

    def getDateAndTitle(self):
        for i, title in enumerate(self.result[0]):
            if i > 0:
                print(title)
                print(self.result[1][i])

ssc = StooqScrappingController()
ssc.filterDateAndTitle()
ssc.getDateAndTitle()