from ft_package import count_in_list
from ft_package import sum_numbers

print("Count in list:")
print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0

print("Total in list:")
print(sum_numbers([1, 2, 3]))
