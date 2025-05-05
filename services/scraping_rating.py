import requests
from bs4 import BeautifulSoup
import re
from services.scraping_elenco import FuriaScraper
from utils.constants import URL_rating

class PlayerRatingFetcher:
    def __init__(self):
        self.scraper = FuriaScraper()

    def get_player_ratings(self):
        players = self.scraper.get_players()
        ratings = []

        for player in players:
            url = f"{URL_rating}{player}/"
            try:
                response = requests.get(url)
                if response.status_code != 200:
                    ratings.append(f"{player} - Rating indisponível")
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')
                divs = soup.find_all('li', class_='_option_fjnm5_89')

                if not divs:
                    ratings.append(f"{player} - Rating não encontrado")
                    continue

                text = divs[0].get_text(strip=True)
                match = re.match(r"([0-9.]+)([A-Za-z]+)", text)

                if match:
                    numero, texto = match.groups()
                    ratings.append(f"{player} - {numero}")
                else:
                    ratings.append(f"{player} - N/A")
            except Exception as e:
                ratings.append(f"{player} - Erro ao obter rating")

        return ratings
