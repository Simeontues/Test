n = int(input("How many times a day do you wash your hands: "))
months = int(input("How many months: "))

def wash_hands(n, months):

    return n*months*30*21/60

print("Wash hands: ", wash_hands(n, months), "minutes")