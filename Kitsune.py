# ---------------------
# Geometry Dash username availability checker
# Coded by yak (@saucize), /oganessium
# https://github.com/oganessium
# mad props to @4201337 @NerexNX and @brensalsa
# ---------------------

import requests
import random
import itertools
print("=============================")
print("Kitsune GD - Kitsune Username scraper for the game Geometry Dash")
print("by Jack (oganessium)")
print("=============================")
def main_f():
    tool = input("Please input u for user or b for batch: ")
    if tool.lower() == "u":
        aaap = input("Input username: ")
        array = [aaap]
    elif tool.lower() == "t":
        array = ['robtop', 'viprin', 'ewkewowfo', 'KitsuneBot', 'PythonWizard', 'Orange', '6ix8ine', 'Hungary', 'Apostrophe', 'brensalsa', 'ykk', 'Yaktose', 'Geomarty']
    elif tool.lower() == "3":
        numb = input("Input number of random 3 letter usernames to scrape: ")
        letters = "abcdefghijklmnopqrstuvwxyz"
        array = []
        for _ in itertools.repeat(None, int(numb)):
            query = random.choice(letters) + random.choice(letters) + random.choice(letters)
            array.append(query)
            
    elif tool.lower() == "b":
        aaap = input("Input batch URL: ")
        try:
            e = requests.get(aaap).text
            array = e.splitlines()
        except Exception:
            print("Error: there is something wrong with the batch data you have given me! Please link to a file with one username per line!")
    else:
        print("Invalid input! please try again.")
        print("=============================")
        print("Thank you for using Kitsune!")
        print("=============================")
        exit()
    available=[]
    unavailable=[]
    if len(array) > 20:
        h = input("Error: This list is on the longer side! This could be slow and cause issues. Are you sure you want to proceed? (Y/N) ")
        if h == "Y":
            pass
        else:
            exit()
    for uname in array:
        data = {
            "gameVersion":"21", "binaryVersion":"35","gdw":"0","str":uname,"secret":"Wmfd2893gb7"
        }
        usersID = requests.post("http://boomlings.com/database/getGJUsers20.php", data=data)

        try:
            userID=usersID.text.split(":")[21]
        except Exception:
            userID="-1"
        data = {
            "gameVersion":"21","binaryVersion":"35","gdw":"0","targetAccountID":userID,"secret":"Wmfd2893gb7"
        }
        userInfo = requests.post("http://boomlings.com/database/getGJUserInfo20.php", data=data)
        if userInfo.text == "-1" and len(uname) >= 3:
            available.append(uname)
        else:
            unavailable.append(uname)
    print("=============================")
    print("Available names: {}".format(", ".join(available)))
    print("Unavailable names: {}".format(", ".join(unavailable)))
    print("=============================")
    print("Done!")
    print("=============================")
    again = input("Would you like to scrape again? (Y/N) ")
    if again == "Y":
        main_f()
    else:
        print("=============================")
        print("Thank you for using Kitsune!")
        print("=============================")

main_f()
