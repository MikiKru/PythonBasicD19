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
title_pattern = re.compile()

rows = stooq_html.find_all("tr")
print("Rekordy")
for index, row in enumerate(rows):
    # filtrowanie daty
    date = str(row.find("td", {"id": "f13"})).replace('<td id="f13" nowrap="">', "").replace("</td>", "")
    # szukanie tylko dat zgodnych z regexp
    # if(re.search(date_pattern, date) is not None):
    #     print("Data:", date)
    if(len(str(row.a).split(">")) > 1):
        print("Title:", str(row.a).split(">")[1].replace("</a",""))
