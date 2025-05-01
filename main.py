import telebot
from config import CHAVE_API
from utils.elenco import mensagem_elenco
from utils.rating import mensagem_rating
from utils.constants import text_base, text_menu

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['start'])
def start(message):
    text = "Olá! Eu sou o bot Furia CS. Para começar, me informe o que você deseja fazer:"
    text += text_base
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['elenco'])
def elenco_handler(message):
    try:
        text = mensagem_elenco()
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"Erro ao buscar elenco: {str(e)}")


@bot.message_handler(commands=['rating'])
def rating_handler(message):
    try:
        text = mensagem_rating()
        bot.send_message(message.chat.id, text, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"Erro ao buscar ratings: {str(e)}")

@bot.message_handler(commands=['partidas'])
def start(message):
    text = "Aqui voce receberá alertas de partidas ao vivo!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['loja'])
def start(message):
    text = "Aqui vai o loja"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['quiz'])
def start(message):
    text = "Aqui vai o quiz"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['menu'])
def start(message):
    text = "Aqui estão os comandos que você pode usar:\n"
    text += text_base
    bot.send_message(message.chat.id, text)



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