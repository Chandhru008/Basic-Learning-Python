class laptop:
    def __init__(self):
        self.ram=0
        self.processor=""
    def display(self):
        print("ram:",self.ram)  
        print("processor:",self.processor) 

hp=laptop()
dell=laptop()

hp.ram=8
hp.processor="intel"

dell.ram=8
dell.processor="intel"

hp.display()
dell.display()

