count = 0
vowels = ['a','e','i','o','u']

# def count_vowels(text: str):
#     for i in enumerate(text):
#         if i in vowels:
#             count.append(i)
#     return count


# print(ans)

# for i in ('hello'):
#     if i in vowels:
#         count.append(i)
#     print(count)


def count_vowels(text: str) -> int:
    count = 0
    for letter in text:
        if letter.lower() in vowels:
            count += 1
    return count

ans = count_vowels('HELLO')
print(ans)