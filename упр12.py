import sys
def moon_weight():
    print('Введите ваш нынешний земной вес')
    weight =int(sys.stdin.readline())
    print('Введите ежегодный прирост вашего веса')
    i =int(sys.stdin.readline())
    print('Введите количество лет')
    age =int(sys.stdin.readline())
    moon = weight * 0.165
    for year in range(0, age):
       print(moon)
       moon=moon+i
moon_weight()
