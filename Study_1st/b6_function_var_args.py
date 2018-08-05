def total(initial=5, *numbers, **keywords):
    count =  initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10, 1, b=2, fruits = 3, vegetables=50, a=100))
