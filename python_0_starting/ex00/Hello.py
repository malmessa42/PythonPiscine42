ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"

tmp_list = list(ft_tuple)
tmp_list[1] = "UAE!"
ft_tuple = tuple(tmp_list)

ft_set.remove("tutu!")
ft_set = list(ft_set) #because set is unordered!
ft_set.append("Abu Dhabi!")

ft_dict["Hello"] = "42AD!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)