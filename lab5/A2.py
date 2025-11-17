def main():
    text = input("Введите текст: ")

    sentence = ""
    sentences = []

    for ch in text:
        sentence += ch
        if ch in ".!?":   # конец предложения
            sentences.append(sentence.strip())
            sentence = ""

    # выводим каждое предложение
    for s in sentences:
        print(s)

    print("Предложений в тексте:", len(sentences))

main()
