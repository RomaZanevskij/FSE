def decode_rle(rle):
    result = ''
    i = 0
    while i < len(rle):
        if rle[i].isdigit() and i + 1 < len(rle):
            count = int(rle[i])
            i += 1
            result += rle[i] * count
        else:
            result += rle[i]
        i += 1
    return result


def load_sequences(filename):
    proteins = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('\t')
                if len(parts) < 3:
                    continue
                name, organism, rle_seq = parts[0], parts[1], '\t'.join(parts[2:])
                decoded = decode_rle(rle_seq)
                proteins[name] = {'organism': organism, 'sequence': decoded}
    except FileNotFoundError:
        print(f"Файл {filename} не найден!")
        return {}
    return proteins
