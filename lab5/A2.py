def main():
    text = input("Введите текст: ")

    sentence = ""
    sentences = []

    for ch in text:
        sentence += ch
        if ch in ".!?": 
            sentences.append(sentence.strip())
            sentence = ""

    for s in sentences:
        print(s)

    print("Предложений в тексте:", len(sentences))

main()

