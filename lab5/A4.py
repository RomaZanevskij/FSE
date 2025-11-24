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


def process_commands(commands_file, proteins, output_file, author_name):
    with open(commands_file, 'r', encoding='utf-8') as f, open(output_file, 'w', encoding='utf-8') as out:
        out.write(f"{author_name}\n")
        out.write("Genetic Searching\n")
        out.write("-" * 74 + "\n")

        op_num = 1
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split('\t')
            cmd = parts[0].lower()

            out.write(f"{op_num:03d}   {cmd}")

            if cmd == 'search':
                if len(parts) < 2:
                    out.write("   \n")
                    out.write("organism\t\t\t\tprotein \n")
                    out.write("NOT FOUND\n")
                else:
                    query = decode_rle(parts[1])
                    out.write(f"   {query} \n")
                    out.write("organism\t\t\t\tprotein \n")
                    found = False
                    for name, data in proteins.items():
                        if query in data['sequence']:
                            out.write(f"{data['organism']}\t\t{name}\n")
                            found = True
                    if not found:
                        out.write("NOT FOUND\n")
