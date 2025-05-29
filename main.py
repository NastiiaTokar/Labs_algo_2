from lab7 import boyer_moore_search

with open("student_work.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

meaningless_words = [
    "Таким чином", 
    "типу", 
    "Взагалі", 
    "в цілому", 
    "на мій погляд"
    ]

for idx, line in enumerate(lines, 1):
    line_lower = line.lower()

    for word in meaningless_words:
        word_lower = word.lower()

        positions = boyer_moore_search(line_lower, word_lower)

        if positions:
            print(f"Знайдено '{word}' у рядку {idx}")