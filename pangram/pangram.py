def is_pangram(sentence):
    '''
    sentence: string, phrase to be tested
    returns: True if sentence is a pangram, otherwise False
    '''
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z'}
    sentence_chars = {char for char in sentence.lower() if char in alphabet}
    if sentence_chars == alphabet:
        return True
    return False
