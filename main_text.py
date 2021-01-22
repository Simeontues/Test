from search_text import search_and_replace_text

text = "I`m learning Spanish now. It`s a beautiful leanguage. l want to visit Spain one day"
sentence = input("Enter a word to search: ")
text = search_and_replace_text(sentence, text)
print(text)
