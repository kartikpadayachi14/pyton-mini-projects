import string

sentence = input("Enter text: ")
sentence = sentence.lower()

for ch in string.punctuation:
    sentence = sentence.replace(ch, "")

words = sentence.split()
print("Words:", len(words))
print("Unique:", set(words))

freq = {}
for w in words:
    freq[w] = freq.get(w,0)+1
    print("Grequency:",freq)
