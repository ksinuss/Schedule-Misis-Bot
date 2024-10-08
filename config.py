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
users_data = {}

accordTranscript = {}
listAbbrevWeekDays = ["Пн", "Вт", "Ср", "Чт", "Пт"]
listFullWeekDays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
for nE in range(len(listAbbrevWeekDays)):
    accordTranscript[listAbbrevWeekDays[nE]] = {
        "fullWord": listFullWeekDays[nE],
        "numEquivalent": nE
    }
listAbbrevParityWeek = ["В", "Н"]
listFullParityWeek = ["Верхняя", "Нижняя"]
for nE in range(len(listAbbrevParityWeek)):
    accordTranscript[listAbbrevParityWeek[nE]] = {
        "fullWord": listFullParityWeek[nE],
        "numEquivalent": nE
    }

queueLessons = {
        "nameFile": "Институт компьютерных наук",
        "nameSheet": "1 курс",
        "nameGroup": "БИВТ-24-17",
        "numSubgroup": 1,
        "numDay": 2,
        "numWeek": 1,
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
    "lessonSchedule": ("ИКН", "4 пара", "ПН", "СР"),
    "studentSurname": "Костионова",
    "studentName": "Ксения",
    "studentMiddlename": " ",
    "nameGroup": "БИВТ-24-17",
    "searchHeaders": ("Языковая группа", "Модуль", "Преподаватель", "Аудитории")
}

allLessonsUrl = "https://misis.ru/students/schedule/"

spreadsheetIdEnglish = [
    "10_ivi43URnuQ3WdRR-47jgc4HSko3zRi2-_wBQ5KC_4",
    "1d7d4l-fT2nku8cfloqyMlzw0r_i0j0rnN-zEeKYwF78"
]
# FirstCourseSpreadsheetIdEnglish = "10_ivi43URnuQ3WdRR-47jgc4HSko3zRi2-_wBQ5KC_4"
# SecondCourseSpreadsheetIdEnglish = "1d7d4l-fT2nku8cfloqyMlzw0r_i0j0rnN-zEeKYwF78"
# exportFormatEnglish = "xlsx"
# lessonEnglishUrl = f'https://docs.google.com/spreadsheets/d/{spreadsheetIdEnglish}/export?format={exportFormatEnglish}&id={spreadsheetIdEnglish}&gid={sheetIdEnglish}' # for downloading sheet
allLessonsEnglishUrl = 'https://docs.google.com/spreadsheets/d/{spreadsheetIdEnglish}' # for .format with passing arguments
# lessonEnglishUrl = 'https://docs.google.com/spreadsheets/d/{spreadsheetIdEnglish}/edit?gid={sheetIdEnglish}#gid={sheetIdEnglish}' # for .format with passing arguments
# lessonEnglishUrl = 'https://docs.google.com/spreadsheets/d/{spreadsheetIdEnglish}/gviz/tq?tqx=out:xlsx&sheet={sheetIdEnglish}' # for .format with passing arguments
lessonEnglishUrl = 'https://docs.google.com/spreadsheets/d/{spreadsheetIdEnglish}/export?format=csv&id={spreadsheetIdEnglish}&gid={sheetIdEnglish}'

# print(lessonEnglishUrl)
