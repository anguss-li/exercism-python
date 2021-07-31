from re import sub


class PhoneNumber:
    def __init__(self, number):
        '''
        number: string, number to be stored.
        '''
        number = sub(r'[^0-9]', '', number)
        if (number[0] != '1' and len(number) == 11) or (len(number) < 10):
            raise ValueError('Invalid NANP phone number')
        self.number = number[len(number)-10:len(number)]
        if any(n == '0' or n == '1' for n in (self.number[0], self.number[3])):
            raise ValueError('1st/4th digit(s) invalid, must be from 2-9')
        self.area_code = self.number[0:3]

    def pretty(self):
        '''
        Returns: stylized self.number in format (NXX)-NXX-XXXX
        '''
        return '-'.join(['('+self.area_code+')',
                         self.number[3:6],
                         self.number[6:11]])