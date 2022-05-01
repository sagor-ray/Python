class firstClass:
    def __init__(self):
        a = 5
        global b
        b = 10
        self.result = a + b
        print(self.result)
    def new(self):
        print("My name is Sagor Ray")
p1 = firstClass()
p1.new()


