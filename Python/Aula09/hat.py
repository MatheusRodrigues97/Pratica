from random import choice

class Hat:

    def __init__(self):
        self.house = ["grifinoria", "lufalufa", "Corvinal ", "Sonserina"]

    def sort (self, name):
        print(name, "is in", choice(self.house))

hat = Hat()

hat.sort("Harry")