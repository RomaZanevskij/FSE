text = 'Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (()).'

def short(text):
    while True:
        left_position = text.find('(')
        right_position = text.find(')')
        if left_position == -1 or right_position == -1 or right_position < left_position:
            break
        text = text.replace(text[left_position:right_position + 1], '')
    return " ".join(text.split())

print('Исходный текст:', text)
print('Укороченый текст:', short(text))
