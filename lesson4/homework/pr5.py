# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

files = ['pr5-1.log', 'pr5-2.log']
poly = []
for file in files:
    f = open(file, 'r')
    poly.append(f.readline().rstrip().split(' = '))
    f.close()

res = {}
for data in poly:
    tmp = data[0].split(' + ')
    if 'sum' not in res:
        res.setdefault('sum', int(data[1]))
    else:
        res['sum'] += int(data[1])
    for t in tmp:
        pos = t.find('x')
        key = t[pos::] if pos > 0 else 'num'
        value = t[:pos:] if pos > 0 else t
        if key not in res:
            res.setdefault(key, int(value))
        else:
            res[key] += int(value)
    print(f'{tmp} = {data[1]}')

res['num'] -= res.pop('sum')
res = ' + '.join([f'{res[key]}{key if key != "num" else ""}' for key in res]) + ' = 0'

print(f'{res}')

f = open('pr5.log', 'w')
f.write(f'{res}\n')
f.close()
