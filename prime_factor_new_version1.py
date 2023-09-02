import time

value = int(input("Enter the number:"))
divisor = 2
prime_factor = []
time_begin = time.time()
while value >= divisor:
    if value % divisor == 0: # whenever a divisor is is a prime store it. 
        prime_factor.append(divisor)
        value /= divisor # update the value which is now 6

    else: #  try when divisor is not a prime number increment by 1 until it reaches to primarity
        divisor += 1
time_end = time.time()

print("It took:",time_end - time_begin)
print("The prime factors are :",prime_factor)
