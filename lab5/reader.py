import re
def sort_key(word):
    # Перевіряємо, чи слово починається з української літери
    if re.match(r'^[А-Яа-яЇїІіЄєҐґ]', word):
        return (0, word.lower())  # Українські літери мають найвищий пріоритет
    else:
        return (1, word.lower())  # Латинські літери мають нижчий пріоритет

def sort_count(sentences):
    number=0
    allwords=[]
    for sentence in sentences:
        words = re.split(r'[^\w\'-]+', sentence)
        if words and words[-1] == '':
            words.pop()
        number += len(words)
        for word in words:
            allwords.append(word)
    allwords.sort(key=sort_key)
    print(f"Відсортований список - {allwords}")
    return number


def read_my_file(file):
    with open(file) as file:
        text = file.read()
        sentences = re.split(r'(?<!\w\.\w.)(?<![А-ЯA-Z][а-яa-z]\.)(?<=\.|\?|!)\s', text)
        cleaned_sentences = [sentence.replace('\n', ' ').strip() for sentence in sentences]
        print(f"1 речення - {cleaned_sentences[0]}")
        countw= sort_count(cleaned_sentences)
        print(f"Слів - {countw}")
    file.close()



read_my_file("text.txt")