class FileWriter:
    """
    This class is responsible for writing the tracked items to a file.
    """

    def writeItemLink(self, url, f):
        """
        Writes the given URL to the file.
        """
        # f = open("tracked_items.txt", "a")
        f.write("Link: ")
        f.write(url + "\n")

        # f.close()

    def writeItemInfo(self, name, price, f):
        """
        Writes the given name and price to the file.
        """
        # f = open("tracked_items.txt", "a")
        f.write("Name: ")
        f.write(name + "\n")
        f.write("Price: ")
        f.write(price + "\n")
        f.write("\n")
        # f.close()

    def writeNewInfoToFile(self, amazon_objects, f):
        for amazon_object in amazon_objects:
            self.writeItemLink(amazon_object["url"], f)
            self.writeItemInfo(amazon_object["title"], amazon_object["current_price"], f)
        f.close()
