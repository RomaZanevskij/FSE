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