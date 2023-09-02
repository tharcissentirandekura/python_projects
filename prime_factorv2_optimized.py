from math import sqrt
import time

value = int(input("Enter the number here:"))
divisor = 2
prime_factor = []
print("Squarre root :",sqrt(value))

begin = time.time()
while divisor <= sqrt(value): # use the sqrt of a number to shorten the computation
    if value % divisor == 0:# check whenever a devisor is to be a prime
        prime_factor.append(divisor) # add it to the prime list
        value = value / divisor # update the value now
        print("Value:",value)
    else: # ckeck when it is not a prime factor
        print("new_value:",value)
        divisor = divisor + 1 # increment by 1
        print("divisor:",divisor)
        
        #if divisor > sqrt(value) and value > 1:
prime_factor.append(int(value))
        

#if value > 1: # for the last value greater that 1 add to prime factorlist
    #prime_factor.append(int(value))
    
    
end = time.time()
print("It took:",end - begin ,"secs to run")
print(prime_factor)

total = 1
for i in prime_factor:
    total = total *i
print("The multiplication is:",total)