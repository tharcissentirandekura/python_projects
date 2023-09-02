import matplotlib.pyplot as plt

value = int(input("Enter a number:"))

sequence_list = []
for num in range(2,value + 1):
    k = num
    sequence = [num]
    while num >= 2:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        sequence.append(num)

    sequence_list.append(sequence)
    print(k,": Sequence is:",sequence,"length:",len(sequence),
"highest reached:",max(sequence))
print("list of seq:",sequence_list)

print((list(range(len(sequence_list)))),sequence_list)

for seq in range(len(sequence_list)):
    plt.plot(range(len(sequence_list[seq])),sequence_list[seq]) # to
#be able to scatter, i preprocess data

plt.scatter(list(range(len(sequence))), sequence)

#plt.plot(list(range(len(sequence))), sequence)

plt.plot(sequence.index(max(sequence)), max(sequence), color =
"red",label = "Highest stopping point")
#plt.legend()
plt.show()