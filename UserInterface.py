from FileWriter import *
from GetAmazonInfo import *
from FileReader import *


def print_items(amazon_objects):
    for item in amazon_objects:
        print("Name: " + item["name"])
        print("Price: " + item["price"])
        print("Link: " + item["url"])
        print()


def main():
    print("Choose from the options below:")
    print("1. Add a new item to track")
    print("2. Check for price drops")
    print("3. View my tracked items")
    print()

    user_input = input("Enter your choice: ")
    print()
    if user_input == "1":
        amazon_url = input("Paste the Amazon URL: ")
        file_writer = FileWriter()
        file_writer.writeItemLink(amazon_url)

        get_amazon_info = GetAmazonInfo()
        amazon_object = get_amazon_info.get_amazon_info(amazon_url)
        item_title = amazon_object["title"]
        item_price = amazon_object["current_price"]
        file_writer.writeItemInfo(item_title, item_price)

    elif user_input == "2":
        file_reader = FileReader()
        amazon_objects = file_reader.readFile()

        for item in amazon_objects:
            item_url = item["url"]
            item_title = item["name"]
            item_price = item["price"]

            get_amazon_info = GetAmazonInfo()
            new_amazon_object = get_amazon_info.get_amazon_info(item_url)

            if new_amazon_object["current_price"] != item_price:
                old_price = float(item_price[1:])
                new_price = float(new_amazon_object["current_price"][1:])
                if new_price < old_price:
                    print(item_title)
                    print("The price has dropped from " + item_price + " to " + new_amazon_object["current_price"])
                    print("Link: " + item_url)
                    print()

    elif user_input == "3":
        file_reader = FileReader()
        amazon_objects = file_reader.readFile()
        print_items(amazon_objects)


if __name__ == "__main__":
    main()
