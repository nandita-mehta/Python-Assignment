from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def get_gender(self):
        pass


class Male(Person):
    def get_gender(self):
        print('Gender is Male')


class Female(Person):
    def get_gender(self):
        print('Gender is Female')


neha = Female()
neha.get_gender()
raj = Male()
raj.get_gender()
# pooja = Person()  <- Throws error
