from services.scraping_rating import PlayerRatingFetcher
from utils.constants import text_menu

def mensagem_rating():
    fetcher = PlayerRatingFetcher()
    ratings = fetcher.get_player_ratings()

    text = "📊 *Ratings dos jogadores:*\n\n"
    for r in ratings:
        text += f"• {r}\n\n"

    text += f"{text_menu}"
    return text
