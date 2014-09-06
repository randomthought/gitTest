def border(text):
    borders = '*' * len(text)
    print borders
    print text
    print borders

text_input = raw_input("Enter text: ")
border(text_input)

