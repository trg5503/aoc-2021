import requests
import re
from bs4 import BeautifulSoup

page = requests.get('https://adventofcode.com/')
html = BeautifulSoup(page.content, 'html.parser')

calendar = html.find_all(class_=re.compile('calendar-day\d+'), recursive=True)
# for day in calendar:
#     # remove day number from tree
#     day.find(class_='calendar-day').extract()
print('\n'.join([d.find_all(text=True, recursive=False)[0][:-2] for d in calendar]))