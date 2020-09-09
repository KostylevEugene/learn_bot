# Здесь содержится код бота

# Импорт файла для сохранения ошибок
import logging

# Импорт модулей коммуникации с сервером, обработки запросов  и обработчик событий
from telegram.ext import Updater, CommandHandler,  MessageHandler, Filters      

#
import Settings

logging.basicConfig(filename="bot.log", level=logging.INFO)         # filename - туда записываются логи; level - уровень важности сообщения

# использование прокси-серверов для обхода блокировок
PROXY = {'proxy_url': Settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': Settings.PROXY_USERNAME, 'password': Settings.PROXY_PASSWORD}}

def greed_user(update, context):        # update - инфа от сервера; context - управление ботом изнутри (отображение деталей операций)
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")
    
def talk_to_me(update, context):        # обрабатывает полученные сообщения
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():         # содержит основной код 
    # передача ключа на сервер
    mybot = Updater(Settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    # сокращение
    dp = mybot.dispatcher
    
    # добавление обработчика запросов
    dp.add_handler(CommandHandler("start", greed_user))

    # добавление обработчика сообщений
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))       # Filters.text - реагирование только на текст

    logging.info("Бот стартовал")
    # произведение запроса на сервер
    mybot.start_polling()
    # ... пока не скажем остановиться
    mybot.idle()

main()
