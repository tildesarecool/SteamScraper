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
    startSuffixPos = scriptContent.find("rgChangingGames") - 11 # 10 is two '}' at the end
    # hopefully this is just the json string
    justGamedata = scriptContent[PostambleStartPos:startSuffixPos] 
    #pyperclip.copy(justGamedata)
    return justGamedata
#RetrieveSteamData()

'''
with open("oneline-singleentry.json", "r") as read_file: 
    data = json.load(read_file)
    #dtos = str(data)
    print(type(data))
    print(data)
    read_file.close()
'''

#test-entries.txt

# hypothetical steps:
# 1. bring in data from test-entries
# 2. add pre- and post-amble
# 3. use loads to convert to dictionary object first?...i think the dump() does need dictionary as input parameter
# 4. used dump() to immediately write result to .json file

with open('test-entries.txt', "r") as file:
    contents = file.read()           # step 1: bring in data from txt file
    #print(contents)
    preamble = '''{ "game_library": ['''
    postamble = ''']}'''
    newContents = preamble + contents + postamble # step 2: add pre- and post-amble
    #print(newContents)
    newContentsAsJson = json.loads(newContents) # step 3: used loads() to convert data to dictionary object
    print(type(newContentsAsJson))
    print(newContentsAsJson)
    file.close()

with open('validated-data.json', "w") as jfile:
    json.dump(newContentsAsJson, jfile, indent=4)

