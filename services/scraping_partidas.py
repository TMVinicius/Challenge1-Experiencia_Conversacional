from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import utils.constants as URL_elenco
import re
import time
import locale
import requests

class ScrapingPartidas:
    def __init__(self):
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        self.options = Options()
        self.options.add_argument("--headless")

    def get_partida(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

        URL_elenco = "https://draft5.gg/equipe/330-FURIA"
        driver.get(URL_elenco)
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        date_elements = soup.find_all("p", class_="MatchList__MatchListDate-sc-1pio0qc-0 kPJtEq")[:1]
        match_elements = soup.find_all("div", class_="MatchCardSimple__MatchTeams-sc-wcmxha-9 gXhBRJ")[:1]
        link_element = soup.find("div", class_="id__ContentContainer-sc-1x9brse-2 hlMjcl")
        link = link_element.find('a', href=lambda s: s and s.startswith("/partida/")) if link_element else None

        dates = []
        matches = []

        for date_elem in date_elements:
            date_text = date_elem.text.strip().replace("📅", "").strip()

            if "," in date_text:
                _, date_part = date_text.split(",", 1)
            else:
                date_part = date_text

            try:
                date_parsed = datetime.strptime(date_part.strip(), "%d de %B de %Y")
                date_parsed = date_parsed.replace(hour=23, minute=59, second=59)
            except Exception as e:
                date_parsed = date_part.strip()

            dates.append(date_parsed)

        for elem in match_elements:
            teams = elem.find_all("span")
            if len(teams) == 2:
                team1 = teams[0].text.strip()
                team2 = teams[1].text.strip()
                matches.append((team1, team2))

        driver.quit()

       
        if not dates or not matches or dates[0] < datetime.now():
            return "❌ Não há partidas nos próximos dias."

        if link:
            match_url = "https://draft5.gg" + link["href"]
        else:
            return "❌ Não foi possível encontrar o link da partida."

        response = requests.get(match_url)

        if response.status_code != 200:
            return f"❌ Erro ao acessar a página da partida: {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find_all('span', class_='MatchJumbotron__MatchJumbotronInfo-sc-180fxwd-1 hfINSo')

        if len(title) < 2:
            return "❌ Não foi possível extrair informações da partida."

        dt_hr_melhorde = title[0].get_text(strip=True)
        melhorde = title[0].get_text(strip=True).split('-')[0].strip()
        melhor_de = re.sub(r'de(\d+)', r'de \1', melhorde)
        horario = re.search(r'\d{2}:\d{2}', dt_hr_melhorde)
        data_formatada = dates[0].strftime("%d/%m/%Y")

        texto = f"🎮 Confronto: {melhor_de} - {matches[0][0]} vs {matches[0][1]}\n"
        texto += f"🏆 Campeonato: {title[1].get_text(strip=True)}\n"
        texto += f"📅 Data: {data_formatada} - {horario.group(0) if horario else 'horário indefinido'}\n"
        texto += f"👉 [Clique aqui para a transmissão]({match_url})"

        return texto
