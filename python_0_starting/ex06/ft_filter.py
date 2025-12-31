def ft_filter(func, iter):

    """
    Filters elements of the iterable based on the given function.

    Parameters:
    - func (function or None): A function that returns a boolean value.
        If None, filters out falsy elements.
    - iter (iterable): The iterable to be filtered.

    Returns:
    - An iterator yielding elements for which func(i) is True,
        or truthy elements if func is None.
    """

    return (i for i in iter if i) if func is \
        None else (i for i in iter if func(i))
    # if func is None:
    #     return (i for i in iter if i)
    # else:
    #     return (i for i in iter if func(i))

# Ex 1:
# lstx = [1, 2, 0, -2, -5, 0, None]
# tmp = ft_filter(None, lstx)
# tmp2 = filter(None, lstx)
# print (list(tmp))
# print (list(tmp2))

# Ex 2:
# strings = ["hello", "", "world", "", "python"]
# non_empty = filter(None, strings)
# print(list(non_empty))  # ['hello', 'world', 'python']
# non_empty2 = ft_filter(None, strings)
# print(list(non_empty2))  # ['hello', 'world', 'python']

# Ex 3:
# mixed = "abc123def456"
# digits = filter(str.isdigit, mixed)
# print(''.join(digits))  # 123456
# digits2 = ft_filter(str.isdigit, mixed)
# print(''.join(digits2))  # 123456

# Ex 4:
# s = "PyThOn"
# uppercase = filter(str.isupper, s)
# print(''.join(uppercase))  # PTO
# uppercase2 = ft_filter(str.isupper, s)
# print(''.join(uppercase2))  # PTO
