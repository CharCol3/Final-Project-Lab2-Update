class Student:
    def __init__(self, name: str, scores: list[int]):
        self.__name = name
        self.__scores = scores
        self.__grade = None
        self.calculate_statistics()

    def calculate_statistics(self):
        if not self.__scores:
            self.__highest = self.__lowest = self.__average = 0
        else:
            self.__highest = max(self.__scores)
            self.__lowest = min(self.__scores)
            self.__average = sum(self.__scores) / len(self.__scores)
        self.assign_grade()

    def assign_grade(self):
        if self.__highest >= 90:
            self.__grade = 'A'
        elif self.__highest >= 80:
            self.__grade = 'B'
        elif self.__highest >= 70:
            self.__grade = 'C'
        elif self.__highest >= 60:
            self.__grade = 'D'
        else:
            self.__grade = 'F'

    @property
    def grade(self):
        return self.__grade

    @property
    def name(self):
        return self.__name

    @property
    def scores(self):
        return self.__scores.copy()
