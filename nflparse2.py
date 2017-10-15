from bs4 import BeautifulSoup

# Beautiful Soup
soup = BeautifulSoup(text)
film_list = soup.find('div', {'class': 'profileFilmsList'})

