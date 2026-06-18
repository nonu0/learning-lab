

def count_occurence(numbers:list[int],target:int) -> int:
    sim = 0
    for num in numbers:
        if num == target:
            sim += 1
    return(sim)

print(count_occurence([5,2,5,3,5],5))