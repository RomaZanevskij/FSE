data = input("Введите пакеты данных: ")

zero_count = data.count("0")
one_count = data.count("1")
losses = zero_count/len(data) * 100 

if not all(char in '01' for char in data):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
else:

    if losses > 0 and losses < 1:
        state = "Отличное качество"
    elif losses > 1 and losses < 5:
        state = "Хорошее качество"
    elif losses > 5 and losses < 10:
        state = "Удовлетворитеьное качество"
    elif losses > 10 and losses < 20:
        state = "Плохое качество"
    else:
        state = "Критическое состояние сети"

    def max_zero(s):
        return len(max(s.split('1'), key = len))


    print(f"Общее количество пакетов: {len(data)}")
    print(f"Количество потерянных пакетов: {zero_count}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_zero(data)}")
    print(f"Процент потерь: {round(losses, 1)}%")
    print(f"Качество связи: {state}")

