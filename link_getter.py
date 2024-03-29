from bs4 import BeautifulSoup
import requests


def get_product_links():
    search_url = "https://www.newegg.com/p/pl?d=rtx4080&N=100006662"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers, timeout=60)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_links = soup.findAll("a", {"class": "item-title"})

    links = [link['href'] for link in product_links if 'href' in link.attrs]
    return links


prod_links = get_product_links()
for link in prod_links:
    print(link)
