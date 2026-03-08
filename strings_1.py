# 1. You are given a string sentence . Print the characters at even indices
# sentence = "Python is amazing"

sentence = "python is amazing"
sentence1 = sentence[::2]
print(sentence1)


# 2.   You are given a string s . Replace all spaces in the string with underscores ( _ ) and print the modified string.
# s = "Python is fun and powerful"

s = "Python is fun and powerful"
replace_s = s.replace(" ","_")
print(s)
print(f"after replacing '_' :     ",replace_s)


# 3. You are given a string s . Check if the string contains only digits.

s= "891011"
print(s)
digit_s = s.isdigit()
print("finding given a string contains only digits   :  ",digit_s)


# 4. You are given a string s . Print the string in reverse order.
# s = "Python is amazing"

s = "Python is amazing"
print(s)
s_rev = s[::-1]
print("After reversing the string :  ", s_rev)


# You are given a string s . Capitalize the first letter of each word in the string and print the modified string.
# s = "python programming is fun"

s = "python programming is fun"
capatilized_s = s.title()
print("After capitalizing text : ", capatilized_s)









