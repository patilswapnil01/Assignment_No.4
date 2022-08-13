# Write a Python program to triple all numbers of a given list of integers. Use Python map.
sample_list = [1, 2, 3, 4, 5, 6, 7]
result = list(map(lambda x: x+x+x ,sample_list))
print(result)