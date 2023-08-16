import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://farid.one/kaggle-solutions/'
response = requests.get(url)
response = response.text


soup = BeautifulSoup(response, 'html.parser')

links = []
for li_tag in soup.find_all('li', class_='secondary'):
    try:
        link = li_tag.find('a')['href']
        if 'discussion' in link:
            place = li_tag.find('img').next_sibling.strip().split(' ')[0]
            competition_name = li_tag.find_previous('b').text.split('. ')[-1].strip()

            # Find the competition details element
            details_element = li_tag.find_previous('td', class_='td-details')

            # Find the prize element within the competition details
            prize_element = details_element.find('p', string=lambda s: s and 'prize' in s.lower())
            prize = prize_element.text.split(':')[-1].strip() if prize_element else ''

            # Find the team element within the competition details
            team_element = details_element.find('p', string=lambda s: s and 'team' in s.lower())
            team = team_element.text.split(':')[-1].strip() if team_element else ''

            # Find the kind element within the competition details
            kind_element = details_element.find('p', string=lambda s: s and 'kind' in s.lower())
            kind = kind_element.text.split(':')[-1].strip() if kind_element else ''
            # Find the metric element within the competition details
            metric_element = details_element.find('p', string=lambda s: s and 'metric' in s.lower())
            metric = metric_element.text.split(':')[-1].strip() if metric_element else ''

            # Find the year element within the competition details
            year_element = details_element.find('p', string=lambda s: s and 'year' in s.lower())
            year = year_element.text.split(':')[-1].strip() if year_element else ''

            info_tuple = (link, int(place[:-2]), competition_name, prize, team, kind, metric, year)
            links.append(info_tuple)
    except:
        pass




scraped =pd.DataFrame(data = links, columns= ['link', 'place', 'competition_name', 'prize', 'team', 'kind', 'metric', 'year'])
scraped.to_csv('kagglesolns.csv', header=None)