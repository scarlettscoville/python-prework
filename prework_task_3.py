# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input
# of the function.
def hello_name(user_name):
    print(f"Hello, {user_name.title()}!")
hello_name('scarlett')


# Question 2
# Write a python function, first_odds that prints the odd
# numbers from 1-100 and returns nothing.
def first_odds():
    odds = list(range(1,101,2))
    print(odds)

first_odds()

# Question 3
# Write a Python function, max_num_in_list to return the 
# max number of a given list.
def max_num_in_list(a_list):
    print(max(a_list))

max_num_in_list([9, 10, 11, 12, 13])

# Question 4
# Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    print(a_year % 4 == 0 or a_year % 100 != 0 and a_year % 400 == 0)

is_leap_year(2022)        
is_leap_year(2024)

# Question 5
# Write a function to check to see if all numbers in the list are consecutive
# numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers.
def is_consecutive(a_list):
    print(sorted(a_list) == list(range(min(a_list), max(a_list) + 1)))

is_consecutive([1,2,4,3,5])

    