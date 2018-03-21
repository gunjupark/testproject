def square_of_sum(count):
    res = count*(count+1)/2
    return res**2

def sum_of_squares(count):
    res = 0
    for i in range(1,count+1):
        res += i**2
    return res

def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
