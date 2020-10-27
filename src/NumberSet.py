from random import shuffle
from random import randint


class NumberSet:
    def __init__(self, size, maxValue):
        self.__size = size
        self.__maxValue = maxValue
        self.__numberSet = []
        self.__index = 0
        self.populate()
        pass

    def populate(self):
        for _ in range(0, self.__size**2):
            ranNum = randint(0, self.__maxValue)
            while self.__numberSet.__contains__(ranNum):
                ranNum = randint(0, self.__maxValue)
            self.__numberSet.append(ranNum)

    def getSize(self):
        return self.__size
        pass

    def get(self, index):
        return self.__numberSet[index]
        pass

    def randomize(self):
        shuffle(self.__numberSet)
        pass

    def getNext(self):
        return self.__numberSet[self.__index]
        pass

    def print(self):
        print(self.__numberSet)
