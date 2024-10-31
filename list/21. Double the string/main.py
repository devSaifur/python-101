def double_string(sentence):
    words = sentence.split(" ")

    doubled_sentences = []

    # doubling the words
    for i in range(0, len(words)):
        double_words = []
        doubled_sentences.insert(i, double_words)
        for latter in words[i]:
            double_word = "".join(latter) + "".join(latter)
            double_words.append(double_word)

    full_sentence = []

    # joining all together
    for sentence in doubled_sentences:
        full_sentence.append("".join(sentence))

    string = "  ".join(full_sentence)

    return string
