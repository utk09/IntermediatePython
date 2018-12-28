# Concept of inheritance
# Python looks up for method in following order: Instance attributes, class attributes and the
# from the base class

class Data(object):
    def getData(self):
        print('In Data class')


class Time(Data):  # Inheriting from Data class
    def getTime(self):
        print('In Time class')


if __name__ == '__main__':
    data = Data()  # assign Data() class
    time = Time()  # assign Time() class

    data.getData()
    time.getTime()
    time.getData()  # Inherited Data method
