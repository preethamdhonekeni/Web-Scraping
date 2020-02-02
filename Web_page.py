from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://en.wikipedia.org/wiki/List_of_largest_universities_and_university_networks_by_enrollment"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class' : "wikitable sortable"}).tbody
rows = table.find_all("tr")
columns = [v.text.replace("\n" , "") for v in table.find_all("th")]
print(columns)
df = pd.DataFrame(columns = columns)
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')
    values = [tds[0].text.replace("\n", ""),
              tds[1].text.replace("\n", ""),
              tds[2].text.replace("\n", ""),
              tds[3].text.replace("\n", ""),
              tds[4].text.replace("\n", ""),
              tds[5].text.replace("\n", ""),
              tds[6].text.replace("\n", ""),
              tds[7].text.replace("\n", ""),
              tds[8].text.replace("\n", "")]
    df = df.append(pd.Series(values, index = columns), ignore_index = True)
    print(df)
    df.to_csv(r'C:\Users\Lenovo\Desktop\SRV\Web_Scrapping' + '\\Universities_by_area.csv', index = 'false')