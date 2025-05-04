import telebot
from config import CHAVE_API
from utils.elenco import message_elenco
from utils.rating import message_rating
from utils.constants import text_base, text_menu, ORG
from utils.loja import message_loja
from utils.produtos import message_produtos
from utils.quiz import sortear_perguntas, message_quiz
from services.scraping_partidas import ScrapingPartidas

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['start'])
def start(message):
    text = f"Olá! Eu sou o bot {ORG} CS 🐾 Para começar, me informe o que você deseja fazer:"
    text += text_base
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['elenco'])
def elenco_handler(message):
    try:
        text = message_elenco()
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"Erro ao buscar elenco: {str(e)}")


@bot.message_handler(commands=['rating'])
def rating_handler(message):
    try:
        text = message_rating()
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"Erro ao buscar ratings: {str(e)}")

scraper = ScrapingPartidas()

@bot.message_handler(commands=['partidas'])
def partidas_handler(message):
    bot.send_message(message.chat.id, f"🔍 Buscando próxima partida da {ORG}...")
    info_partida = scraper.get_partida()
    bot.send_message(message.chat.id, info_partida, parse_mode='Markdown')
    menu_text = "👇  Aqui estão os comandos que você pode usar:\n"
    menu_text += text_base
    bot.send_message(message.chat.id, menu_text)


@bot.message_handler(commands=['loja'])
def loja_handler(message):
    try:
        imagem_url, legenda = message_loja()
        legenda += "\n" + text_menu
        if imagem_url:
            bot.send_photo(message.chat.id, photo=imagem_url, caption=legenda, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, legenda)
    except Exception as e:
        bot.send_message(message.chat.id, f"Erro ao buscar produto: {str(e)}")


@bot.message_handler(commands=['produtos'])
def produtos_handler(message):
    try:
        lista_produtos = message_produtos()
        for imagem_url, legenda in lista_produtos:
            bot.send_photo(message.chat.id, photo=imagem_url, caption=legenda, parse_mode="Markdown")
        
        menu_text = "👇  Aqui estão os comandos que você pode usar:\n"
        menu_text += text_base
        bot.send_message(message.chat.id, menu_text)
    except Exception as e:
        bot.send_message(message.chat.id, f"Erro ao enviar produtos: {str(e)}")


usuarios_quiz = {}
@bot.message_handler(commands=['quiz'])
def quiz_handler(message):
    user_id = message.from_user.id
    perguntas = sortear_perguntas()

    usuarios_quiz[user_id] = {"perguntas": perguntas, "indice": 0, "acertos": 0}

    primeira_pergunta = perguntas[0]
    texto_pergunta = f"{primeira_pergunta['pergunta']}\n"
    for opcao in primeira_pergunta['opcoes']:
        texto_pergunta += opcao + "\n"

    bot.send_message(message.chat.id, texto_pergunta)

@bot.message_handler(func=lambda message: message.from_user.id in usuarios_quiz)
def handle_resposta_quiz(message):
    message_quiz(bot, message, usuarios_quiz)



def verificar(message):
    return True

@bot.message_handler(func=verificar)
def handle_message(message):
    text = """
😕 Oops! Parece que eu não reconheço este comando.
Tente usar um dos comandos que eu conheço:
"""
    text += text_base
    bot.send_message(message.chat.id, text)
bot.polling()