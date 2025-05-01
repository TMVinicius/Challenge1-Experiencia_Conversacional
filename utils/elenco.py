from services.scraping_elenco import FuriaScraper
from utils.constants import text_menu

def mensagem_elenco():
    scraper = FuriaScraper()
    players = scraper.get_players()
    coach = scraper.get_coach()

    text = "👥 *Elenco:*\n\n *⭐Titulares:*\n"
    
    for i, p in enumerate(players):
        if i == 5:
            text += "\n📋 *Reservas:*\n"
        text += f"• {p}\n"

    if len(coach) == 1:
        text += f"\n🎯 *Coach:* {coach[0]}"
    elif len(coach) > 1:
        text += f"\n🎯 *Coaches:* {', '.join(coach)}"
    else:
        text += "\n🎯 *Coach:* Não encontrado"

    text += f"\n\n{text_menu}"
    return text
