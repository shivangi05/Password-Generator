import random
print("Wlcome to the password generator!")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special = ['!','@','#','$','%','^','&','*']

lettersinput = int(input("How many letters would you like to have?"))
numbersinput = int(input("How many numbers would you like to have?"))
specialinput = int(input("How many special characters would you like to have?"))

lpass = ""
for char in range(1,lettersinput +1):
    letterp = random.choice(letters)
    lpass = letterp + lpass
#print(lpass)

npass = ""
for char in range(1,numbersinput +1):
    numberp = random.choice(numbers)
    npass = numberp + npass
#print(npass)

spass = ""
for char in range(1,specialinput +1):
    specialp = random.choice(special)
    spass = specialp + spass

# Final print
password = lpass+npass+spass
#print(password)

totalnumber = lettersinput + numbersinput + specialinput
#print(totalnumber)

finalpassword = ""
for num in range(1, totalnumber+1):
    fpassword = random.choice(password)
    finalpassword = finalpassword+fpassword
print(f"Your new password is {finalpassword}.")   
