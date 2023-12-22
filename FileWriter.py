class FileWriter:
    """
    This class is responsible for writing the tracked items to a file.
    """

    def writeItemLink(self, url):
        """
        Writes the given URL to the file.
        """
        f = open("tracked_items.txt", "a")
        f.write("Link: ")
        f.write(url + "\n")

        f.close()

    def writeItemInfo(self, name, price):
        """
        Writes the given name and price to the file.
        """
        f = open("tracked_items.txt", "a")
        f.write("Name: ")
        f.write(name + "\n")
        f.write("Price: ")
        f.write(price + "\n")
        f.write("\n")
        f.close()
