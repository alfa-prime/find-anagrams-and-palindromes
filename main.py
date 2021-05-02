from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(f"Время исполнения функции {func.__name__}() : {datetime.now() - start}")
        return result
    return wrapper

@timeit
def get_words():
    source = 'data/russian_nouns.txt'
    with open(source, encoding='utf-8') as file:
        result = [word.strip() for word in file.readlines()]
    return result

@timeit
def find_palindromes(data):
    return [word for word in data if word == word[::-1]]

@timeit
def find_anagrams(data):
    result = {}
    for word in data:
        key = ''.join(sorted(word))
        if key in result:
            result[key].append(word)
        else:
            result[key] = [word]
    return [values for values in result.values() if len(values) > 1]


if __name__ == '__main__':
    words = get_words()

    palindromes = find_palindromes(words)
    with open('palindromes.txt', 'w', encoding='utf-8') as file:
        for item in palindromes:
            file.write(f"{item}, \n")

    anagrams = find_anagrams(words)
    with open('anagrams.txt', 'w', encoding='utf-8') as file:
        for item in anagrams:
            file.write(f"{', '.join(item)}\n")
