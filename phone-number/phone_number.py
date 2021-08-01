from re import sub


class PhoneNumber:
    '''
    A North American Numbering Plan (NANP) compliant telephone number.

    Attributes:
        number: 10 digit phone number
        area_code: 3 digit number representing a NANP area
    '''

    def __init__(self, number: str):
        '''Clean number and check legality.'''
        number = sub(r'[^0-9]', '', number)
        if (length := len(number)) < 10 or (number[0] != '1' and length == 11):
            raise ValueError('Invalid NANP phone number')

        self.number = number[length-10:length]
        if any(n == '0' or n == '1' for n in (self.number[0], self.number[3])):
            raise ValueError('1st/4th digit(s) invalid, must be from 2-9')

        self.area_code = self.number[0:3]

    def pretty(self) -> str:
        '''Return stylized self.number in format (NXX)-NXX-XXXX.'''
        return '-'.join(['('+self.area_code+')',
                         self.number[3:6],
                         self.number[6:11]])
