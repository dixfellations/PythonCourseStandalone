text = " "
cleaned_text = []
for char in text.lower():
    if char.isalpha() or char == ' ':
        cleaned_text.append(char)
cleaned_text = ''.join(cleaned_text)
words = cleaned_text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
bigram_counts = {}
for i in range(len(words)-1):
    bigram = f"{words[i]} {words[i+1]}"
    bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1
trigram_counts = {}
for i in range(len(words)-2):
    trigram = f"{words[i]} {words[i+1]} {words[i+2]}"
    trigram_counts[trigram] = trigram_counts.get(trigram, 0) + 1
print("Слова:", ", ".join(f"{k}: {v}" for k, v in word_counts.items()))
print("Биграммы:", ", ".join(f"{k}: {v}" for k, v in bigram_counts.items()))
print("Триграммы:", ", ".join(f"{k}: {v}" for k, v in trigram_counts.items()))