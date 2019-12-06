import requests
from bs4 import BeautifulSoup
import re

class StooqScrappingController:
    def __init__(self):
        # wykonanie żądania metodą GET na adres url -> obiekt strony
        stooq_page = requests.get("https://stooq.pl/n/?s=2&p=4+22&c=0")
        # na zwróconym obiekcie strony parsujemy do formatu html
        self.stooq_html = BeautifulSoup(stooq_page.content, 'html.parser')

    def filterDateAndTitleAndUrl(self):
        date_pattern = re.compile(".{3}, [0-9]{1,2} .{3}, [0-9]{1,2}:[0-9]{1,2}")
        title_pattern = re.compile("^.{20,}$")
        urlPattern = re.compile("^https:\/\/stooq.pl\/n\/\?f=.*")
        # pobieramy dane z znaczników tr
        rows = self.stooq_html.find_all("tr")
        # [titles , dates, links]
        self.result = [[], [], []]

        for index, row in enumerate(rows):
            # filtrowanie daty
            try:
                url = "https://stooq.pl/"+ str(row.a['href'])
                if(re.search(urlPattern, url)):
                    self.result[2].append(url)
            except:
                pass
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

    def getContentByUrl(self, url):
        content_page = requests.get(url)
        content_html = BeautifulSoup(content_page.content, 'html.parser')

        content = content_html.find_all("font", attrs={"id" : "f13"})     # szukamy znacznika font z parametrem id = f13

        for c in content:
            print(c)


    def getDateAndTitle(self):
        for i, value in enumerate(self.result[1]):
            if i > 0:
                print(self.result[0][i])    # tytuły
                print(self.result[1][i])    # daty
                print(self.result[2][i])    # linki



ssc = StooqScrappingController()
# ssc.filterDateAndTitleAndUrl()
# ssc.getDateAndTitle()
ssc.getContentByUrl("https://stooq.pl/n/?f=1326700&c=0&p=4+22")