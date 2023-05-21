
def sum(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum

def max_sum(a):
    """
    for all starts
        for all ends
            sum up array
            if better than current
                update current
    """
    max = -999999
    for i in range(len(a)):
        for j in range(len(a) + 1): # maybe need to be len(a) + 1
            sub_array = a[i:j]
            sum = sum(sub_array)
            if sum > max:
                max = sum
    return max
    

a = [1,4,-5,7,3]
print(max_sum(a))