# single_quote = "Hello"
# Double_quote = "World"
# triple_quote = """Multi-linestring"""

# print(triple_quote)

# text = "Python Programming"

# print(text[0])   # (First Character)
# print(text[-1])  # (last Character)
# print(text[0:6]) # (Slice 0 to 5)
# print(text[:6])  # (From start to 5)
# print(text[7:])  # (From 7 to end)

# name = " bob the builder "

# print(len(name))
# print(name.strip())
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.replace("bob", "min"))

message_1 = f"""Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable.
This makes Python perfect for beginner and experts alike"""

word = message_1.split()
words_count = len(word)
char_count = len(message_1)
sentence_count = message_1.count('.') + message_1.count('!') + message_1.count('?')


print(f"total word: {words_count}")
print(f"total Characters: {char_count}")
print(f"total sentence: {sentence_count}")
