def evens(num_list):
    """
    the function gets a list of numbers and returns a sorted list of the even nums in it.
    :param num_list: a given list of numbers
    :type num_list: list
    :return sorted_list: a list of only the even numbers, sorted from big to small.
    :rtype sortes_list: list
    """
    sorted_list = []
    for n in num_list:
        if n % 2 == 0:
            sorted_list.append(n)
    return sorted(sorted_list, reverse=True)


print(evens([13, 15, 56, 148, 24, 48, 2, 57, 94, 77]))
