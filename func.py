#declar some classes :)

class basetask:
    def __init__(self, length, weight, name) -> None:
        self.length = length
        self.weight = weight
        self.name = name

    def printTask(self):
        print("lengh of bt is", self.length, "weight of bt is", self.weight, "name of bt is ", self.name)

class schooltask(basetask):
    def __init__(self, length, weight, name) -> None:
        super().__init__(length, weight, name)

    def printSchoolTask(self):
        print("length of schooltask is ", self.length, "wegith is ", self.weight, "name is", self.name)

class workTask(basetask):
    pass

bt = basetask(1111, 0 , "boringtask")
bt.printTask()

st = schooltask(10, 1, "schooltask")
st.printSchoolTask()

