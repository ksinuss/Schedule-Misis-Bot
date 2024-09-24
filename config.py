HOME_DIR = '/schedule_misis' # path to the project folder
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt' # file for storing bot_token
DATA_PATH = f'{HOME_DIR}/creds/users.json' # file for storing user_data

text_help = """Список доступных команд:
/start - начать/продолжить работу помощника
/help - вывести справочную информацию о боте
/about - вывести немного информации обо мне - давай познакомимся:)

А вот основные пояснения по использованию бота:
- Бот предназначен для того, чтобы выполнять функцию внимательного и дружелюбного ассистента, с которым можно обсуждать важные вопросы хоть каждый день
- После запуска бота вам нужно отправить любое сообщение - текстовое или голосовое
- После начала бот начнет генерировать текст, если вы отправили текстовое сообщение, или аудио - если голосовое, и отправит вам свой ответ
- После этого вам можно отправить следующее сообщение, на которое нужно ответить
- Ваш диалог будет продолжаться до тех пор, пока у вас не закончится количество символов/токенов, выделенных на проект
- После того, как вы закончите, вам будет предложено получить файл с логами, узнать информацию о боте, получить пояснения по использованию бота - выберите вариант, который посчитаете нужным
- Не сдерживайте свое воображение и креативьте по полной!"""

system_data = {
    "lastUpdate": None,
    "numCurWeek": 0,
    "countLessons": 7
}

accordTranscript = {}
listAbbrevWeekDays = ["Пн", "Вт", "Ср"]
listFullWeekDays = ["Понедельник", "Вторник", "Среда"]
for nE in range(len(listAbbrevWeekDays)):
    accordTranscript[listAbbrevWeekDays[nE]] = {
        "fullWord": listFullWeekDays[nE],
        "numEquivalent": nE
    }
listAbbrevParityWeek = ["В"]
listFullParityWeek = ["Верхняя"]
for nE in range(len(listAbbrevParityWeek)):
    accordTranscript[listAbbrevParityWeek[nE]] = {
        "fullWord": listFullParityWeek[nE],
        "numEquivalent": nE
    }

queueLessons = {
        "nameFile": "Институт компьютерных наук.xlsx",
        "nameSheet": "1 курс",
        "nameGroup": "БИВТ-24-17",
        "numSubgroup": 1,
        "numDay": 2,
        "numWeek": 0,
        "numLesson": 5
}
# queueLessons = {
#         "nameFile": "Институт новых материалов",
#         "nameSheet": "2 курс",
#         "nameGroup": "БЭН-23-4-1",
#         "numSubgroup": 1,
#         "numDay": 4,
#         "numWeek": 1,
#         "numLesson": 2
# }
queueEnglish = {
    "lessonSchedule": "ИКН_4 пара ПН-СР",
    "studentSurname": "Костионова",
    "studentName": "Ксения",
    "studentMiddlename": " ",
    "nameGroup": "БИВТ-24-17",
    "searchHeaders": ("Языковая группа", "Модуль", "Преподаватель", "Аудитории")
}


allLessonsUrl = "https://misis.ru/students/schedule/"

IKNspreadsheetIdEnglish = "10_ivi43URnuQ3WdRR-47jgc4HSko3zRi2-_wBQ5KC_4"
INMspreadsheetIdEnglish = "1d7d4l-fT2nku8cfloqyMlzw0r_i0j0rnN-zEeKYwF78"
IKNsheetIdEnglish = "1839462526"
INMsheetIdEnglish = "1839462526"
exportFormatEnglish = "xlsx"
spreadsheetIdEnglish = INMspreadsheetIdEnglish
sheetIdEnglish = INMsheetIdEnglish
lessonEnglishUrl = f'https://docs.google.com/spreadsheets/d/{spreadsheetIdEnglish}/export?format={exportFormatEnglish}&id={spreadsheetIdEnglish}&gid={sheetIdEnglish}'
# print(lessonEnglishUrl)