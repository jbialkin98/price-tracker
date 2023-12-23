import requests
from bs4 import BeautifulSoup


class GetAmazonInfo:
    """
    This class is used to get the information from the Amazon website.
    """

    def get_amazon_info(self, url):
        headers = {"accept-language": "en-US,en;q=0.9", "accept-encoding": "gzip, deflate, br",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                 "Chrome/111.0.0.0 Safari/537.36",
                   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                             "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

        # url = ("https://www.amazon.com/PlayStation-Console-Marvels-Spider-Man-Bundle-5/dp/B0CKZGY5B6/?_encoding=UTF8"
        #        "&pd_rd_w=AMPU5&content-id=amzn1.sym.bfeb452d-6b18-4a24-ba5e-59373fde003c%3Aamzn1.symc.09cd26f5-5745-467b"
        #        "-9787-8f66ac3a0285&pf_rd_p=bfeb452d-6b18-4a24-ba5e-59373fde003c&pf_rd_r=ESMS95PMJGPNSBGGW50K&pd_rd_wg"
        #        "=xK2e3&pd_rd_r=039a531e-4020-4cef-9472-e437c3dcf5a5&ref_=pd_gw_ci_mcx_mr_hp_d")

        page = requests.get(url, headers=headers)

        item_object = {}

        soup = BeautifulSoup(page.content, "lxml")

        try:
            title = soup.find("span", attrs={"id": 'productTitle'})
            title_string = title.string.strip()  # Title as a String Object
            item_object["name"] = title_string
        except:
            item_object["name"] = "Not Found"

        try:
            current_price = soup.find("span", attrs={"class": 'a-offscreen'})
            current_price_string = current_price.string.strip()  # Price as a String Object
            item_object["price"] = current_price_string
        except:
            item_object["price"] = "Not Found"

        return item_object

