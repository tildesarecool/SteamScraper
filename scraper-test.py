import requests, pyperclip, json, re
from bs4 import BeautifulSoup
from pathlib import Path

STEAM_LIBRARY_URL = '''https://steamcommunity.com/id/nelixery/games/?tab=all'''
STEAM_USER_ID = '''nelixery'''
SAVED_DATA_FILE_NAME = 'gamedata-for-' + STEAM_USER_ID + '''.txt'''

def RetrieveSteamData():
    # use get to grab the HTML source
    result = requests.get(STEAM_LIBRARY_URL) # resut.text will show whole source of page
    # make this into HTML
    loadToBeaut = BeautifulSoup(result.text, "html.parser")
    # select "only" the appropriate <script> tag with the JSON data
    scriptContent = str(loadToBeaut.select('#responsive_page_template_content > script:nth-child(4)')[0])
    #pyperclip.copy(scriptContent)
    #putToBoard = pyperclip.copy(scriptContent)
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
#RetrieveSteamData()


with open("oneline-singleentry.json", "r") as read_file: 
    data = json.load(read_file)
    #dtos = str(data)
    print(type(data))
    print(data)
    read_file.close()

