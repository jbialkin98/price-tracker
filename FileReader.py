from GetAmazonInfo import *


class FileReader:
    """
    Class for reading tracked items file.
    """

    def read_file(self):
        get_amazon_info = GetAmazonInfo()
        amazon_objects = []

        f = open("tracked_items.txt", "r")
        amazon_object = {}

        for line in f:
            if line.startswith("Link: "):
                amazon_url = line[6:].strip()
                amazon_object["url"] = amazon_url
            elif line.startswith("Name: "):
                item_name = line[6:].strip()
                amazon_object["name"] = item_name
            elif line.startswith("Price: "):
                item_price = line[7:].strip()
                amazon_object["price"] = item_price
                amazon_objects.append(amazon_object)
                amazon_object = {}

        f.close()
        return amazon_objects
