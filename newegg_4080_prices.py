from bs4 import BeautifulSoup
import requests

RTX_CARD_PRICES = {}  # created a hashmap to store the name and price of the graphics card


def save_price_info(url_loc):
    """
    Basic function which will get the price and name of a graphics card from newegg
    :param url_loc: newegg URL passed through
    :return: None; The function will get the product name and the price and store it inside
    a dictionary
    """
    res_loc = requests.get(url_loc)
    doc_loc = BeautifulSoup(res_loc.text, 'html.parser')

    price_loc = doc_loc.find(class_="price-current").strong.text.replace(",", "")
    name_loc = doc_loc.find(class_="form-current-value").text
    RTX_CARD_PRICES[name_loc] = price_loc


def get_cheapest_prod_val(loc_dict):
    min_key = min(loc_dict, key=loc_dict.get)
    min_val = loc_dict[min_key]
    print(f"Cheapest RTX Card: {min_key}\nPrice: {min_val}")


def get_most_expensive(loc_dict):
    max_key = max(loc_dict, key=loc_dict.get)
    max_val = loc_dict[max_key]
    print(f"Most expensive RTX Card: {max_key}\nPrice: {max_val}")


def main():
    # Storing 11 different urls to get their name and price and store it in my dictionary
    URLS = (
        "https://www.newegg.com/msi-geforce-rtx-4080-rtx-4080-16gb-ventus-3x-oc/p/N82E16814137765",
        "https://www.newegg.com/msi-geforce-rtx-4080-rtx-4080-16gb-gaming-x-slim-white/p/N82E16814137843",
        "https://www.newegg.com/msi-geforce-rtx-4080-super-rtx-4080-super-16g-expert/p/N82E16814137871",
        "https://www.newegg.com/zotac-geforce-rtx-4080-super-zt-d40820b-10p/p/N82E16814500579",
        "https://www.newegg.com/msi-geforce-rtx-4080-super-16g-suprim-x/p/N82E16814137853",
        "https://www.newegg.com/zotac-geforce-rtx-4080-super-zt-d40820q-10p/p/N82E16814500581",
        "https://www.newegg.com/msi-geforce-rtx-4080-super-16g-ventus-3x-oc/p/N82E16814137852",
        "https://www.newegg.com/gigabyte-geforce-rtx-4080-super-gv-n408saorus-m-16gd/p/N82E16814932669",
        "https://www.newegg.com/gigabyte-geforce-rtx-4080-super-gv-n408sgaming-oc-16gd/p/N82E16814932671",
        "https://www.newegg.com/asus-geforce-rtx-4080-super-rog-strix-rtx4080s-o16g-gaming/p/N82E16814126692",
        "https://www.newegg.com/gigabyte-geforce-rtx-4080-super-gv-n408saero-oc-16gd/p/N82E16814932670"
    )

    for index, item in enumerate(URLS):
        save_price_info(item)

    get_cheapest_prod_val(RTX_CARD_PRICES)
    get_most_expensive(RTX_CARD_PRICES)


if __name__ == "__main__":
    main()
