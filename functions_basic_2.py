def countdown(num):
    output = []
    for i in range(num, -1, -1):
        output.append(i)
    return output
print(countdown(5))

def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([1, 2])

def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(list):
    newList = []
    if len(list) < 2:
        return False
    for i in range(0, len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
    print(len(newList))
    return newList

print(values_greater_than_second([5,4,3,2,1,4]))
print(values_greater_than_second([3]))

def this_length_that_value(size, value):
    size_and_value = []
    for i in range(0, size):
        size_and_value.append(value)
    return size_and_value
    
    
print(this_length_that_value(4,7))
print(this_length_that_value(6,2))