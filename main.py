import requests
from bs4 import BeautifulSoup
from pony import orm
from datetime import datetime

# Creating the database
db = orm.Database()
db.bind(provider="sqlite", filename="products.db", create_db=True)


class Product(db.Entity):
    name = orm.Required(str)
    price = orm.Required(float)
    created_date = orm.Required(datetime)


db.generate_mapping(create_tables=True)


# Function for scrapping website
def newegg(url_loc, session):
    resp = session.get(url_loc)
    doc = BeautifulSoup(resp.text, 'html.parser')
    price_loc = doc.strong.get_text()
    price_loc = float(price_loc.replace(",", ""))
    data = (
        "Newegg",
        price_loc
    )
    return data


def amazon(url_loc, session):
    resp = session.get(url_loc)
    doc = BeautifulSoup(resp.text, 'html.parser')
    price_loc = float(doc.find(class_="a-price-whole").text.replace(".", "").replace(",", ""))
    data = (
        "Amazon",
        price_loc
    )
    return data


def ebay(url_loc, session):
    resp = session.get(url_loc)
    doc = BeautifulSoup(resp.text, "html.parser")
    price_loc = float(doc.find(class_="ux-textspans"))

def main():
    session = requests.Session()
    # Headers
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/122.0.0.0 Safari/537.36"
    })
    print(newegg("https://www.newegg.com/msi-geforce-rtx-4080-rtx-4080-16gb-ventus-3x-oc/p/N82E16814137765", session))
    print(amazon("https://www.amazon.com/MSI-Tri-Frozr-Lovelace-Architecture-Graphics/dp/B0BL61TNG1/ref=asc_df_B0BL61TNG1/?tag=hyprod-20&linkCode=df0&hvadid=636987148024&hvpos=&hvnetw=g&hvrand=9963020479621512965&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9028277&hvtargid=pla-1917035310440&psc=1&mcid=1a94810ce566302387ec4f1636e4e303&gclid=Cj0KCQjwwMqvBhCtARIsAIXsZpY_QmDs2KtxFwyOehB2BGOkLKwpJT8VQAsVv0g2eVRyB8V8BLC6e1QaAivcEALw_wcB", session))


if __name__ == "__main__":
    main()
