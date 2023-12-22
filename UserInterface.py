from FileWriter import *
from GetAmazonInfo import *


def main():
    print("Choose from the options below:")
    print("1. Add a new item to track")
    print("2. View my tracked items")

    user_input = input("Enter your choice: ")
    if user_input == "1":
        amazon_url = input("Paste the Amazon URL: ")
        file_writer = FileWriter()
        file_writer.writeItemLink(amazon_url)

        get_amazon_info = GetAmazonInfo()
        amazon_object = get_amazon_info.get_amazon_info(amazon_url)
        item_title = amazon_object["title"]
        item_price = amazon_object["current_price"]
        file_writer.writeItemInfo(item_title, item_price)


if __name__ == "__main__":
    main()
