def intersection(arrays):
    # Instantiate an empty cache and result list
    cache = {}
    result = []

    """
    Create a cache that counts the number of instances of each element.
    If the number of instances of a particular element is equal to the
    number of lists, that means that element exists in every list.
    Append that element to the result list, and continue iterating
    until you've reached the end of your domain. Return the result.
    
    NOTE:
    This solution assumes that all elements in each nested list are
    unique. Not sure how to refactor this code to handle duplicates
    within a list. This solution feels like it's in the spirit of what
    we've learned this week, but if each nested list is supposed to be 
    made up of unique elements, a key piece of information is missing
    from the problem statement. I imagine a solution that handles 
    non-sets would be a bit more complicated.
    """

    for lst in arrays:
        for value in lst:
            if value not in cache:
                cache[value] = 1
            else:
                cache[value] += 1

    # Define the number of lists as the length of arrays
    num_lists = len(arrays)

    """
    If the counter for a key is equal to the number of lists, append 
    that key to result.
    """
    
    for key, value in cache.items():
        if value == num_lists:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
