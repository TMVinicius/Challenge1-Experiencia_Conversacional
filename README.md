# 🎯 Desafio Técnico - FURIA Tech

**Desafio Técnico - FURIA Tech** este projeto foi desenvolvido como parte de um desafio voltado à criação de experiências conversacionais para fãs da FURIA, com foco no Telegram. 🚀 A proposta é simples, mas poderosa: construir um bot que concentre tudo o que um fã da equipe de CS da FURIA gostaria de ver e interagir em tempo real.

## Utilize o bot!

[Link do Bot no Telegram](https://t.me/desafio_furiacs_bot)

<p align="center">
  <img src="assets/qrcode.png" width="150" alt="QR Code Bot Telegram"/>
</p>

## 🔍 Como foi feita a Coleta de Dados?

- **Web Scraping** 🕷️
  - A coleta de todos os dados pra o bot da FURIA foram realizada através de web scraping com Beautiful Soup e Selenium.
  - Foi utilizada a página do campeonato na [Draft5](https://draft5.gg/) para obter dados do elenco e partidas futuras do time, o site [Profilerr](https://profilerr.net/pt/) também foi utilizado para estatísticas de cada jogador.
  - Foi utilizada também a loja da [FURIA](https://www.furia.gg/) para integração da funcionalidade /loja do bot.
  - O projeto foi desenvolvido de maneira que fazendo apenas algumas alterações seja possível pegar os dados de qualquer equipe! ⚙️

## 📂 Estrutura do Projeto

- **`/main.py`**: Arquivo principal que inicializa o bot Telegram e define os comandos disponíveis.
- **`/config.py`**: Contém a chave da API do Telegram.
- **`/services`**:
  - **`/scraping_elenco.py`**: Script responsável por coletar o elenco.
  - **`/scraping_partidas.py`**: Script responsável por coletar as informações das próximas partidas.
  - **`/scraping_rating.py`**: Script responsável por coletar os ratings dos jogadores.
- **`/utils`**:
  - **`/constants.py`**: Contém as mensagens padrão e constantes utilizadas no bot.
  - **`/elenco.py`**: Função utilitária para retornar a lista de jogadores do elenco.
  - **`/loja.py`**: Retorna os produtos e imagens da loja.
  - **`/produtos.py`**: Lista os produtos disponíveis na loja.
  - **`/quiz.py`**:  Gerencia o quiz interativo com perguntas e respostas.
  - **`/rating.py`**: Lógica para montar a mensagem com os ratings coletados. 

## 🛠️ Requisitos

- Python (versão 3.8 ou superior) 🐍
- Dependências listadas em **pyproject.toml** 📜

### 📥 Instalação

1. Clone o repositório:

   ```
   git clone https://github.com/TMVinicius/challenge-experiencia-conversacional-furia
   cd challenge-experiencia-conversacional-furia
   ```


2. Instale as dependências:

   ```
   pip install .
   ```


3. Rode o projeto:

   ```
   python main.py
   ```


## 📧 Contato

Para qualquer dúvida ou feedback, entre em contato comigo por [viniciustavaresbr@gmail.com](mailto:viniciustavaresbr@gmail.com).
