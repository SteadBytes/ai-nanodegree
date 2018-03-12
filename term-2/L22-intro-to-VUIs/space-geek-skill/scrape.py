import requests
from bs4 import BeautifulSoup
# scrape list of 100 space facts from:
url = 'https://www.thefactsite.com/2012/01/100-random-facts-about-space.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}


def get_facts(soup):
    ol = soup.find('ol')
    lis = [li for li in soup.find('ol').find_all('li')]
    # some list items have <script> tags embedded after text
    # contents[0] just to get text
    # som items are just an <a> tag -> ignore these
    facts = [li.contents[0] for li in lis if not li.find('a')]
    return facts


facts = []
# facts are paginated, simply with a '/<page_number>' appended to url
for i in range(5):
    if i == 0:
        page_url = url
    else:
        page_url = f'{url}/{i}'

    r = requests.get(page_url, headers=headers)
    soup = BeautifulSoup('\n'.join(r.text.splitlines()), 'html.parser')
    facts += get_facts(soup)

print(facts)
