import re
def create_matr_list_from_faile(faile)->list:
    matrix = []

    with open(faile, "r") as f:
        for line in f.readlines():
            matrix_2 = []
            line = re.sub("\n", "", line)
            for s in line:
                matrix_2.append(int(s))
            matrix.append(matrix_2)
    return matrix
print(create_matr_list_from_faile("faile.txt"))

def check(a: int, b: int, ground: list, a_max: int, b_max: int) -> list:
    """ Проверка кратера.
        : param a: координата кратера
        : param b: координата кратера
        : param ground: снимок луны
        : param a_max: максимальный размер а
        : param b_max: мфксимальный размер b
        : return: фото кратера
       """
    ground [a][b] = 'a'
    if a + 1 < a_max:
        el = ground[a + 1] [b]
        if  el == '1':
            ground [a + 1][b] = 'a'
            check(a +1, b, ground, a_max, b_max)
    if b + 1 < b_max:
        el = ground[a][b + 1]
        if el == '1':
            ground[a][b +1] = 'a'
            check(a, b + 1, a_max, b_max)
    if a - 1 > -1:
        el = ground[a - 1] [b]
        if el == '1':
            ground[a - 1][b] = 'a'
            check(a - 1, b, ground, a_max, b_max)
    if b - 1 > -1:
        el = ground [a][b - 1]
        if el == '1':
            ground[a][b - 1] = 'a'
            check(a, b - 1, ground, a_max, b_max)
    return  ground

def calculater(ground: list) -> int:
    """Количество кратеровю
    : param ground: снимок луны
    : return: количество кратеров"""
    count = 0
    line_max = len(ground)
    colum_max = len(ground[0])
    for a in range (line_max):
        for b in range(colum_max):
            el = ground[a][b]
            if el == '1':
                ground = check(a, b, ground, line_max, colum_max)
                count += 1
    return  count
print(calculater(create_matr_list_from_faile('faile.txt')))
