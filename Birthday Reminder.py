#Birthday Reminder Through excel File
def playsound():
    from playsound import playsound
    playsound("E:\\Laptop Data\\Software Engineering\\2nd Semester\\Object Oriented Programming\\Project Folder\\tiny_text_message.mp3")
    

def notification():
    import time
    from plyer import notification
    notification.notify(
        title = "Birthday Reminder",
        message = "Wish your Friend a very happy birthday",
        timeout = 30,
    )


import pandas as pd
excelRead=pd.read_excel("E:\\Laptop Data\\Software Engineering\\2nd Semester\\Object Oriented Programming\\Project Folder\\Birthdates.xlsx" ,sheet_name="Sheet1")
print(excelRead)

import datetime
today=datetime.datetime.now().strftime("%d-%m")
#print(today)

for index,item in excelRead.iterrows():
    bday=item["Birthdate"].strftime("%d-%m")
    #print(bday)

    if today == bday:
        notification()
        playsound()
