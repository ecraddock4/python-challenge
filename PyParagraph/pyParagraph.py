import os


# Read file

paragraph_one = os.path.join('paragraph_1.txt')



# Initialize
with open(paragraph_one, newline='') as file:
    #print(file.read())

    print('Paragraph Analysis')
    print('============================')

    text = file.read()
    words = text.split(' ')

    word_count = len(words)
    print("Approximate Word Count: " + str(word_count))
    

    sentence_split = text.split('. ')
    sentence_count = len(sentence_split)
    print("Approximate Senctence Count: " + str(sentence_count))

    letter_sum = 0

    # Average letter count
    for word in words:
        word_length = len(word)
        letter_sum = word_length + letter_sum
        
    print('Letter Sum: ' + str(letter_sum))


    # Average Sentence Length

    sentence_length = word_count / sentence_count
    print('Average Sentence Length: ' + str(sentence_length))