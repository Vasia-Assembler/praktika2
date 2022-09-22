from typing import List


def lengths_product(words: List[str]) -> List[int]:
    """Элементы списка – кол-во букв 'm' в каждом слове (по порядку),
    умноженное на 4, если последняя буква слова
    находится в диапазоне от 'b' до 'p'"""
    return list(map(lambda x: (ord('b') <= ord(x[len(x) - 1]) <= ord('p')) and len(x) * 4 or len(x), words))


def words_lengths(words: List[str]) -> List[int]:
    """Элементы списка – длины слов из списка words,
    в которых четное кол-во букв"""
    return list(filter(lambda x: x is not None, list(map(lambda x: (len(x) % 2 == 0) and len(x) or None, words))))


def alphabetical(words: List[str]) -> List[str]:
    """Элементы списка – последовательности в алфавитном порядке
    из всех букв слов списка words, кроме 'm'"""
    all_characters = set()
    for w in words:
        for n in w:
            all_characters.add(n)
    if 'm' in all_characters:
        all_characters.remove('m')
    sorted_characters = sorted(all_characters, key=str.lower)
    return list(sorted_characters)


if __name__ == "__main__":
    words_list = ["mammal", "mnemonic", "scam", "momentum", "memory", "mankind"]
    words_1 = lengths_product(words_list)
    words_2 = words_lengths(words_list)
    words_3 = alphabetical(words_list)

    print(words_list, words_1, words_2, words_3, sep="\n")