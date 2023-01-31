numbers = [int(input()) for _ in range(10)]
dict_numbers = {}
for i in numbers:
    dict_numbers[i] = numbers.count(i) 
print(int(sum(numbers) / len(numbers)))
for k, v in dict_numbers.items():
    if v == max(dict_numbers.values()):
        print(k)