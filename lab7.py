def boyer_moore_search(haystack, needle):
    if not needle or not haystack:
        return []
    
    bad_char = {}
    for i in range(len(needle)):
        bad_char[needle[i]] = i
    
    result = []
    m = len(needle)
    n = len(haystack)
    s = 0  
    
    while s <= n - m:
        j = m - 1
        
        while j >= 0 and needle[j] == haystack[s + j]:
            j -= 1
            
        if j < 0:
            result.append(s)
            s += 1  

        else:
            s += max(1, j - bad_char.get(haystack[s + j], -1))
    
    return result

haystack = "та мама мила маму"
needle = "мама"

print(boyer_moore_search(haystack, needle))