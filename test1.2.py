build_price = int(input("Build price:"))
sell_price = int(input("Sell price:"))
volume = int(input("Volume of sells:"))

def calculate(build_price, sell_price, volume):
    diffrence = 0
    diffrence = sell_price - build_price
    return diffrence * volume

print(calculate(build_price, sell_price, volume))