input("Parity - last bit = 0 even, last bit = 1 odd. Press Enter")
for n in [32, 33, 34, 35, 36, 37, 38, 39]:
    if n & 1:
        print(" ", n, "-> odd")
    else:
        print(" ", n, "-> even")

n = int(input("Enter a number (try 21 or 70): "))
input("Count the 1s - watch bits drop off. Press Enter ")
temp = n
while temp > 0:
    print(" binary:", bin(temp)[2:], " last bit:", temp & 1)
    temp >>= 1
print(" total 1s in", n, "=", bin(n).count('1'))