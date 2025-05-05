
def get_produtos_message():
    produtos = [
        {
            "imagem_url": "https://furiagg.fbitsstatic.net/img/p/moletom-manga-dupla-my-hero-academia-x-furia-verde-150220/337185-1.jpg?w=1280&h=1280&v=no-value",
            "url_produto": "https://www.furia.gg/produtos/collabs/my-hero-academia",
            "text": " Gosta de anime? Então você vai amar essa collab! \n\n 🔥 FURIA x My Hero Academia!"
        },
        {
            "imagem_url": "https://furiagg.fbitsstatic.net/img/p/camiseta-oversized-furia-x-zor-verde-estonada-150242/337333-1.jpg?w=1280&h=1280&v=no-value",
            "url_produto": "https://www.furia.gg/produtos/collabs/zor",
            "text": "🟢 Collab FURIA x ZOR!"
        },
        {
            "imagem_url": "https://furiagg.fbitsstatic.net/img/p/camiseta-furia-future-is-black-preta-150146/336680-1.jpg?w=1280&h=1280&v=no-value",
            "url_produto": "https://www.furia.gg/produtos/colecoes/future-is-black",
            "text": "Pelo compromisso com a igualdade racial, a FURIA cria um caminho de inclusao e respeito, promovendo a representatividade e a diversidade! ✊🏾🐾\n\n 🖤 FURIA Future is Black!"
        }
    ]

    lista_produtos = []
    for produto in produtos:
        legenda = f"{produto['text']}\n👉 [Clique aqui para conferir]({produto['url_produto']})"
        lista_produtos.append((produto['imagem_url'], legenda))

    return lista_produtos
