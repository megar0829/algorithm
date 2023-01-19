clas_dict = {}
A = 4
for i in ['A', 'B', 'C', 'D', 'F']:
    clas_sum = 0.3
    if i == 'F':
        clas_dict[i] = 0.0
    else:
        for j in ['+', '0', '-']:
            clas_dict[i+j] = A + clas_sum
            clas_sum -= 0.3
    A -= 1
C_lang = input()
print(clas_dict[C_lang])