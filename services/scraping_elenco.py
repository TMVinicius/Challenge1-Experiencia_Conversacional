import requests
from bs4 import BeautifulSoup
from utils.constants import URL_elenco

class FuriaScraper:
    def __init__(self):
        self.players = []
        self.coach = []

    def fetch_data(self):
        response = requests.get(URL_elenco)
        if response.status_code != 200:
            raise Exception(f"Erro ao acessar a página: {response.status_code}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.find_all('div', class_='PlayerCardList__PlayerCardListContainer-sc-cuylet-0 kuAkeK')

        self.players.clear()
        self.coach.clear()

        for i in range(0, len(divs)):     
            for jogadores in divs[i]:
                if len(divs) == 2:
                    if i == 0:
                        self.players.append(jogadores.get_text(strip=True))
                    else:
                        break
                else:
                    if i == 0 or i == 1:
                        self.players.append(jogadores.get_text(strip=True))
                    else:
                        break

        for coach_center in soup.find_all('div', class_='sc-dkPtRN id__MenuCol-sc-1x9brse-1 UsnfG elezoS'):
            for treinador in coach_center.find_all('div', class_='PlayerCard__PlayerNickName-sc-1u0zx4y-4 iJDKZA'):
                self.coach.append(treinador.get_text(strip=True))

    def get_players(self):
        if not self.players:
            self.fetch_data()
        return self.players

    def get_coach(self):
        if not self.coach:
            self.fetch_data()
        return self.coach
