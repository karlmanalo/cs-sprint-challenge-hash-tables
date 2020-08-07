def get_indices_of_item_weights(weights, length, limit):
    # Instantiate an empty cache and result list
    cache = {}
    result = []

    """
    Create a cache where the keys are the weights and the values are
    the index values. Create these index values as lists to handle
    duplicate keys.
    """

    for index, weight in enumerate(weights):
        if weight not in cache:
            cache[weight] = [index]
        else:
            cache[weight].append(index)

    """
    Iterate through each weight (weight_1) in our list. If limit - weight_1 
    (weight_2) exists in our cache, we need to return the index values of
    both weight_1 and weight_2. Return a tuple of indices, where the first
    index is the "higher" index, numerically speaking. Because the values
    in our cache were stored as lists (even if they are 1 element long),
    we must call max/min on these lists to return an index, and again call
    max/min on the resulting tuples to find our result.
    """  

    for index, weight in enumerate(weights):
        if limit - weight in cache:
            return (max(index, max(cache[limit - weight])), min(index, min(cache[limit - weight])))

    return None
