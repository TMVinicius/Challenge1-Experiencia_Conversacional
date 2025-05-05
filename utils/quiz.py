import random
from utils.constants import text_base

perguntas_possiveis = [
    {
        "pergunta": "🐾 Qual ano a FURIA foi fundada?",
        "opcoes": ["A) 2015", "B) 2017", "C) 2018", "D) 2019"],
        "resposta_correta": "B"
    },
    {
        "pergunta": "🎯 Qual jogador da FURIA é conhecido como 'KSCERATO'?",
        "opcoes": ["A) Yuri", "B) Kaike", "C) Andrei", "D) Rafael"],
        "resposta_correta": "B"
    },
    {
        "pergunta": "🏆 Qual foi a melhor colocação da FURIA em um Major CS:GO?",
        "opcoes": ["A) Semifinal", "B) Quartas de final", "C) Fase de grupos", "D) Final"],
        "resposta_correta": "A"
    },
    {
        "pergunta": "🔥 Qual coach já comandou a FURIA no CS?",
        "opcoes": ["A) Guerri", "B) Dead", "C) Peacemaker", "D) Zews"],
        "resposta_correta": "A"
    },
    {
        "pergunta": "🎮 Quem foi o primeiro AWPer da FURIA?",
        "opcoes": ["A) HEN1", "B) Saffee", "C) Fallen", "D) Art"],
        "resposta_correta": "A"
    }
]


def get_random_questions():
    return random.sample(perguntas_possiveis, 3)


def handle_quiz_message(bot, message, usuarios_quiz):
    user_id = message.from_user.id
    quiz_data = usuarios_quiz[user_id]
    indice = quiz_data['indice']
    pergunta_atual = quiz_data['perguntas'][indice]

    resposta_usuario = message.text.strip().upper()

    if resposta_usuario == pergunta_atual['resposta_correta']:
        bot.send_message(message.chat.id, "✅ Resposta correta!")
        quiz_data['acertos'] += 1
    else:
        bot.send_message(
            message.chat.id,
            f"❌ Resposta errada! A resposta certa era: {pergunta_atual['resposta_correta']}"
        )

    quiz_data['indice'] += 1
    if quiz_data['indice'] < len(quiz_data['perguntas']):
        proxima_pergunta = quiz_data['perguntas'][quiz_data['indice']]
        texto_pergunta = f"{proxima_pergunta['pergunta']}\n"
        for opcao in proxima_pergunta['opcoes']:
            texto_pergunta += opcao + "\n"

        bot.send_message(message.chat.id, texto_pergunta)
    else:
        total = quiz_data['acertos']
        bot.send_message(
            message.chat.id,
            f"🎉 Quiz finalizado! Você acertou {total}/{len(quiz_data['perguntas'])} perguntas."
        )
        del usuarios_quiz[user_id]

        menu_text = "👇 Aqui estão os comandos que você pode usar:\n" + text_base
        bot.send_message(message.chat.id, menu_text)
