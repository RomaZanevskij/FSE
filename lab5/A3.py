def make_abbreviation():
    text = input("Введите текст: ")  
    words = text.split()            
    result = ""                      

    for w in words:
        if len(w) >= 3:               
            result += w[0].upper()   

    print("Аббревиатура:", result)

make_abbreviation()
