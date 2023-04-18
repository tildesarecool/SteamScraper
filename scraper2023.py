# I decided maybe i want to try some things left over from chatgpt
# the header tag is the main difference i didn't find any place else



#import urllib.request
#from bs4 import BeautifulSoup as bs
# new approach
from selenium import webdriver
from bs4 import BeautifulSoup
import pyperclip
#import json, pyperclip, requests

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

steamurl = "https://steamcommunity.com/id/subassy/games/?tab=all"

driver.get(steamurl)

getsource = driver.page_source


pyperclip.copy(getsource)

'''
# Extract the table data using Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')
soup.find_all('')
table = soup.find('table')
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    for col in cols:
        print(col.text)
'''
# Close the browser
driver.quit()


############################# since below didn't work either, I am going to try a different approach

'''

url = "https://steamcommunity.com/id/subassy/games/?tab=all"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

#sauce = urllib.request.urlopen(url).read()

#response = requests.get(url, headers=headers)
#html = response.text

sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

#stringsoup = string(sauce)

print(soup)
#pyperclip.copy()

#print(html)

#urllib.request.urlopen()

###############################################################


'''


'''


response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")
game_containers = soup.find_all("div", class_="gameListRow")
games = []
for game in game_containers:
    title = game.find("div", class_="gameListRowItemName").text.strip()
    hours_played = game.find("div", class_="gameListRowItemHours").text.strip()
    app_id = game["data-appid"]
    store_path = f"https://store.steampowered.com/app/{app_id}"
    game_data = {
        "title": title,
        "hours_played": hours_played,
        "app_id": app_id,
        "store_path": store_path
    }
    games.append(game_data)

file_path = "steam_games_data.json"
with open(file_path, "w") as file:
    json.dump(games, file)
print(f"Steam games data has been saved to {file_path}")


-------------------------------------------------------------------

15:08 2/5/2023

$url = 'https://steamcommunity.com/id/subassy/games/?tab=all'
$headers = @{
    'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

$response = Invoke-WebRequest -Uri $url -Headers $headers
$html = $response.Content

$game_containers = Select-Html -InputObject $html -XPath '//div[@class="gameListRow"]'
$games = @()
foreach ($game in $game_containers) {
    $title = $game.QuerySelector('div.gameListRowItemName').innerText.Trim()
    $hours_played = $game.QuerySelector('div.gameListRowItemHours').innerText.Trim()
    $app_id = $game.GetAttribute('data-appid')
    $store_path = "https://store.steampowered.com/app/$app_id"
    $game_data = @{
        'title' = $title
        'hours_played' = $hours_played
        'app_id' = $app_id
        'store_path' = $store_path
    }
    $games += $game_data
}

$file_path = 'steam_games_data.json'
$games | ConvertTo-Json | Out-File -FilePath $file_path
Write-Output "Steam games data has been saved to $file_path"

-----------------------------------------------------------------

15:08 2/5/2023

import requests
import json
from bs4 import BeautifulSoup

def get_steam_games_meta_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    game_containers = soup.find_all('div', {'class': 'gameListRow'})
    games = []
    for game in game_containers:
        title = game.find('div', {'class': 'gameListRowItemName'}).text.strip()
        hours_played = game.find('div', {'class': 'gameListRowItemHours'}).text.strip()
        app_id = game['data-appid']
        game_data = {
            'title': title,
            'hours_played': hours_played,
            'app_id': app_id
        }
        games.append(game_data)
    return games

if __name__ == '__main__':
    url = 'https://steamcommunity.com/id/subassy/games/?tab=all'
    games = get_steam_games_meta_data(url)
    with open('steam_games_data.json', 'w') as f:
        json.dump(games, f)
    print('Steam games data has been saved to steam_games_data.json')


'''