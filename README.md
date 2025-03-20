# python_code
Required Functions:
• my_info():
o Parameters: None.
o Functionality: This function should return a list containing your personal information in
the following order:
▪ Your student ID.
▪ Your first name.
▪ Your last name.
o Example: my_info() should return something like [123456, "John", "Doe"]. (Replace this
example with your actual student ID and name.)
• get_number_list(n):
o Parameters: This function accepts a single parameter n, which indicates how many
numbers the function will read from the user.
o Functionality:
▪ It should prompt the user to input n positive integers.
▪ The function will then create a list of these numbers and return it.
o Input Constraints:
▪ Only positive integers should be considered valid inputs. You can assume users
will provide valid inputs for the sake of simplicity (no error handling required for
input validation in this function).
• process_number_list(num_list, k):
o Parameters: This function takes two parameters:
▪ num_list - a list of numbers (integers).
▪ k - an integer specifying which element from the start and end of the sorted list
should be considered as the k-th largest and smallest number.
o Functionality:
▪ The function should return a list containing the k-th largest and k-th smallest
number from the list.
▪ If k is out of bounds (greater than the length of the list, or non-positive), the
function should return None.
▪ If the list contains duplicate values, the function must treat them as if they only
appeared once. That is, it should behave as if the list contains only unique
values.
▪ Negative numbers and zero in the list should also be considered as out-of-
bounds conditions, and the function should return None if they exist.
o Edge Cases:
▪ The function should handle scenarios where the list is too small or the value of k
is too large or non-positive by returning None.
▪ Example: If k = 3 but the list contains only 2 distinct elements, the function
should return None.
