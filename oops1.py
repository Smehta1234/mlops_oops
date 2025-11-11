class employee:
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.desigination = "SDE"

    def travel(self,destination):
        print(f"employee is now traveling to {destination}")


sam = employee()
# print(sam.id)
sam.travel("kerala")
