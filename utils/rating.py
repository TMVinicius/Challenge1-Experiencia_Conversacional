from services.scraping_rating import PlayerRatingFetcher
from utils.constants import text_menu

def get_rating_message():
    fetcher = PlayerRatingFetcher()
    ratings = fetcher.get_player_ratings()

    text = "📊 *Ratings dos jogadores:*\n\n"
       
    for r in ratings:
        text += f"• {r}\n\n"

    text += "📈 O que é rating? \nO rating é uma métrica que avalia o desempenho geral de um jogador com base em estatísticas das partidas, como eliminações, mortes, dano causado e impacto nas rodadas.\n\n"
    text += f"{text_menu}"

    return text
