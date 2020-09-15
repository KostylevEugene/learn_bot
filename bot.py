# Здесь содержится код бота

# Импорт файла для сохранения ошибок
import logging

# ephem выполняет высокоточные астрологические вычисления
import ephem

# Импорт модулей коммуникации с сервером, обработки запросов  и обработчик событий
from telegram.ext import Updater, CommandHandler,  MessageHandler, Filters      

#
import Settings

logging.basicConfig(filename="bot.log", level=logging.INFO)         # filename - туда записываются логи; level - уровень важности сообщения

# использование прокси-серверов для обхода блокировок
PROXY = {'proxy_url': Settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': Settings.PROXY_USERNAME, 'password': Settings.PROXY_PASSWORD}}

# Данная функция приветствует пользователя при подключении к боту
def greed_user(update, context):        # update - инфа от сервера; context - управление ботом изнутри (отображение деталей операций)
    print("Вызван /start")          # это сообщение появится в консоли
    update.message.reply_text("Здравствуй, пользователь!")          # это сообщение придет пользователю


def planet_place(update, context):
    text = update.message.text.split(' ')
    print(text[1])
    if text[1] == 'Mars':
        planet = ephem.Mars('2020/09/13')
        p = ephem.constellation(planet)
        print(p)
        update.message.reply_text(p)
    
    if text[1] == 'Uranus':
        planet = ephem.Uranus('2020/09/13')
        p = ephem.constellation(planet)
        print(p)
        update.message.reply_text(p)
    
    if text[1] == 'Mercury':
        planet = ephem.Mercury('2020/09/13')
        p = ephem.constellation(planet)
        print(p)
        update.message.reply_text(p)
    
    if text[1] == 'Venus':
        planet = ephem.Venus('2020/09/13')
        p = ephem.constellation(planet)
        print(p)
        update.message.reply_text(p)

    if text[1] == 'Jupiter':
        planet = ephem.Jupiter('2020/09/13')
        p = ephem.constellation(planet)
        print(p)
        update.message.reply_text(p)

    if text[1] == 'Saturn':
        planet = ephem.Saturn('2020/09/13')
        p = ephem.constellation(planet)
        print(p)
        update.message.reply_text(p)

    if text[1] == 'Neptune':
        planet = ephem.Neptune('2020/09/13')
        p = ephem.constellation(planet)
        print(p)
        update.message.reply_text(p)

        
def talk_to_me(update, context):        # обрабатывает полученные сообщения
    text = update.message.text          # полученный текст 
    print(text)                   # сообщение в консоли
    update.message.reply_text(text)                 # текст отправленный пользователю

def main():         # содержит основной код 
    # передача ключа на сервер
    mybot = Updater(Settings.API_KEY, use_context=True, request_kwargs=PROXY)
    
    # сокращение
    dp = mybot.dispatcher
    
    # добавление обработчика запросов для подключения бота
    dp.add_handler(CommandHandler("start", greed_user))

    dp.add_handler(CommandHandler("planet", planet_place))

    # добавление обработчика "эхо-сообщений"
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))       # Filters.text - реагирование только на текст

    logging.info("Бот стартовал")
    
    # произведение запроса на сервер
    mybot.start_polling()
    
    # ... пока не скажем остановиться
    mybot.idle()

#if _name_ == "_main_":
main()
