# Import the HTML agility pack module
#Import-Module -Name HtmlAgilityPack

#using namspace 

#"C:\Users\Keith\Documents\repos\SteamScraper\HtmlAgilityPack.dll"

# Define the URL of the Steam store page


Add-Type -Path "C:\Users\Keith\Documents\repos\SteamScraper\HtmlAgilityPack.dll"
$url = "https://steamcommunity.com/id/subassy/games/?tab=all"
# Create a web request and fetch the HTML content of the page
$request = [System.Net.HttpWebRequest]::Create($url)
$response = $request.GetResponse()
$stream = $response.GetResponseStream()
$reader = New-Object System.IO.StreamReader($stream)
$content = $reader.ReadToEnd()

$html = New-Object HtmlAgilityPack.HtmlDocument
$hcontent = $html.LoadHtml($content)

#$hcontent = $html.DocumentNode.GetClasses()
Write-Host($content)

$nodes = $html.DocumentNode.SelectNodes("//a[@class='game-name-link']")
foreach ($node in $nodes) {
    Write-Output $node.InnerHtml
}





# Create a web request and fetch the HTML content of the page
$request = [System.Net.HttpWebRequest]::Create($url)
$response = $request.GetResponse()
$stream = $response.GetResponseStream()
$reader = New-Object System.IO.StreamReader($stream)
$content = $reader.ReadToEnd()

# Load the HTML content into the HTML agility pack
$html = New-Object HtmlAgilityPack.HtmlDocument
$html.LoadHtml($content)

# Find the "RECOMMENDED" header
$recommendedHeader = $html.DocumentNode.SelectSingleNode("//div[@id='recommended_block']//h2[@class='section_title']")
if ($recommendedHeader) {
    Write-Host "Recommended header found: $($recommendedHeader.InnerText)" -ForegroundColor Green

    # Find the first three entries under the "RECOMMENDED" header
    $entries = $recommendedHeader.ParentNode.SelectNodes(".//div[contains(@class, 'recommendation')]") | Select-Object -First 3

    # Display the title, release date, and price of each entry
    foreach ($entry in $entries) {
        $title = $entry.SelectSingleNode(".//div[@class='responsive_search_name_combined']//span[@class='title']")?.InnerText.Trim()
        $releaseDate = $entry.SelectSingleNode(".//div[@class='responsive_search_name_combined']//div[@class='col search_released responsive_secondrow']")?.InnerText
        $price = $entry.SelectSingleNode(".//div[@class='col search_price_discount_combined responsive_secondrow']//div[@class='col search_price discounted responsive_secondrow']//span[@class='discounted']")?.InnerText

        Write-Host "Title: $($title)"
        Write-Host "Release date: $($releaseDate)"
        Write-Host "Price: $($price)" -ForegroundColor Cyan
        Write-Host ""
    }
}
else {
    Write-Host "Recommended header not found." -ForegroundColor Yellow
}
