# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}

my_dict = {'name': 'python', 
           'age': 25}
print(my_dict)
my_dict.update({'city' : 'East Godavari'})
print(my_dict)
print ("-"*75)
print("\n")

# Write Python code to access and print the value associated with the key 'price' in the following dictionary:
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}

product_info = {'name': 'Laptop', 
                'brand': 'Dell', 
                'price': 1200}
print("orginal Dictionary ", product_info)
print(" Result for getting price key", product_info['price'])
print ("-"*75)
print("\n")


# Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}

my_dict = {'name': 'python',
           'age': 30, 
           'city': 'Bhimavaram'}
print("My Set is ", my_dict)
my_dict.pop("city")
print(my_dict)
print ("-"*75)
print("\n")


# Write Python code to print all the keys present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}

my_dict = {'name': 'python', 
           'age': 25, 
           'city': 'Rajahmundry'}
print("Orginal Data :", my_dict)
print(my_dict.keys())
print ("-"*75)
print("\n")


# Write Python code to print all the values present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}

my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print("Orginal Data :", my_dict)
print(my_dict.values())
print ("-"*75)
print("\n")


# Write a Python script that updates a dictionary with a new key-value pair.

my_dict = {'name': 'Rishi', 
           'age': 17}
my_dict.update({'study': 10})
print("updated dictionary is:",my_dict)
print("\n")


# Write a Python script that accesses and prints the value associated with a specific key in a dictionary.

my_dict = {'name': 'Indira', 
           'age': 35,
           'emp_id':333,
           'branch':'East Godavari'}
print("original Dictionary",my_dict)
print("printing specific key valuce : employee id : ", my_dict['emp_id'])
print ("-"*75)
print("\n")

# Write a Python script that removes a key-value pair from a dictionary

my_dict = {'name': 'Indira', 
           'age': 35,
           'emp_id':333,
           'branch':'East Godavari'}
print("original Dictionary",my_dict)

print("printing after removing a key-value pair : employee id : ", my_dict.pop('emp_id'))
print ("-"*75)
print("\n")


# Write a Python script that prints all the keys present in a dictionary.

my_dict = {'name': 'Indira', 
           'age': 35,
           'emp_id':333,
           'branch':'East Godavari'}
print("original Dictionary",my_dict)
print(my_dict.keys())
print ("-"*75)
print("\n")


# Write a Python script that prints all the values present in a dictionary.

my_dict = {'name': 'Indira', 
           'age': 35,
           'emp_id':333,
           'branch':'East Godavari'}
print("original Dictionary",my_dict)
print(my_dict.values())
print ("-"*75)
print("\n")

