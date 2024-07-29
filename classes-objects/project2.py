class laptop():
    chargertype="C type"

    def __init__(self):
        self.brand=""
        self.price=""

        def setPrice(self,price):
            self.price=price

            def getPrice(self):      #instance method 
                print(self.price)

                @classmethod                  #class method
                def changeChargerType(cls):     
                    cls.chargertype="B Type"
                    print("the charger type changed to B type")

                    @staticmethod               #static method
                    def info():
                        print("this is laptop class")

                        hp=laptop()
                        hp.setPrice(20000)
                        hp.getprice()

                        laptop.changeChargerType()
                        hp.info()
