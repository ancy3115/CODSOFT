import random
length=int(input("Enter the length of the password:"))
password="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrsstuvwxyz1234567890!@#$%^&*?"
word="".join(random.sample(password,length))
print("Your random password is ",word)
print("\n          ====CODE EXECUTION SUCCESSFUL====       ")
