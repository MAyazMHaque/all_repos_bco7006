# object oriented programming

class Student(object):
    def __init__(self, name, number, age): # here name is the name of the students and number is the number of units studetns is studying
        self._name = name # creating the variable to store the name of the student
        self._scores = []  # creating th empty list to store the scores of the each subjects
        self._age = age
        for count in range(number):
            self._scores.append(0)

    def getName(self):
        return self._name

    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age

    def setScore(self, i, score):
        self._scores[i - 1] = score

    def getScore(self, i):
        return self._scores[i - 1]

    def getAverage(self):
        return sum(self._scores) / len(self._scores)

    def getHighScore(self):
        return max(self._scores)

    def __str__(self):
        return  "Name: " +self._name + "\nScores: " + \
                    " ".join(map(str, self._scores)) + "\nAge: " +str(self._age)
# on 23 Mar Pakistan Day
s = Student("Ayaz", 5, 29) # here "s" is the instance of the class student
s.setScore(2,89)
s.setScore(3,67)
s.setScore(5,78)
s.setScore(1,85)
# print(s.getScore(1))
print(s)

