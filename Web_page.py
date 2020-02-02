from bs4 import BeautifulSoup                        #bs4 is the library to be imported
import requests
import pandas as pd

#Enter the URL you want to Scrap from tthe Website 

URL = "https://en.wikipedia.org/wiki/List_of_largest_universities_and_university_networks_by_enrollment"    
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

#we need to decide which table you want to download and select the table name by using INSPECT option.

table = soup.find('table', {'class' : "wikitable sortable"}).tbody

#Create ROWS and COLUMNS

rows = table.find_all("tr")
columns = [v.text.replace("\n" , "") for v in table.find_all("th")]

#Create a DATA FRAME and write a loop to read the rows accordingly then convert and append into the dataframe and then save it into CSV fromat.

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
