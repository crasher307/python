# на входе такой список a = [4, 3, -10, 1, 7, 12], получить такой [4, -10, 12, 3, 1, 7]

base = [4, 3, -10, 1, 7, 12]

srt = lambda x: x % 2
res = base.copy()
res.sort(key=srt)

print(f'base:\t{base}\nresult:\t{res}')
