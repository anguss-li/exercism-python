def two_fer(name=None):
    '''
    name: string, name to be returned in string by function
    returns: string, "One for X, one for me." where X is name. If no input given
    , returns "One for you, one for me."
    '''
    if name == None:
        return "One for you, one for me."
    return "One for " + name + ", one for me."
