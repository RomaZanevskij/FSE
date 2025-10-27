import random
import time

correct = 0
total_time = 0
times = []

count = int(input("Введите количество примеров: "))

for i in range(1, count + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    result = a * b

    print(f"\nВопрос {i}/{count}")
    while True:
        start = time.time()
        user_input = input(f"{a} * {b} = ")
        end = time.time()

        try:
            answer = int(user_input)
            elapsed = round(end - start, 1)
            times.append(elapsed)
            total_time += elapsed

            if answer == result:
                print(f"Верно! (Время: {elapsed} сек)")
                correct += 1
            else:
                print(f"Неверно! Правильно: {result} (Время: {elapsed} сек)")
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

print("=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)
print(f"Общее время: {round(total_time, 1)} секунд")
print(f"Среднее время на вопрос: {round(total_time / count, 1)} сек")
print(f"Правильных ответов: {correct}/{count}")
accuracy = round((correct / count) * 100, 1)
print(f"Процент правильных: {accuracy}%")
