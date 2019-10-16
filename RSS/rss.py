import telebot
import requests
from bs4 import BeautifulSoup
import re
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("russian")

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


@bot.message_handler(commands=['donate'])
def donate(message):
    bot.send_message(message.chat.id, "На поддержку проекта")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        global k
        bot.send_message(message.chat.id, "Отправьте мне ссылку на RSS ленту: " + "\n\n" +
                         "Список популярных RSS лент: " + "\n" + "Лента ру - /LentaRu" + "\n" +
                         "СПОРТ сегодня - /SportToday" + "\n" +
                         "Travel ru -  /TravelRu")
        k = 0
    except:
        bot.send_message(message.chat.id, "Возникла ошибка.")


@bot.message_handler(commands=['help'])
def get_help(message):
    try:
        bot.send_message(message.chat.id, "Бот создан для просмотра новостей"
                                          " с помощью специальных RSS лент. Введите /start для начала пользования.")
    except:
        bot.send_message(message.chat.id, "Error")


@bot.message_handler(content_types=['text'])
def start_message(message):
    dict_tape = {"/LentaRu": "http://lenta.ru/l/r/EX/import.rss",
                 "/SportToday": "http://www.sports.ru/sports_docs.xml",
                 "/TravelRu": "http://www.travel.ru/inc/side/yandex.rdf"}
    a = 0
    lst_frequency = []
    count = 0

    global k, url
    try:
        if k == 0:
            if message.text in dict_tape:
                url = dict_tape[message.text]
            else:
                url = message.text
            bot.send_message(message.chat.id, "Сообщите пару ключевых слов: " +
                             "\n\n" +
                             "например: Трамп, Зеленский, сообщил")
            k += 1

        else:
            category = message.text
            resp = requests.get(url)
            soup = BeautifulSoup(resp.content, features='xml')
            items = soup.findAll('item')
            key_words = category
            for item in items:
                count += 1
                for k in key_words.split(","):
                    for i in (" ".join([stemmer.stem(i.lower()) for i in item.title.text.split()]) + " " + " ".join(
                            [stemmer.stem(i.lower()) for i in cleanhtml(item.description.text).split()])).split():
                        if i == stemmer.stem(k):
                            a += 1
                            if item.link.text not in lst_frequency:
                                lst_frequency.append(item.link.text)
                                bot.send_message(message.chat.id,
                                                 item.title.text +
                                                 "\n" +
                                                 cleanhtml(item.description.text) +
                                                 "\n" +
                                                 "Ссылка на новость: " +
                                                 item.link.text)
            if a == 0:
                bot.send_message(message.chat.id, "К сожалению, по данному запросу новости отсутствуют")
            k = 0

            if count == len(items):
                bot.send_message(message.chat.id, "Нажмите /start для нового поиска новостей")
    except:
        bot.send_message(message.chat.id, "Произошла ошибка. Возможно вы ввели неверные данные. "
                                              "Повторите попытку позже.")


bot.polling()
