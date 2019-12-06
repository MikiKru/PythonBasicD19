import requests
from bs4 import BeautifulSoup

# wykonanie żądania metodą GET na adres url -> obiekt strony
stooq_page = requests.get("https://stooq.pl/n/?s=2&p=4+22&c=0")

# na zwróconym obiekcie strony parsujemy do formatu html
stooq_html = BeautifulSoup(stooq_page.content, 'html.parser')

# print(stooq_html.prettify())

# dates = stooq_html.findAll("td", {"id" : "f13"})
# print("Pobrana data")
# print(str(dates[4]).replace('<td id="f13" nowrap="">',"").replace("</td>",""))

import re
date_pattern = re.compile(".{3}, [0-9]{1,2} .{3}, [0-9]{1,2}:[0-9]{1,2}")
title_pattern = re.compile("^.{20,}$")

rows = stooq_html.find_all("tr")
result = [[],[]]

print("Rekordy")
for index, row in enumerate(rows):
    if(index > 4):
        # filtrowanie daty
        date = str(row.find("td", {"id": "f13"})).replace('<td id="f13" nowrap="">', "").replace("</td>", "")
        if (len(str(row.a).split(">")) > 1):
            title = str(row.a).split(">")[1].replace("</a","")
            # szukanie tylko dat zgodnych z regexp
            if(re.search(date_pattern, date) is not None):
                # print("Data:", date)
                result[1].append(date)
            # szukamt tylko tytułów zgodnych z regexp
            if(re.search(title_pattern,title) is not None and title[0:4] != "<img"):
                # print("Title:", title)
                result[0].append(title)
            if(title[0:4] == "<img"):
                title = "obrazek"
                result[0].append(title)
                # print("obrazek - tytuł do pobrania")


for i, title in enumerate(result[0]):
    if i > 0:
        print(title)
        print(result[1][i])