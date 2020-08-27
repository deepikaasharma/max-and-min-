numbers = [1, 3, 4, 6, 2]
max_num = max(numbers)

print(max_num)


a = 30
n = 90

num_list = list(range(a, n))
print('max:', max(num_list))


numbers = [3, 1, 4, 6, 2]
min_num = min(numbers)

print(min_num)

a = 30
n = 90

num_list = list(range(a, n))
print('min: ', min(num_list))

multiple_min = [-1, 7, 3, 6, -1, 9, 10, -1]
print(min(multiple_min))


"""Max and Min Challenge

Given the following code, what would print to the console?

nums_lst = [3, 5, 1.9, 7.3]
print(max(nums_lst))

"""

nums_lst = [3, 5, 1.9, 7.3]
print(max(nums_lst))


"""Given the following code, what would print to the console?

lst = [-5, 13, 2, -4, 1, 0]
print(min(lst))

"""

lst = [-5, 13, 2, -4, 1, 0]
print(min(lst))


"""Complete the diff_max_min function below. This function takes a single parameter called digit_lst. This function should find the max of the list and the min of the list and and return the difference between them."""

def diff_max_min(digit_lst):
  mx = max(digit_lst)
  mn = min(digit_lst)
  return (mx - mn)

