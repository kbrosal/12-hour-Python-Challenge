def word_occurrence(sentence, word):
    # Removing punctuation and making the sentence lowercase
    cleaned_sentence = ''.join(char for char in sentence if char.isalnum() 
                            or char.isspace()).lower()

    # Splitting the sentence into words
    words = cleaned_sentence.split()

    # Counting the occurrences of the word
    count = words.count(word.lower())

    return count

example_sentence = "This is a test sentence. This sentence is just a test."
example_word = "This"
print(word_occurrence(example_sentence, example_word))



