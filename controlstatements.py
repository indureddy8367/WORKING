# 1. program to check whether given character is vowel or not

character = input("enter a character : ")
if character in "aeiouAEIOU" :
    print(f" Entered character - {character} is an Vowel")
else :
    print(f"Entered character - {character} is a consonent")


# 2. program to Age Group Classification
# Child: 0-12 years
# Teenager: 13-17 years
# Adult: 18-64 years
# Senior: 65 years and older


age = int(input("Enter ur age: "))
if age>=0 and age<=12 :
    print(f"The person age of {age} is an - Child ")
elif age>=13 and age<=17 :
    print(f"The person age of {age} is an - Teenager ")
elif age>=18 and age<=64 :
    print(f"The person age of {age} is an  - Adult ")
else :
    print(f"The person age of {age} is an - Senior")

# 3. program to take a integer and classify it is an positive, negative and zero using if elif else

value1 = int(input("Enter an integer : "))
if value1 > 0 :
    print(f"Entered integer {value1} is a positive")
elif value1< 0 :
    print(f"Entered integer {value1} is a naegative number")
else :
    print(f"Entered integer {value1} is zero")

# 4. Program that checks whether a given year is a leap year or not. 
#       A leap year is divisible by 4, but not by 100 unless it is divisible by 400.

leap_year = int(input("enter a Year : "))

if(leap_year%4==0 or leap_year%400==0) and leap_year%100!=0 :
    print("Entered year {year} is a Leap Year")
else :
    print("Entered year {year} is not a leap Year ")

# 5. Calculator +,-,*,/

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
operator = input("enter operator :")

if operator == '+' :
    print("Selected Operator addition {+} and the result for the given numbers is : ", num1+num2)
elif operator == '-' :
    print("Selected Operator subtraction {-} and the result for the given numbers is : ", num1-num2)
elif operator == '*' :
    print("Selected Operator multiplication {*} and the result for the given numbers is : ", num1*num2)
elif operator == '/' :
    print("Selected Operator division {/} and the result for the given numbers is : ", num1/num2)
else :
    print("Wrong operator Selected")

# 6. Shorthand if

num = int(input("Enter a numer to find even or odd : "))
result = "even" if num%2 ==0 else "odd"
print(result)

# 7. Discount Calculator 
product_cost = int(input("Enter the Itemp product_cost : "))
discount_per = int(input("Enter the discount percentage : "))
discount = product_cost * (discount_per)/100
print(f" Discount price - {discount}")
final_cost = product_cost - discount
print(f"product final cost is {final_cost}")

# 8. BMI Calculator
# formula: BMI = weight (kg) / (height (m))^2
weight =float(input("Enter Weight : "))
height = float(input("Enter Height"))
bmi = weight/height**2
print(bmi)








