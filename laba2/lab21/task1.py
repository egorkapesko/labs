text = input("Введите текст: ")

text = text.lower()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

unique_words_count = len(word_count)

print("Количество каждого слова:")
for word, count in word_count.items():
    print(f"{word}: {count}")

print(f"\nКоличество уникальных слов: {unique_words_count}")
