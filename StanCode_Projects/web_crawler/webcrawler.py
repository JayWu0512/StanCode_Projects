"""
File: webcrawler.py
Name: jay wu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        rows = soup.find_all('tbody')
        # find all the rows under tbody

        male_total = 0
        female_total = 0
        # set the initial total is 0

        for row in rows:
            data = row.text.split()
            # turn HTML into text and split it

            for i in range((len(data) - 2)//5 - 4):
                # the first number starts from the second number, and plus 5 will be the next
                # ex. 1, Jacob, ""273,945"", Emily, 223,723, 2, Michael, ""250,633"", Madison, 193,181...
                # the last four is not digit, so minus 4.
                male_total += int(data[2 + i * 5].replace(',', ''))
                # the 2, 7, 12, 17...will be male number

            for i in range((len(data) - 2)//5 - 4):
                female_total += int(data[4 + i * 5].replace(',', ''))
                # the 4, 9, 14, 19...will be female number

        print('Male Number:', male_total)
        print('Female Number:', female_total)


if __name__ == '__main__':
    main()
