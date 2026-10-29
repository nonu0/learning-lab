# numbers = [5,1,9,3,7,10, 100]
# numbers = [-10, -5, -20]
numbers = [42]


def largest_number(numbers: list) -> int:     
    num = numbers[0]
    for i in numbers:
        if i > num:
            # print(i)
            num = i
    return num

    
ans = largest_number(numbers)
print(ans)