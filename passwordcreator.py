
#this script for learning python
# Script aimed to create a password It contains a random arrangement of letters
#numbers and signs in certain proportions 
#with the least number of elements 6 to an unspecified number depending on the user's request
 
 #import modules
import string
import random

 #Preparing lists of elements that make up the password
s1= list(string.ascii_lowercase)
s2= list(string.ascii_uppercase)
s3= list(string.digits)
s4= list(string.punctuation)

 #characters Numbers of password
char_num= input("Enter numbers for password's elements")

 #this Operational Loop , identify the input type and Specify the length of the password
while True:
    try:
        char_num= int(char_num)
        if char_num <6:
            print("Enter at least 6 to create good password ")
            char_num= input("please try another available number !")
        else:
            break
    except:
        print('Please Enter numbers only ')
        char_num= input("Enter numbers for password's elements ")

 #shuffle the random selections from the lists of (letters(lower case & upper case), numbers & punctuations)
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

 #Determine the required percentage for each list (20% &30%)
part1= round(char_num*(30/100))
part2= round(char_num*(20/100))
#List that will contain the password
password= []

 #Letter creation loop by 30%
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
 #Letter creation loop by 20%
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
 #shuffle the all selections after password created
random.shuffle(password)
 #Re-save the password after shuffling
password= "".join(password[0:])

#get the password
print(password)
   