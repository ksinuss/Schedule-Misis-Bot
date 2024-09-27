import requests
from config import users_data, queueEnglish, allLessonsUrl, spreadsheetIdEnglish, allLessonsEnglishUrl, lessonEnglishUrl

def getLessonsResponse(link: str) -> str:
    response = requests.get(link, verify=True)
    response = response.text
    return response

def getLinkSchedule(nameInstitute: str) -> str:
    nameInstitute = nameInstitute.split()
    response = getLessonsResponse(allLessonsUrl)
    response = response[response.rfind("Расписание учебных занятий"):response.rfind("Обновление")]
    listInstLinks = [i for i in range(len(response)) if response.startswith('<a href="/files/', i)]
    for instLink in listInstLinks:
        grabLink = response[instLink:]
        grabLink = grabLink[:grabLink.find('</a></span>')]
        grabNameInst = grabLink[grabLink.find('target="_blank">'):]
        if ''.join(nameInstitute) in ''.join(grabNameInst.split()):
            link = grabLink[grabLink.find('="') + 2:]
            link = link[:link.find('" target=')]
            extFile = link[link.rfind('.'):]
            return {
                "url": "https://misis.ru" + link,
                "extFile": extFile
            }
    return None

def downloadSchedule(links: list):
    for link in links:
        fileResponse = requests.get(link["url"], verify=True)
        filePath = link["nameFile"] + link["extFile"]
        if fileResponse.status_code == 200:
            with open(filePath, 'wb') as file:
                file.write(fileResponse.content)
            print('File downloaded successfully')
        else:
            print('Failed to download file')

def getTimeUpdate() -> str:
    response = getLessonsResponse(allLessonsUrl)
    startTime = response.find('Обновление:') + 12
    time = response[startTime:startTime + 10]
    return time

def getLinkEnglishSchedule(userId: int = 0, headersSheet: tuple = ('.')):
    # try:
    #     numCourse = users_data[userId]["numCourse"]
    # except KeyError:
    #     return "Неверный формат User ID."
    numCourse = 1
    response = getLessonsResponse(allLessonsEnglishUrl.format(spreadsheetIdEnglish = spreadsheetIdEnglish[numCourse - 1]))
    response = response[response.find("topsnapshot"):response.rfind("Europe/Moscow")]
    listSheetsId = [i for i in range(len(response)) if response.startswith('"[', i)]
    # print(response)
    for sheetId in listSheetsId:
        grabId = response[sheetId:]
        grabId = grabId[:grabId.find('"]')]
        # print(grabId)
        if 'null' not in grabId and all(header in grabId for header in headersSheet):
            rightSheetId = grabId[grabId.find('\\"') + 2:]
            rightSheetId = rightSheetId[:rightSheetId.find('\\"')]
            return lessonEnglishUrl.format(spreadsheetIdEnglish = spreadsheetIdEnglish[numCourse - 1],
                                           sheetIdEnglish = rightSheetId)
    return None

# res = getLinkEnglishSchedule(headersSheet = queueEnglish["lessonSchedule"])
# res = getLinkEnglishSchedule()
# print(res)

# import time
# start_time = time.time()

# res = getLinkSchedule("Институт компьютерных наук")
# print(res)

# print("--- %s seconds ---" % (time.time() - start_time))
