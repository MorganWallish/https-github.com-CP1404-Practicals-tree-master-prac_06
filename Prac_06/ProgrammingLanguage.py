class ProgrammingLanguage:

    def __init__(self, title, typing, reflection, year):
        self.title = title
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False


    def __str__(self):
        return "{}, {} typing, Reflection={}, first appeared in {}".format(self.title, self.typing, self.reflection,
                                                                           self.year)






