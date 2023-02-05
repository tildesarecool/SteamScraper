from msilib.schema import AppId
import string
import requests, pyperclip, json, re
from bs4 import BeautifulSoup
from pathlib import Path

# this user has only 8 games. easier sampler data
STEAM_LIBRARY_URL = '''https://steamcommunity.com/id/nelixery/games/?tab=all'''
STEAM_USER_ID = '''nelixery'''
#SAVED_DATA_FILE_NAME = 'gamedata-for-' + STEAM_USER_ID + '''.txt'''
SAVED_DATA_FILE_NAME = '''gamedata-for-nelixery.txt'''

def CheckFileExists():
    p = Path(SAVED_DATA_FILE_NAME)
    #savedIsFile = 
    if (p.is_file() and p.exists()):
        #print("File exists and is a file")
        return True
    else:
        #print("File does not exist")
        return False

########## for experimental this is just here to exist so the rest of the script can go largely unmodified
def RetrieveSteamData():
    # use get to grab the HTML source
    result = requests.get(STEAM_LIBRARY_URL) # resut.text will show whole source of page
    # make this into HTML
    loadToBeaut = BeautifulSoup(result.text, "html.parser")
    # select "only" the appropriate <script> tag with the JSON data
    scriptContent = str(loadToBeaut.select('#responsive_page_template_content > script:nth-child(4)')[0])
    # jump to first character of JSON string (position)
    #PostambleStartPos = (scriptContent.find("= ") + 2)
    # decided I'll skip out the '[' and '];' before/after json string as they're probably not needed
    PostambleStartPos = (scriptContent.find("= ") + 3)
    # jump to last character of JSON string (position)
    #startSuffixPos = scriptContent.find("rgChangingGames") - 8
    startSuffixPos = scriptContent.find("rgChangingGames") - 10
    # hopefully this is just the json string
    justGamedata = scriptContent[PostambleStartPos:startSuffixPos] 
    return justGamedata


def WriteOrOpenDatafile():
    if CheckFileExists() == False:
        # hopefully not needed (for experimental version)
        DataFile = RetrieveSteamData()
        with open(SAVED_DATA_FILE_NAME, "w") as file:
            file.write(DataFile)
            file.close()
            print("file written")
        return DataFile
    else:
        with open(SAVED_DATA_FILE_NAME, "r") as file:
            # FileContents = json.load(file) # doens't work at this stage
            FileContents = file.read()            
            file.close()
        #pyperclip.copy(TakeOutEscSlash)
        return FileContents

# too lazy to integrate this into function
BringInString = WriteOrOpenDatafile()
TakeOutEscSlash = BringInString.replace('''\/''','''/''',-1)

# from here I'll try something new
# since the main one just has an inplace entry anyway

#pyperclip.copy(TakeOutEscSlash)

'''
with open("gamedata.json", "w") as file:
   file.write(TakeOutEscSlash)
   file.close()
'''
#j = open('gamedata.json')
'''
with open ("gamedata.json", "r") as readfile:
    j = readfile.read()
    readfile.close()
'''
#j = '{"appid":1536770,"name":"Learn Programming: Python - Retro","app_type":1,"logo":"https://cdn.akamai.steamstatic.com/steam/apps/1536770/capsule_184x69.jpg","friendlyURL":false,"availStatLinks":{"achievements":false,"global_achievements":false,"stats":false,"gcpd":false,"leaderboards":false,"global_leaderboards":false},"hours_forever":"192","last_played":1643042035}' #,{"appid":39210,"name":"FINAL FANTASY XIV Online","app_type":1,"logo":"https://cdn.akamai.steamstatic.com/steam/apps/39210/capsule_184x69.jpg","friendlyURL":false,"availStatLinks":{"achievements":false,"global_achievements":false,"stats":false,"gcpd":false,"leaderboards":false,"global_leaderboards":false},"hours_forever":"79","last_played":1647682819}
#j = '{"appid":1025480,"name":"1-Bit Revival: The Residuals of Null","app_type":1,"logo":"https://cdn.akamai.steamstatic.com/steam/apps/1025480/capsule_184x69.jpg","friendlyURL":1025480,"availStatLinks":{"achievements":true,"global_achievements":true,"stats":false,"gcpd":false,"leaderboards":false,"global_leaderboards":false},"hours_forever":"0.6","last_played":1642216987}'#,{"appid":1536770,"name":"Learn Programming: Python - Retro","app_type":1,"logo":"https://cdn.akamai.steamstatic.com/steam/apps/1536770/capsule_184x69.jpg","friendlyURL":false,"availStatLinks":{"achievements":false,"global_achievements":false,"stats":false,"gcpd":false,"leaderboards":false,"global_leaderboards":false},"hours_forever":"192","last_played":1643042035}'

j = '''
    "appid":1536770,
    "name":"Learn Programming: Python - Retro",
    "app_type":1,
    "logo":"https://cdn.akamai.steamstatic.com/steam/apps/1536770/capsule_184x69.jpg",
    "friendlyURL":false,
    "availStatLinks":
    {
        "achievements":false,
        "global_achievements":false,
        "stats":false,"gcpd":false,"leaderboards":false,"global_leaderboards":false
    },
        "hours_forever":"192",
        "last_played":1643042035
'''


''',
{
    "appid":39210,
    "name":"FINAL FANTASY XIV Online",
    "app_type":1,
    "logo":"https://cdn.akamai.steamstatic.com/steam/apps/39210/capsule_184x69.jpg",
    "friendlyURL":false,
    "availStatLinks":
    {
        "achievements":false,
        "global_achievements":false,
        "stats":false,
        "gcpd":false,
        "leaderboards":false,
        "global_leaderboards":false
    },
        "hours_forever":"79",
        "last_played":1647682819
}
}
'''



print(type(j))
#json.dumps

#pyperclip.copy(j)

#json.JSONDecoder().decode(j)   #.raw_decode(j)


#GameDict = json.loads(j)


