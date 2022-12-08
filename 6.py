def N_Check():  # обработчик ошибки ввода числа N
    while True:
        try:
            N = int(input('Введите кол-во признаков сравнения: '))
            return N
        except ValueError:
            print("Нужно ввести цифру!")

N = N_Check()
a = [0] * N
results = [0] * N
det = 0
i = 0
weight = 0
for i in range(N):
    a[i] = [0] * N
for j in range (N): #цикл для создания матрицы
    for i in range (N):
        if i == j:
            a[i][j] = 1
        elif j < i:
            weight = int(input('Введите на сколько признак ' + str(j + 1) + ' важнее признака ' + str(i + 1) + ': '))
            a[i][j] = weight
        elif j > i:
            a[i][j] = 1/weight

        results[j] += a[i][j]
        det += a[i][j]
for i in range(N): #цикл для расчёта ответов
    print ('Весовые коэффиценты: ' + str("%.2f" % (results[i]/det)))