import matplotlib.pyplot as plt

value = int(input("Enter a number:"))

sequence_list = [] # the list of the sequence's list of each number
length_seq = []# len of sequence list of any number between 2 and n

max_val_seq = [] # max value reached in every number's sequence list
longest_seq = []

leading_digits = []

digits = [1,2,3,4,5,6,7,8,9]
leading_digits_count = []
for num in range(2,value + 1):
    
    sequence = [num]
    while num >= 2:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
            
        sequence.append(num)
            

    sequence_list.append(sequence)
    length_seq.append(len(sequence)) 
    max_val_seq.append(max(sequence))
    
    if max(length_seq) == len(sequence):
        longest_seq = sequence
    for num in sequence:
        leading_digits.append(int(str(num)[0]))

for i in list(set(sorted(leading_digits))):
    leading_digits_count.append(leading_digits.count(i))

plt.bar(digits,leading_digits_count)
        
        
        
    






