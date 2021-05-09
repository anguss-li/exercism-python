def slices(series, length):
    '''
    series: string, digits to be sliced
    length: integer, the number of digits in each individual slice
    returns: list of strings, slices of original series each length long
    '''
    if length > len(series) or length < 1:
        raise ValueError(
            "Cannot slice %d digits using %d length" % (len(series), length))
    slice_list = []
    for integer in range(len(series)-length+1):
        slice_list.append(''.join(series[integer:integer+length]))
    return slice_list
