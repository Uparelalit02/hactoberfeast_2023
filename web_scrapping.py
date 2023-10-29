import requests
from bs4 import BeautifulSoup

# Replace this URL with the one you want to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract specific information from the page
    # For example, let's extract all the links on the page
    links = soup.find_all('a')
    
    for link in links:
        print(link.get('href'))

else:
    print('Failed to retrieve the web page.')

