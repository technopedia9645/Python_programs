import colorama
from colorama import Fore
file = 'value.txt'
with open(file) as values:
    lines = values.readlines()
string = ''
for line in lines:
    string += line.rstrip()
# print(len(string))
date = input("enter your birthday in ddmmyy format: ")
if date in string:
    print(Fore.GREEN + "Cheers! your birthday is in the million digits of the value of pi")
else : 
    print(Fore.RED + "your birthday is not in the million digits of the value of pi")