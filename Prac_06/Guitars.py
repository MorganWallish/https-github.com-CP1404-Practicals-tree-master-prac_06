class Guitar:

    def __init__(self, name, year, cost):

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def get_age(self):

    def is_vintage(self):