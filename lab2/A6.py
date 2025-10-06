sec = int(input("Введите количество секунд с начала суток: "))

hours = (sec // 3600) % 24
minutes = (sec % 3600) // 60
seconds = sec % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")