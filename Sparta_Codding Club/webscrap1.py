import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# Start coding

# Using select
movies = soup.select('.lister > table > tbody > tr')

soup.select_one('tag_name[attribute="value"]')
# Looping through the movies
for movie in movies:
    # First, let's get the title of the movie
    movie_title = movie.select_one('.titleColumn > a').text
print(movie_title)

        # How to use selector (copy selector)
soup.select('tag name')
soup.select('.class name')
soup.select('#ID name')

soup.select('upper tag name> sub tag name> sub tag name')
soup.select('higher tag name.class name> subtag name.class name')

# How to find by tag and attribute value
soup.select('tag name[attribute="value"]')

# If you only want to bring one
soup.select_one('same as above')



import requests
from bs4 import BeautifulSoup

# Read the URL and get the HTML,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# You will be scraping the data from this page
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Use the requests library to get the HTML code at the url above
data = requests.get(url=url, headers=headers)

# The BeautifulSoup library makes it easy to
# parse HTML code
soup = BeautifulSoup(data.text, 'html.parser')

