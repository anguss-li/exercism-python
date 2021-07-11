from itertools import cycle
from random import choices
from string import ascii_lowercase as alphabet


class Cipher:
    def __init__(self, key: str = None):
        '''Encode text strings using a shift cypher using key'''
        self.key = ''.join(choices(alphabet, k=100)) if not key else key

    def encode(self, text: str) -> str:
        '''Shift letters in text by distance of corresponding letter in key'''
        encoded_text = ''
        for letter, key in zip(text, cycle(self.key)):
            distance = alphabet.find(letter) + alphabet.find(key)
            if distance > 25:
                distance -= 26
            encoded_text += alphabet[distance]
        return encoded_text

    def decode(self, text: str) -> str:
        '''
        Shift letters in text back by distance of corresponding letter in key
        '''
        decoded_text = ''
        for letter, key in zip(text, cycle(self.key)):
            distance = alphabet.find(letter) - alphabet.find(key)
            if distance < 0:
                distance += 26
            decoded_text += alphabet[distance]
        return decoded_text
