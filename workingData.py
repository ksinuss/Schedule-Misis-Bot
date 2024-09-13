import pandas as pd
            
def getSpecifiedLessonInfo(filePath: str, nameSheet: str, 
                  nameGroup: str, numSubgroup: int,
                  numDay: int, numWeek: int, numLesson: int):
    schedule = pd.read_excel(filePath, sheet_name = nameSheet, header=None, skiprows=0)
    columnIndex = schedule.columns[schedule.isin([nameGroup]).any()]
    columnIndex = int(columnIndex.values[0])
    lessonInfo = schedule.iloc[2 + (numDay - 1) * 14 + numWeek + (numLesson - 1) * 2, 
                               columnIndex + (numSubgroup - 1) * 2:columnIndex + 2 + (numSubgroup - 1) * 2]
    try:
        nameLesson, nameTeacher = lessonInfo.values[0].split('\n')
        numAudience = lessonInfo.values[1]
        return {
            "nameLesson": nameLesson,
            "nameTeacher": nameTeacher,
            "numAudience": numAudience
        }
    except AttributeError:
        return "Пары нет."
    
def getEnglishLessonInfo(filePath: str, fullName: tuple, nameGroup: str, searchHeaders: tuple, nameSheet = 0):
    schedule = pd.read_excel(filePath, sheet_name = nameSheet, skiprows = 1) # make 3 row with headers - with non-zero tables of contents
    resultCells = None
    for indRow in range(len(schedule)):
        studentInfo = schedule.loc[[indRow]]
        studentName = studentInfo['ФИО'].values[0]
        studentGroup = studentInfo['Академ группа'].values[0]
        try:
            if all(name in studentName for name in fullName) and nameGroup == studentGroup:
                indRow = studentInfo.index.values[0]
                numInGroup = studentInfo.values[0][0]
                resultCells = (indRow, numInGroup)
        except TypeError:
            continue
    try:
        groupInfo = schedule.loc[[resultCells[0] - resultCells[1]]]
        resultInfo = {}
        for header in searchHeaders:
            resultInfo[header] = groupInfo[header].values[0]
        return resultInfo
    except TypeError:
        return "Студент не найден в указанных списках."
    # result = schedule.loc[schedule["ФИО"] == 'Костионова Ксения Ивановна']
