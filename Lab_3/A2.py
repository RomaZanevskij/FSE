import string
password = input("Введите пароль: ")

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
errors = []

if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if password == password.lower():
    errors.append("В пароле отсутствуют заглавные буквы")
if password == password.upper():
    errors.append("В пароле отсутствуют строчные буквы")
if not any(c in '*-#' for c in password):
    errors.append("В пароле отсутствуют специальные символы")
if not any(c in string.digits for c in password):
    errors.append("В пароле отсутствуют цифры")
if any(c not in allowed for c in password):
    errors.append("В пароле используются непредусмотренные символы")

if not errors:
    print("Надежный пароль")
else:
    print("Ошибки:")
    for err in errors:
        print("-", err)
