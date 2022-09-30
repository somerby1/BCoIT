import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        return float(coef_str)
    except:
        while True:
            try:
                # Вводим с клавиатуры
                print(prompt)
                coef_str = input()
                #Проверяем равен ли коэффициент при квадрате нулю
                if coef_str == "0" and index == 1: print(1/0)
                return float(coef_str)
            except:
                print("Неправильный ввод коэффициента, повторите попытку ввода.") 

def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        set[float]: Список корней
    '''
    result = set()
    D = b * b - 4 * a * c
    sqD = math.sqrt(D)
    root1 = (-b + sqD) / (2.0 * a)
    root2 = (-b - sqD) / (2.0 * a)
    result.add(root1)
    result.add(root2)
    return result

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: ')
        for i in roots:
            print(i)
    elif len_roots == 2:
        print('Два корня: ')
        for i in roots:
            print(i)
            
# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
