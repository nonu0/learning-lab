def frequency_map(numbers:list[int]) -> dict[int,int]:
    dict = {}
    for num in numbers:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    return dict

numbers = [1,2,5,2,3,4,6,4,3,7,0]

print(frequency_map(numbers))
