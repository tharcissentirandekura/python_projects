import matplotlib.pyplot as plt


# reading the file containg the information of students
file = open('names.txt','r')

read = file.read() 
new_list = read.split() # turning it into the list

students = [] # a lista and its sublists of students information


# making it like a string to be able to split it easily and turn it into 
# a sublists to easily access the data
for word in new_list:
    string = word.split(",") # turning it into sub-lists
    students.append(string)


more_age = []
less_age = []
province = []
ages = []

# check for the age of students in the file 
print("For those with less than 19 years old")

for i in students:
    if int(i[2]) < 19:
        less_age.append(str(i[0]) + ":"+str(i[2]) + ":" + str(i[1]))
        #print(i[1],":",i[2])

print("there are:",len(less_age),"students with less than 19")
print(less_age)
print()
print("For those with 19 years old or more:")

for i in students:
    ages.append(i[2])
    province.append(i[1])# make the list of provinces only
    if int(i[2]) > 19 or int(i[2]) == 19:
        more_age.append(str(i[0]) + ":"+ str(i[2]+ ":" + str(i[1])))
print("provinces:",province)

#iterating through the list and
for i in province:
    print(province.count(i), "in :",i) # counting provinces appeared
    plt.bar(i,province.count(i),)
    plt.title("The number of studets and their provinces", color = "green", size = 16)
    plt.ylabel("Number of students from one province", size = 14, color = "blue")
    plt.xlabel("List of provinces", size = 20, color = "blue") # graphically analyzing the students and province
    # to see where there are more students or less
for j in ages:
    print(j,": ",ages.count(j))
    #plt.plot(j,ages.count(j))

print("the are :", len(more_age), "students with 19 or more")
print(more_age)


print()
print("Total students is:", len(more_age) + len(less_age)) # showing the total
# of all students in the class.

plt.show()



        

