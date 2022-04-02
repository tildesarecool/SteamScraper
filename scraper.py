# couldn't decide how to do this:
# just set a static URL or ask user (me) for input and concatenate together a URL?
# static owuld be easier during development but I want to at least how prompt works out
# so I'll leave both versions and uncomment if necessary

# so I'll try it this way and change it later if I need to
# sampler steam profile URL (random user whom i don't know)
#https://steamcommunity.com/id/nelixery/games/?tab=all
# this user only has a few games which is much easier to deal with than a 1000+ records
# a sample json would also make it easier but this is fine

#steamURLFirstHalf = '''https://steamcommunity.com/id/'''
#steamURLSecondHalf = '''/games/?tab=all'''
# step 1: ask for steam ID:
#input_string_var = input("Enter Steam ID only: ") # Returns the data as a string
# next, concatentate that with the game collection page of user profile
#STEAM_LIBRARY_URL = steamURLFirstHalf + input_string_var + steamURLSecondHalf

# import some modules. probably need reg expressions eventually too.
import requests, pyperclip, json
from bs4 import BeautifulSoup
from pathlib import Path

# this user has only 8 games. easier sampler data
STEAM_LIBRARY_URL = '''https://steamcommunity.com/id/nelixery/games/?tab=all'''
SAVED_DATA_FILE_NAME = '''gamedata.txt'''
# I could check the return code here but I'll save that for later instead

# this part should be a function since I don't want to download the HTML and parse it
# every time I run the script, only if the written text file doesn't exist or if the user
# requests it be downloaded

######## this block of code checks if the file exists or not and only if not writes the data
def CheckFileExists():
    p = Path(SAVED_DATA_FILE_NAME)
    #savedIsFile = 
    if (p.is_file() and p.exists()):
        #print("File exists and is a file")
        return True
    else:
        #print("File does not exist")
        return False


'''
    if savedIsFile == True:
        print("It is a file")
        if p.exists() == True:
            print("The file exists")
        else:
            print("The file does not exist")
'''
    #print("value of fileexists is " + str(fileExists))
    #if fileExists == False:
    #    print(fileExists)
    #else:
    #    print("True")
    #return fileExists
    #print(fileExists)


#print(CheckFileExists())


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
# this just copies the above varialbe to the clipboard so I can paste into notepad
# and yes, I have the json string only
#pyperclip.copy(justGamedata)

# now I need to write this captured json out to a text file
# it feels like
# https://learnxinyminutes.com/docs/python/
# is almost as good as an actual book for reference and looking up things like this
# of course actual book is also good reference:
# https://automatetheboringstuff.com/2e/chapter9/

# with open("myfile1.txt", "w+") as file:
# file.write(str(contents))        # writes a string to a file

#print("Vale of file exists is ", + CheckFileExists())

if CheckFileExists() == False:
    with open(SAVED_DATA_FILE_NAME, "w+") as file:
        file.write(justGamedata)
        file.close()
        print("file written")
else:
    print("file exists")
        
#else:
#    with open(SAVED_DATA_FILE_NAME, "r+") as file:
        #sReadFile = o.read() # probably returns string
#        print("Vale of file exists is ", + CheckFileExists())
#        fcontents = file.read()
    #print(fcontents)


#pyperclip.copy(sReadFile)


    






'''

# Reading from a file
with open('myfile1.txt', "r+") as file:
    contents = file.read()           # reads a string from a file
print(contents)

'''











