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
        f = open("tracked_items.txt", "a")
        file_writer.writeItemLink(amazon_url, f)
        f.close()

        get_amazon_info = GetAmazonInfo()
        amazon_object = get_amazon_info.get_amazon_info(amazon_url)
        item_title = amazon_object["title"]
        item_price = amazon_object["current_price"]
        f = open("tracked_items.txt", "a")
        file_writer.writeItemInfo(item_title, item_price, f)
        f.close()

    elif user_input == "2":
        file_reader = FileReader()
        amazon_objects = file_reader.readFile()

        print("Amazon objects: ")
        print(amazon_objects)

        new_amazon_objects = []

        for item in amazon_objects:
            item_url = item["url"]
            item_title = item["name"]
            item_price = item["price"]

            get_amazon_info = GetAmazonInfo()
            new_amazon_object = get_amazon_info.get_amazon_info(item_url)

            old_price = float(item_price[1:])
            new_price = float(new_amazon_object["current_price"][1:])
            if new_price < old_price:
                print(item_title)
                print("The price has dropped from " + item_price + " to " + new_amazon_object["current_price"])
                print("Link: " + item_url)
                print()

            new_amazon_object["url"] = item_url
            new_amazon_objects.append(new_amazon_object)

        print("New Amazon objects: ")
        print(new_amazon_objects)

        file_writer = FileWriter()
        f = open("tracked_items.txt", "w")
        file_writer.writeNewInfoToFile(new_amazon_objects, f)

    elif user_input == "3":
        file_reader = FileReader()
        amazon_objects = file_reader.readFile()
        print_items(amazon_objects)


if __name__ == "__main__":
    main()
