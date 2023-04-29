from django import template

register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются :(

@register.filter(name='censor')
def Censor(value):
    Banned_List = ['сука', 'дурак', 'тупой', 'мудак']
    sentence = value.split()
    for i in Banned_List:
        for words in sentence:
            if i in words:
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))
    return " ".join(sentence)