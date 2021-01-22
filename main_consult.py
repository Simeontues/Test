from calculate import calculate
days = int(input("How many days did you worked: "))
salary = 0
bonus = 0
full = 0

salary = days*200
bonus = calculate(days)
full = salary + bonus