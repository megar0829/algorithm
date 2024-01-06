binary1, binary2 = input().split()
print(bin(int(binary1, 2) + int(binary2, 2))[2:])