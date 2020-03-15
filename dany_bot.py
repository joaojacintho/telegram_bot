# -- coding: utf-8 --

# Importando a lib do Telegram bot 
import telebot
from telebot import types

# Passando a chave do bot pelo arquivo txt
token = open("token.txt", "r")
API_TOKEN = str(token.readline())

# Iniciando o bot com o seu Token
bot = telebot.TeleBot(API_TOKEN)

# Resposta ao comando start no chat bot
@bot.message_handler(commands=['start'])
# Definindo a função para o comando start
def send_welcome(message):
    # Pegando o id do chat, para identificar a conversa
    """
        Isso faz com que mesmo que haja 300 instancias do bot iniciados ele responda cada uma de forma única
    """
    cid = message.chat.id
    # Respondendo ao comando para o cid correto 
    msg = bot.reply_to(
        message, "Olá, este é um bot criado por João lucas. \n Nosso Id é " + str(cid))

    # Enviando outra mensagem
    bot.send_message(cid, "Caso você precise de ajuda, use a função /ajuda")
 
    """
        Diferença entre reply_to > send_message
        O reply_to aguarda ser chamada através de um comando
        O send_message não necessita de uma ação anterior para enviar a mensagem
    """


@bot.message_handler(commands=['ajuda'])
def send_help(message):
    cid = message.chat.id
    msg_help = bot.reply_to(message,
                            "Listando os comandos \n Opção 1: /cadastro \n Opção 2: /categoria \n Opção 3: /contato \n Opção 4: /repo")
    bot.send_message(
        cid, "Caso ainda tenha dificuldades, entre em contato pelo email: contato@mindsystem.com.br")


@bot.message_handler(commands=['categoria']) 
def send_category(message):
    cid = message.chat.id
    # Criando um layout com as opções para o usuario digitar, quando for True o usuario só poderá escolher uma opção
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # Adicionando as opções para o layout
    markup.add('Sapatos', 'Roupas')
    # Respondendo ao comando e passando as opções
    msg_category = bot.reply_to(
        message, "Escolha a categoria que você deseja: ", reply_markup=markup)


@bot.message_handler(commands=['repo'])
def send_repository(message):
    cid = message.chat.id
    msg_repository = bot.reply_to(message,
                                  "Blz, você quer ter acesso ao repo onde está o meu cérebro, vou te mandar a URL, calma que esqueci o link :)")
    bot.send_message(
        cid, "Aqui como prometi, https://github.com/joaojacintho/telegram_bot")


bot.polling()
