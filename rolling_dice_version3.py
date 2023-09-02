import random
import matplotlib.pyplot as plt
target = int(input("The desired outcome:"))
trial = int(input("Enter the times of roll to try:"))

universe = []
outcome = [1,2,3,4,5,6]

for j in range(1,trial+1):
    universe.append(random.randint(1,7))
 

count_outcome = [universe.count(1),universe.count(2),universe.count(3),universe.count(4),universe.count(5),universe.count(6)]

number_target = universe.count(target)
possible_outcomes = len(universe)
prob_target = number_target/possible_outcomes


for i in range(len(outcome)):
    print(outcome[i],"::","appears:",count_outcome[i],"times",",its probability:",count_outcome[i]/possible_outcomes,"percentage = ",count_outcome[i]/possible_outcomes*100)
prob = [j + 0.4 for j in outcome]
predicted = [1/6*trial,1/6*trial,1/6*trial,1/6*trial,1/6*trial,1/6*trial]

print("The possible outomes are:",possible_outcomes)
print("The desired outcomes:",[target])
print("The probability of rolling:",universe)
print("The probability of getting ",target,"is:",prob_target)
print("The times",target,"appeared:",number_target)

plt.bar(outcome,count_outcome, label="observed", width = 0.5)
plt.bar(prob,predicted, label="Predicted", width = 0.4)
plt.legend()
plt.show()











