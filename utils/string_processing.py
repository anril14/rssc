from soupsieve.util import lower


def string_processing(raw: str) -> (list, str):
    words = []
    useful = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'
    cur = ''
    for i, item in enumerate(raw):
        if item == ' ':
            for _ in cur:
                if lower(_) in useful:
                    words.append(cur)
                    cur = ''
                    break
            else:
                cur = ''
            continue
        cur = ''.join(cur + item)

    return words, ' '.join(words)
