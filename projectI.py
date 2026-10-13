n = int(input("Enter a number (try 5 or 12): "))
guess = input("Left shift doubels it. guess: " + str(n) + " << 1 = ? ")

input("NOT - flips every bit. Press enter ")
print(" 12 =", bin (12)[2:])
print(" NOt 12 =", ~12 & 0xFF)

input("XOR - different bits give 1. Press Enter ")
print(" 12 ^ 10=", 12 ^ 10)

input("Left shift - multiplies by 2. Press enter ")
print(" ", n, "<< 1 =", n << 1, " your guess:", guess)

input("Right shift - divides by 2. Press enter ")
print(" ", n, ">> 1 =", n >> 1)