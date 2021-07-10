from string import ascii_uppercase as capitals, ascii_letters as letters


def response(hey_bob: str) -> str:
    '''Emulate Bob's response according to the README'''
    chars = hey_bob.strip()
    is_capitalized = (all(char in capitals for char in chars if char in letters)
                      and any(char in letters for char in chars))
    is_question = chars.endswith("?")
    is_silence = chars == ""

    if is_silence:
        return "Fine. Be that way!"
    elif is_capitalized and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_capitalized:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    return "Whatever."
