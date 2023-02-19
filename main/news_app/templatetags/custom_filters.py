from django import template

register = template.Library()

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
STOP_LIST = {
    'Израиль.': 'И******.',
    'Израиля.': 'И******.',
    'Израиля': 'И******',
    'Израиль': 'И******',
    'США.': 'С**.',
    'США': 'С**',
}


@register.filter()
def currency(text_in):
    text_out = text_in[:].split()

    for i in text_out:

        for key, value in STOP_LIST.items():
            if key in text_out:
                index_word = text_out.index(key)
                text_out[index_word] = value

    text_out = ' '.join(text_out)

    return f'{text_out}'
