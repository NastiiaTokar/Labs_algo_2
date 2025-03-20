def count_elements(arr): #рахує к-ть елементів у масиві
    count = 0
    for _ in arr:
        count += 1
    return count

def sum_elements(arr): #знаходить суму всіх елементів
    total = 0
    for num in arr:
        total += num
    return total

def max_elements(arr): #знаходить максимальний елемент у масиві
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        return max_val
    
def can_paint(boards, painters, max_time, paint_time): #перевіряє чи можна пофарбувати всі щити за мах time
    count = 1
    total_time = 0

    for i in range(count_elements(boards)):
        time_needed = boards[i] * paint_time

        if time_needed > max_time:
            return False
        
        if total_time + time_needed > max_time:
            count += 1
            total_time = time_needed

            if count > painters:
                return False
        else:
            total_time += time_needed

    return True


def min_time_to_paint(K, T, L):
    left = max_elements(L) * T
    right = sum_elements(L) * T

    while left < right:
        mid = (left + right) // 2

        if can_paint(L, K, T, mid):
            right = mid
        else:
            left = mid + 1


    return left
    

K = 5
T = 10
L = [15, 10, 5, 10, 15, 20, 20, 15, 20]

print(min_time_to_paint(K, T, L), "хвилин")