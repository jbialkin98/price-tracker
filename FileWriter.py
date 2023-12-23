class FileWriter:
    """
    This class is responsible for writing the tracked items to a file.
    """

    def writeItemLink(self, url, f):
        """
        Writes the given URL to the file.
        """
        f.write("Link: ")
        f.write(url + "\n")

    def writeItemInfo(self, name, price, f):
        """
        Writes the given name and price to the file.
        """
        f.write("Name: ")
        f.write(name + "\n")
        f.write("Price: ")
        f.write(price + "\n")
        f.write("\n")

    def writeNewInfoToFile(self, amazon_objects, f):
        """
        Writes the information from each object into the file.
        :param amazon_objects:
        :param f:
        :return:
        """
        for amazon_object in amazon_objects:
            self.writeItemLink(amazon_object["url"], f)
            self.writeItemInfo(amazon_object["name"], amazon_object["price"], f)
        f.close()
