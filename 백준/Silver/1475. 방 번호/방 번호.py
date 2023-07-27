room_numbers = [0 for _ in range(10)]
N = list(map(int, input()))
for i in N:
    room_numbers[i] += 1
if room_numbers.index(max(room_numbers)) == 6 or room_numbers.index(max(room_numbers)) == 9:
    room_numbers[6] = round(((room_numbers[6] + room_numbers[9]) / 2) + 0.00000001)
    room_numbers.pop()
    print(max(room_numbers))
else:
    print(max(room_numbers))

