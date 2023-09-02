def is_prime(number):
    
    factors = []
    for i in range(2,number+1):
        if number % i == 0:
            factors.append(i)
    if len(factors) == 1:
        return factors

range_number = int(input("Enter a number:"))
prime_numbers = []

for num in range(2,range_number + 1):
    if is_prime(num):
        prime_numbers.append(num)

print("The prime numbers from 2 to ",range_number,"is:",prime_numbers)
        