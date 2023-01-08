#035 ask the user to enter their name and then display their name three times
# name = input("Enter your name?")
# for i in range(3):
#     print(name)

#036 Alter 035 so that it will ask the user to enter their name and a number and then display their name that number of times
# name = input("Enter your name?")
# num = int(input("Enter a number?"))
# for i in range(0,num):
#     print(name)
#037 Ask the user to enter their name and display each letter in their name on a separate line.
# name = input("Enter your name?")
# for i in name:
#     print(i)

#038 Change program to  also ask for a number. Display their name(one letter at a time on each line) and 
#repeat this for the number of times they entered
# name = input("Enter your name?")
# num = int(input("Enter a number?"))
# for x in range(0, num):
#     for i in name:
#         print(i)

#039 Ask the user enter a number between 1 and 12 and then display the times before table for that number
# num = int(input("Enter a number between 1-12?"))
# for i in range(1,13):
#     answer = i*num
#     print(i, "x", num, "=", answer)
#040 Ask for a number and then count down from 50 to that number they entered in the output:
number = int(input("Enter a number below 50?"))
for num in range(50,number-1,-1):
    print(num,end=" ")
