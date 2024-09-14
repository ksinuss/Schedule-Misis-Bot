import requests
import config

def getLessonsResponse(link: str) -> str:
    response = requests.get(link, verify=True)
    response = response.text
    return response

def getLinkSchedules(nameInstitute: str) -> dict:
    nameInstitute = nameInstitute.split()
    response = getLessonsResponse(config.allLessonsUrl)
    grabFlag = False
    linkData = ""
    link = None
    for i in range(len(response) - 16):
        grabText = response[i:i + 16]
        if grabText == '<a href="/files/':
            grabFlag = True
        if grabText[:4] == '</a>' and linkData:
            nameFile = linkData[linkData.find('_blank">') + 8:].replace('\xa0', ' ').replace('­', '')
            nameFile = nameFile.split()
            if ' '.join(nameFile) == ' '.join(nameInstitute) or ' '.join(nameFile[1:]) == ' '.join(nameInstitute[1:]):
                validLink = "https://misis.ru" + linkData[9:linkData.find('" target')]
                extFile = validLink[validLink.rfind('.'):]
                link = {
                    "url": validLink,
                    "extFile": extFile
                }
                break
            grabFlag = False
            linkData = ""
        if grabFlag:
            linkData += response[i]
    return link

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
    response = getLessonsResponse(config.allLessonsUrl)
    startTime = response.find('Обновление:') + 12
    time = response[startTime:startTime + 10]
    return time

def getEnglishSchedule():
    linkEnglishSchedule = [{
        "url": config.lessonEnglishUrl,
        "nameFile": "Расписание кабинетов - Английский язык",
        "extFile": ".xlsx"
    }]
    return linkEnglishSchedule


# downloadSchedule(getLessonsSchedule())
link = getLinkSchedules(config.queueLessons['nameFile'])
print(link)
