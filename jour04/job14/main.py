def my_long_word(length, input_str):
    words = []
    current_word = ''

    for char in input_str + ' ':
        if char != ' ':
            current_word += char
        else:
            if len(current_word) > length:
                words.append(current_word)
            current_word = ''

    return ' '.join(words)

result = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

print("Output :", result)
