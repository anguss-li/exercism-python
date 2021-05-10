import string


class PhoneNumber:
    def __init__(self, number):
        """
        number: string, number to be stored.
        """
        removable_chars = str.maketrans(dict.fromkeys(string.punctuation+' '))
        number = number.translate(removable_chars)
        if (number[0] != "1" and len(number) == 11) or (len(number) < 10):
            raise ValueError("Invalid NANP phone number")
        self.number = number[len(number)-10:len(number)]
        illegal_digits = (self.number[0] == "0" or self.number[0] == "1" or
                          self.number[3] == "0" or self.number[3] == "1")
        if illegal_digits:
            raise ValueError("1st/4th digit(s) invalid, must be from 2-9")
        self.area_code = self.number[0:3]

    def pretty(self):
        '''
        Returns: stylized self.number in format (NXX)-NXX-XXXX
        '''
        pretty_number = "("
        for index in range(len(self.number)):
            if index == 2:
                pretty_number += (self.number[index] + ")-")
            elif index == 5:
                pretty_number += (self.number[index] + "-")
            else:
                pretty_number += (self.number[index])
        return pretty_number
