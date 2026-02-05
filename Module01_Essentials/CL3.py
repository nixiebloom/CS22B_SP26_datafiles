### This template is for the class exercises covered in M01_L03_review-objects for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### CL3.1: List comprehension. Given:
NL = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## Write a list comprehension to collect the diagonal items from matrix NL
# ** your code **
diag = [NL[i][i]for i in range(len(NL))]
print(diag)

##### CL3.2: Using my_list, create a list of tuples where tuple is (n, n**3) where n is each number in the list.
dia_list = [1, 2, 3, 4, 5]
# ** your code **
power3 =[(n, n**3) for n in dia_list]
print(power3)


##### CL3.3: Multiple all the values of the items in a dictionary 
num_dict = {'num1':100, 'num2':346, 'num3':-24}
# ** your code **
mult100 = 