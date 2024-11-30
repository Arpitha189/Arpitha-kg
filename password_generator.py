import random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*''(',')']
print("WELLCOME TO PASSWORD GENERATOR")
n_letter=int(input("how many letters do you want in password:"))
n_number=int(input("how many number do you want in password:"))
n_symbols=int(input("how many symbols do you want in password:"))
password=[]
for i in range(1,n_letter+1):
    p=random.choice(letter)
    password+=p
for i in range(1,n_number+1):
    q=random.choice(number)
    password+=q 
for i in range(1,n_symbols+1):
    r=random.choice(symbols)
    password+=r        
print(password)
random.shuffle(password)
N=print(password)
Password=""
for i in password:
    Password+=i
print(Password)    #casesensitive caps and small are different
