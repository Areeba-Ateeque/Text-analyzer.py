def text_analyzer(text):
    # Calculate number of characters
    num_characters = len(text)
    # Calculate number of words
    num_words = len(text.split())
    # Calculate number of sentences
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")
    print(f"Number of sentences: {num_sentences}")

# Get input from the user
user_input = input("Enter a string: ")
text_analyzer(user_input)
