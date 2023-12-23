from FileWriter import *
from FileReader import *
from GetAmazonInfo import *


def print_items(amazon_objects):
    for item in amazon_objects:
        print("Name: " + item["name"])
        print("Price: " + item["price"])
        print("Link: " + item["url"])
        print()


def print_item_names(amazon_objects):
    num = 1
    for item in amazon_objects:
        print(str(num) + ". " + item["name"])
        num += 1
    print()
    return num


def main():
    while True:
        user_input = ""
        user_input_not_valid = True

        while user_input_not_valid:
            print("Choose from the options below:")
            print("1. Add a new item to track")
            print("2. Check for price drops")
            print("3. View my tracked items")
            print("4. Remove a tracked item")
            print("5. Quit the program")
            print()

            user_input = input("Enter your choice: ")
            print()

            if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "5":
                user_input_not_valid = True
                print("Please enter a valid input")
                print()
            else:
                user_input_not_valid = False

        if user_input == "1":
            amazon_url = input("Paste the Amazon URL or type '0' to go back: ")

            if amazon_url == "0":
                print()
                continue

            file_writer = FileWriter()
            f = open("tracked_items.txt", "a")
            file_writer.writeItemLink(amazon_url.strip(), f)
            f.close()

            get_amazon_info = GetAmazonInfo()
            amazon_object = get_amazon_info.get_amazon_info(amazon_url)
            item_title = amazon_object["name"]
            item_price = amazon_object["price"]
            f = open("tracked_items.txt", "a")
            file_writer.writeItemInfo(item_title, item_price, f)
            f.close()
            print("Item successfully added.")
            print()

        elif user_input == "2":
            file_reader = FileReader()
            amazon_objects = file_reader.read_file()

            new_amazon_objects = []

            for item in amazon_objects:
                item_url = item["url"]
                item_title = item["name"]
                item_price = item["price"]

                get_amazon_info = GetAmazonInfo()
                new_amazon_object = get_amazon_info.get_amazon_info(item_url)

                old_price = float(item_price[1:])
                new_price = float(new_amazon_object["price"][1:])

                print(item_title)
                if new_price < old_price:
                    print("The price has dropped from " + item_price + " to " + new_amazon_object["price"])
                else:
                    print("The price of the item has stayed the same. It is still " + item_price)
                print("Link: " + item_url)
                print()

                new_amazon_object["url"] = item_url
                new_amazon_objects.append(new_amazon_object)

            file_writer = FileWriter()
            f = open("tracked_items.txt", "w")
            file_writer.writeNewInfoToFile(new_amazon_objects, f)

        elif user_input == "3":
            file_reader = FileReader()
            amazon_objects = file_reader.read_file()
            print_items(amazon_objects)

        elif user_input == "4":
            file_reader = FileReader()
            amazon_objects = file_reader.read_file()
            num = print_item_names(amazon_objects)
            num_to_remove = 0

            valid_num_to_remove = False
            while not valid_num_to_remove:
                num_to_remove = input("Enter the number of the item you would like to remove or type '0' to go back: ")
                if num_to_remove == "0":
                    break
                if 1 <= int(num_to_remove) <= num:
                    valid_num_to_remove = True
                else:
                    print("Please enter a valid number")
                    print()

            if num_to_remove == "0":
                print()
                continue

            amazon_objects.pop(int(num_to_remove) - 1)
            file_writer = FileWriter()
            f = open("tracked_items.txt", "w")
            file_writer.writeNewInfoToFile(amazon_objects, f)
            f.close()
            print("Item successfully removed.")
            print()

        elif user_input == "5":
            return


if __name__ == "__main__":
    main()
