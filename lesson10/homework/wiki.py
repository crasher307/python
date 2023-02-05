import re
import wikipedia

wikipedia.set_lang("ru")


def getInfo(word):
    try:
        response = ''
        text = ' '.join(str(wikipedia.page(word).content[:1000]).split()[:-2]).split('.')[:-1]
        for x in text:
            response += f'{x}.' if '==' not in x and len((x.strip())) > 3 else ''
        response = re.sub('\([^()]*\)', '', response)
        response = re.sub('\([^()]*\)', '', response)
        response = re.sub('\{[^\{\}]*\}', '', response)
        response += '...'
        return response
    except Exception:
        return 'В энциклопедии нет информации об этом'
