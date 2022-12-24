# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# Формат входных данных: В первой строке подаётся число n (n – количество холодильников). В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
# Формат выходных данных: Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

ref = [
    '230v895pa0359',
    'Axb9n74w6To0jpxbnw6',  # -
    '20bv1v0n1v',
    'qn0aqnnbt07noqn5b0q',  # -
    'zb7wn8bov8z',
    'qvob7oanton9vpn9v5qpn9v',  # -
    'qv7ob9ob7v9q',
    'q75vvjan7c4ToNkuk7tc4k',  # -
    '5vb7bvs8n',
    'w9Abn7lt3n9Obn7',  # -
    '6',
    '222anton456',
    'a1n1t1o1n1',
    '0000a0000n00t00000o000000n',
    'gylfole',
    'richard',
    'ant0n',
]
refFind = []


def check(code, find):
    st = ''
    for c in code:
        c = c.lower()
        if st == find:
            return True
        elif c == find[len(st)]:
            st += c
    return False


for ser in ref:
    if check(ser, 'anton'):
        refFind.append(ser)

print(f'Коды холодильников ({len(ref)}): {ref}\nКоды зараженных ({len(refFind)}): {refFind}')
