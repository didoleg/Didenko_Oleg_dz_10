from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc_size(self):
        pass


class Coat(Clothes):
    @property
    def calc_size(self):
        necessary_size = round(self.size / 6.5 + 0.5)
        return necessary_size


class Suit(Clothes):
    @property
    def calc_size(self):
        necessary_size = round(self.size * 2 + 0.3)
        return necessary_size


coat = Coat(48)
suit = Suit(178)
print(coat.calc_size)
print(suit.calc_size)
