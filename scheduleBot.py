
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
import telebot
import getRowData
import workingData
from creds import get_bot_token
from config import LOGS, text_help
from telebot.types import ReplyKeyboardMarkup

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

@bot.message_handler(commands=['stt'])
def stt_handler(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Отправь голосовое сообщение, чтобы я его распознал!')
    bot.register_next_step_handler(message, stt)

# Переводим голосовое сообщение в текст после команды stt
def stt(message):
    user_id = message.from_user.id
    # Проверка, что сообщение действительно голосовое
    if not message.voice:
        bot.send_message(user_id, 'Отправь голосовое сообщение')
        return
    status, text = speech_to_text(file) # преобразовываем голосовое сообщение в текст
    # Если статус True - отправляем текст сообщения и сохраняем в БД, иначе - сообщение об ошибке
    if status:
        # Записываем сообщение и кол-во аудиоблоков в БД
        add_message(user_id=user_id, full_message=[text, 'user', 0, 0, stt_blocks])
        bot.send_message(user_id, text, reply_to_message_id=message.id, reply_markup=make_keyboard(['/stt', '/tts', '/debug', '/help', '/about']))
    else:
        bot.send_message(user_id, text, reply_markup=make_keyboard(['/stt', '/tts', '/debug', '/help', '/about']))

@bot.message_handler(commands=['tts'])
def tts_handler(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Отправь следующим сообщением текст, чтобы я его озвучил!')
    bot.register_next_step_handler(message, tts)

def tts(message):
    user_id = message.from_user.id
    text = message.text
    # Проверка, что сообщение действительно текстовое
    if message.content_type != 'text':
        bot.send_message(user_id, 'Отправь текстовое сообщение')
        return
    # Если статус True - отправляем голосовое сообщение, иначе - сообщение об ошибке
    if status:
        bot.send_voice(user_id, content, reply_to_message_id=message.id)
    else:
        bot.send_message(user_id, content, reply_markup=make_keyboard(['/stt', '/tts', '/debug', '/help', '/about']))

@bot.message_handler(commands=['start'])
def start(message):
    pass

def choice_day(message):
    bot.send_message(message.chat.id,
                     text='Выберите день недели (Пн - понедельник, Вт - вторник, Ср - среда, Чт - четверг, Пт - пятница, Сб - суббота)'
                      ' и четность недели (В - вехняя, Н - нижняя)',
                     reply_markup=make_keyboard(['Пн_В', 'Вт_В', 'Ср_В', 'Чт_В', 'Пт_В', 'Сб_В',
                                                 'Пн_Н', 'Вт_Н', 'Ср_Н', 'Чт_Н', 'Пт_Н', 'Сб_Н']))

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        user_id = message.from_user.id
        text = message.text
        # отправляем запрос к GPT
        status_gpt, answer_gpt, tokens_in_answer = ask_gpt(last_messages)
        # обрабатываем ответ от GPT
        if not status_gpt:
            # если что-то пошло не так — уведомляем пользователя и прекращаем выполнение функции
            bot.send_message(user_id, answer_gpt)
            return
        # сумма всех потраченных токенов + токены в ответе GPT
        total_gpt_tokens += tokens_in_answer
        # добавляем ответ GPT и потраченные токены в базу данных
        full_gpt_message = [answer_gpt, 'assistant', total_gpt_tokens, 0, 0]
        add_message(user_id=user_id, full_message=full_gpt_message)
        bot.send_message(user_id, answer_gpt, reply_to_message_id=message.id)  # отвечаем пользователю текстом
    except:
        bot.send_message(user_id, "Нет результатов.", reply_markup=make_keyboard(['/help']))

bot.polling()
