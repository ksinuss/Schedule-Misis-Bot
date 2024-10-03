from config import system_data, queueLessons, queueEnglish
import pandas as pd
from datetime import datetime
from getRowData import getLinkSchedule, getLinkEnglishSchedule
from requests import get        
def getSpecifiedLessonInfo(filePath: str, nameSheet: str, 
                  nameGroup: str, numSubgroup: int,
                  numDay: int, numWeek: int, numLesson: int):
    schedule = pd.read_excel(filePath, sheet_name = nameSheet, header=None, skiprows=0)
    columnIndex = schedule.columns[schedule.isin([nameGroup]).any()]
    columnIndex = int(columnIndex.values[0])
    lessonInfo = schedule.iloc[2 + numDay * 14 + numWeek + (numLesson - 1) * 2, 
                               columnIndex + (numSubgroup - 1) * 2:columnIndex + 2 + (numSubgroup - 1) * 2]
    try:
        nameLesson, nameTeacher, numAudience = None, None, None
        if "Иностранный язык" in lessonInfo.values[0]:
            filePath = getLinkEnglishSchedule(headersSheet = queueEnglish["lessonSchedule"])
            print(filePath)
            nameLesson = getEnglishLessonInfo(filePath,
                                 (queueEnglish["studentSurname"], queueEnglish["studentName"], queueEnglish["studentMiddlename"]),
                                 queueEnglish["nameGroup"],
                                 queueEnglish["searchHeaders"])
        else:
            nameLesson, nameTeacher = lessonInfo.values[0].split('\n')
            numAudience = lessonInfo.values[1]
        return {
            "nameLesson": nameLesson,
            "nameTeacher": nameTeacher,
            "numAudience": numAudience
        }
    except TypeError:
        return "Пары нет."
    
def getEnglishLessonInfo(filePath: str, fullName: tuple, nameGroup: str, searchHeaders: tuple, nameSheet = 0):
    # response = get(filePath)
    # df = pd.read_excel(response.content, engine='openpyxl')
    schedule = pd.read_csv(filePath,skiprows = 1)
    # print(df)
    # schedule = pd.read_excel(filePath, sheet_name = nameSheet, skiprows = 1) # make 3 row with headers - with non-zero tables of contents
    resultCells = None
    for indRow in range(len(schedule)):
        studentInfo = schedule.loc[[indRow]]
        studentName = studentInfo['ФИО'].values[0]
        studentGroup = studentInfo['Академ группа'].values[0]
        try:
            if all(name in studentName for name in fullName) and nameGroup == studentGroup:
                indRow = studentInfo.index.values[0]
                numInGroup = int(studentInfo.values[0][0])
                resultCells = (indRow, numInGroup)
                # print(resultCells)
        except TypeError:
            continue
    try:
        groupInfo = schedule.loc[[resultCells[0] - resultCells[1]]]
        resultInfo = {}
        for header in searchHeaders:
            resultInfo[header] = groupInfo[header].values[0].replace('\n', '')
        return resultInfo
    except TypeError:
        return "Студент не найден в указанных списках."

def infoProcessing(numDay):
    # numDay = datetime.today().weekday() - 6
    filePath = getLinkSchedule(queueLessons["nameFile"])["url"]
    numWeek = queueLessons["numWeek"]
    for numLesson in range(system_data["countLessons"]):
        dayInfo = getSpecifiedLessonInfo(filePath=filePath, nameSheet=queueLessons["nameSheet"],
                                         nameGroup=queueLessons["nameGroup"], numSubgroup=queueLessons["numSubgroup"],
                                         numDay=numDay, numWeek=numWeek, numLesson=numLesson + 1)
        print(numLesson + 1, '\n', dayInfo)
        print()

def getDaySchedule(numDay = datetime.today().weekday() - 6):
    infoProcessing(numDay)

getDaySchedule(0)
