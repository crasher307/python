# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def load(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    return data


def save(file, mess):
    with open(file, 'w+', encoding='utf-8') as f:
        f.write(mess)


def basicEncode(fIn, fOut=None):
    mess = load(fIn)
    itemAdd = lambda d, c: d.append({'c': c, 'count': 1})
    data = []
    itemAdd(data, mess[0])
    for i in range(1, len(mess)):
        dNum = len(data) - 1
        if mess[i] == data[dNum]['c'] and data[dNum]['count'] < 9:
            data[dNum]['count'] += 1
        else:
            itemAdd(data, mess[i])
    res = ''.join([f'{i["count"]}{i["c"]}' for i in data])
    if fOut is not None:
        save(fOut, res)
    return res


def basicDecode(fIn, fOut=None):
    mess = load(fIn)
    res = ''.join([
        i['c'] * int(i['count'])
        for i in [
            {'c': mess[i + 1], 'count': mess[i]}
            for i in range(0, len(mess), 2)
        ]
    ])
    if fOut is not None:
        save(fOut, res)
    return res


print(basicEncode('dataIn.txt', 'dataOut.txt'))
# print(basicDecode('dataIn.txt', 'dataOut.txt'))
