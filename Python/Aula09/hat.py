from random import choice

class Hat:

    house = ["grifinoria", "lufalufa", "Corvinal ", "Sonserina"]

    @classmethod
    def sort (cls, name):
        print(name, "is in", choice(cls.house))

Hat.sort("Harry")