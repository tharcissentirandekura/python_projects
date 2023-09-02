from math import sqrt

def find_prime(value):
    divisor = 2 
    prime_factor = []
    
    
    while divisor <= sqrt(value): # use the sqrt of a number to shorten the computation
        if value % divisor == 0:# check whenever a devisor is to be a prime
            prime_factor.append(divisor) # add it to the prime list
            value = value / divisor # update the value now
        else: # ckeck when it is not a prime factor
            divisor = divisor + 1 # increment by 1
    
            
    prime_factor.append(int(value))
    #print(prime_factor)
    return prime_factor
        

number = int(input("Enter the number here:"))
prime_list = []
for num in range(2,number + 1):
    if len(find_prime(num)) == 1 :
        prime_list.append(num)
print("prime factors checked:",find_prime(number))
print(prime_list)




