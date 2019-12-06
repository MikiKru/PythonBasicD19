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


rows = stooq_html.find_all("tr")
print("Rekordy")
for row in rows:
    if(str(row.find("td", {"id" : "f13"}))
            .replace('<td id="f13" nowrap="">',"").replace("</td>","") is not None):
        print("Data:",str(row.find("td", {"id" : "f13"})).replace('<td id="f13" nowrap="">',"").replace("</td>",""))
    if(len(str(row.a).split(">")) > 1):
        print("Title:", str(row.a).split(">")[1].replace("</a",""))
