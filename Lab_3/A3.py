prev = int(input("Введите предыдущее показание счётчика: "))
curr = int(input("Введите текущее показание счётчика: "))

used = curr - prev
total = 0

if used <= 300:
    total = 21
elif used <= 600:
    total = 21 + (used - 300) * 0.06
elif used <= 800:
    total = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    total = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

avg_price = total / used if used > 0 else 0

print(f"Объём потреблённого газа: {used} куб. м")
print(f"Сумма оплаты: {total:.2f} $")
print(f"Средняя цена за кубометр: {avg_price:.2f} $")

