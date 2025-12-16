# conditional operators in python like if , elif , else ,== , != , > , < , >= , <=

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
# we can also use this as online conditional operator
temp = int(input("Enter the temperature: "))    
if 25<=temp<=50: # checking range between 25 to 50
  print("Hot")
elif 10<=temp<=24: # checking range between 10 to 24
  print("Cold")
elif temp<10:
  print("Extremely Cold") # checking less than 10