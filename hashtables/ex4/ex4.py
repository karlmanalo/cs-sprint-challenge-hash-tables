def has_negatives(a):
    
    # Instantiate empty cache and result list
    cache = {}
    result = []

    """
    For each element in a, we cache a key:value pair of element:1 if 
    the key i does not yet exist in the cache. After adding element i
    to the cache, we check to see if -i exists in the cache (with the
    additional conditional that i != 0). If both of these conditions 
    are met, we append i to our result list. Runs in O(n) time.
    """
    
    for i in a:
        if i not in cache:
            cache[i] = 1
            if -i in cache and i != 0:
                result.append(abs(i))
            
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
