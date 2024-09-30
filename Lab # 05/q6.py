class Employee(ABC):
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    @abstractmethod
    def calBonus(self):
        pass


class Manager(Employee):
    def __init__(self, name, sal):
        super().__init__(name, sal)

    def calBonus(self):
        return self.sal * 20 / 100

    def Hire(self):
        print("Hiring Someone....")


class Developer(Employee):
    def __init__(self, name, sal):
        super().__init__(name, sal)

    def calBonus(self):
        return self.sal * 10 / 100

    def WriteCode(self):
        print("Writing Code....")


class SeniorManager(Manager, Developer):
    def __init__(self, name, sal):
        super().__init__(name, sal)

    def calBonus(self):
        return 30 / 100 * self.sal


sm = SeniorManager("aisha", 100000)
print("Bonus is ", sm.calBonus())
sm.WriteCode()
sm.Hire()

