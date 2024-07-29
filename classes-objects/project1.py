class laptop:
    price=0
    processor=" "
    ram=" "

Hp=laptop()
Dell=laptop()
Asus=laptop()


Hp.price=10000
print("HP laptop:Price:{}\n".format(Hp.price))
Hp.processor="ryzen 7"
print("HP laptop:Processor:{}\n".format(Hp.processor))
Hp.ram="8GB"
print("HP laptop:RAM:{}\n".format(Hp.ram))

Dell.price=80000
Dell.processor="Intel 7"
Dell.ram=" 16GB"
print("DELL laptop:Price:{}\n".format(Dell.price))
print("DELL laptop:Processor:{}\n".format(Dell.processor))
print("DELL laptop:RAM:{}\n".format(Dell.ram))

Asus.price=10000
print(Asus.price)
