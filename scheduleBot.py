
# links = getRowData.getLessonsSchedule()
# print(links)

# lastUpdate = getData.getTimeUpdate()
# print(lastUpdate)

# getData.getEnglishSchedule()

# workingData.getEnglishLessonInfo("Расписание кабинетов - Английский язык.xlsx",
#                                    (queueEnglish["studentSurname"],
#                                     queueEnglish["studentName"]),
#                                     queueEnglish["nameGroup"],
#                                     queueEnglish["searchHeaders"])

# lessonInfo = workingData.getSpecifiedLessonInfo(links[5]['url'], 
#                         queueLessons["nameSheet"],
#                         queueLessons["nameGroup"],
#                         queueLessons["numSubgroup"],
#                         queueLessons["numDay"],
#                         queueLessons["numWeek"],
#                         queueLessons["numLesson"])
# print(lessonInfo)


# importing libraries
import json
import telebot
import getRowData
from workingData import getDaySchedule
from creds import get_bot_token
from config import text_help
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

# creating a bot
BOT_TOKEN = get_bot_token()
bot = telebot.TeleBot(BOT_TOKEN)

# creating a keyboard with the transferred buttons
def make_keyboard(buttons):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*buttons)
    return markup

# command handlers:
@bot.message_handler(commands=['help'])
def say_help(message):
    bot.send_message(message.from_user.id, text_help)

@bot.message_handler(commands=['getSchedule'])
def start(message):
    pass

def choice_day(message):
    bot.send_message(message.chat.id,
                     text='Выберите день недели (Пн - понедельник, Вт - вторник, Ср - среда, Чт - четверг, Пт - пятница, Сб - суббота)'
                      ' и четность недели (В - вехняя, Н - нижняя)',
                     reply_markup=make_keyboard(['Пн_В', 'Вт_В', 'Ср_В', 'Чт_В', 'Пт_В', 'Сб_В',
                                                 'Пн_Н', 'Вт_Н', 'Ср_Н', 'Чт_Н', 'Пт_Н', 'Сб_Н']))
    bot.register_next_step_handler(message, get_schedule)

def get_schedule(message):
    timeDayInfo = message.text
    getDaySchedule()

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        user_id = message.from_user.id
        text = message.text
        bot.send_message(user_id, answer_gpt, reply_to_message_id=message.id)  # отвечаем пользователю текстом
    except:
        bot.send_message(user_id, "Нет результатов.", reply_markup=make_keyboard(['/help']))

bot.polling()
