def response(hey_bob: str) -> str:
    '''Emulate Bob's response according to the README'''
    speech = hey_bob.strip()
    is_capitalized = speech.isupper()
    is_question = speech.endswith("?")
    if is_capitalized and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_capitalized:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    elif speech == "":
        return "Fine. Be that way!"
    return "Whatever."
