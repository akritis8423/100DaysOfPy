# num1=eval(input("enter the number: "))
# num2=eval(input("enter the number 2: "))
# sum=num1+num2
# print(type(sum))
# print(sum)


# BMI Calculator:

# height=int(input("enter the hight in m: "))
# weight=int(input("enter the weight in kg"))
# bmi=(weight/(height*height))
# print(bmi)



# your life in weeks..........

# age=eval(input("enter your current age: "))
# num=eval(input("enter the age you will live: "))
# years_remaining=num-age
# days_remain=years_remaining*365
# weeks_remain=years_remaining*52
# month_remain=years_remaining*12
#
# message=f"You have {days_remain} days, {weeks_remain} weeks, {month_remain} months left"
# print(message)


#  FINAL PROJECT------TIP CALCULATOR..............
print("welcome to the tip calculator. ")
num=eval(input("What was the total bill? "))
tip=eval(input("what percentage tip you want to give? 10, 12, or, 15? "))
split=eval(input("how many people to split the bill? "))
res=(num+tip)/split
ans=f"Each person should pay: {res}"
print(ans)
