"""
binary = input("Enter binary to find number:")
x = len(binary)
number = []
for bin in range(x):
    x -= 1
    print(x)
    number.append(int(binary[bin])*(2)**x)
print(binary,": is equal to:",sum(number))

"""
number = int(input("Enter a number:"))
binary = 2
bin = []
while number >=binary:
    print(number // binary)
    if number % binary == 0:
        bin.append(number % binary)
        number = number //binary
        if number == 1:
            bin.append(number)

print(bin)


