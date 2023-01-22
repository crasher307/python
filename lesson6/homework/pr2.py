# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

def check(f, v):
    try:
        f(v)
        return True
    except ValueError:
        return False


lst = ('a', 'b', '2', '3', 'c')
n = list(filter(lambda x: check(int, x), lst))
s = list(filter(lambda x: x not in n, lst))

print(f'Буквы:\t{s}\nЦифры:\t{n}')
