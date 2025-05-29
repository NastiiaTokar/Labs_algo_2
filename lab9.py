def sqrt(x):
    l = 0.0
    r = x
    for _ in range(100):
        m = (l + r) / 2
        if m * m > x:
            r = m
        else:
            l = m
    return l

def hypot(a, b):
    return sqrt(a * a + b * b)

def max_wire_length(w, heights):
    n = 0
    while n < len(heights):
        if heights[n] < 1:
            heights[n] = 1
        n += 1
        
    dp = []
    for i in range(len(heights)):
        dp.append([0.0] * heights[i])

    for i in range(1, len(heights)):
        for h2 in range(1, heights[i] + 1):  
            max_val = 0.0
            for j in range(1, heights[i - 1] + 1):  
                prev = dp[i - 1][j - 1] 
                d = hypot(w, h2 - j)    
                val = prev + d
                if val > max_val:
                    max_val = val
            dp[i][h2 - 1] = max_val

    max_total = 0.0
    k = 0
    while k < len(dp[-1]):
        if dp[-1][k] > max_total:
            max_total = dp[-1][k]
        k += 1
    return max_total
