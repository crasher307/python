# Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

lst = ("a", 'b', '2', '3', 'c')

res = dict()
for x in lst:
    try:
        float(x)
        key = 'num'
    except ValueError:
        key = 'str'

    if key not in res:
        res.setdefault(key, list())

    res[key].append(x)

print(f'lst: {lst}\nres: {res}')
