def finder(files, queries):
   
    # Instantiate an empty cache and result list
    cache = {}
    result = []


    """
    To create our cache, we must first figure out what the most
    appropriate key would be. Since the queries are filenames, our goal
    will be to create a cache where the keys are filenames and the
    values are lists of complete filepaths with those filenames. To 
    access the filenames from the filepaths, we utilize the .rsplit()
    method, where we define the character / as our delimiter and only
    split once (starting from the right). Now that we have our filename,
    we can begin building our cache with this filename as our key. If
    the filename does not yet exist in our cache, we define the value
    in our cache to be a 1-element list containing the full filepath.
    If the filename does exist in our cache, we append the filepath to
    the existing list at that key in the cache.
    """
    for f in files:
        key = f.rsplit("/", 1)[-1]
        if key not in cache:
            cache[key] = [f]
        else:
            cache[key].append(f)
    
    """
    Now it's a simple matter of checking our cache for each of the 
    queries. If the filename in queries exists in our cache, we extend
    our result list with the list that exists at that filename's value
    in the cache.
    """
    for q in queries:
        if q in cache:
            result.extend(cache[q])

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
