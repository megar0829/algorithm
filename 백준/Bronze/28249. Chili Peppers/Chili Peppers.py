price = {
    'Poblano': 1500,
    'Mirasol': 6000,
    'Serrano': 15500,
    'Cayenne': 40000,
    'Thai': 75000,
    'Habanero': 125000
}
N = int(input())
result = 0
people = [input() for _ in range(N)]
for i in people:
    result += price[i]
print(result)