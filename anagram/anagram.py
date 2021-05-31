def find_anagrams(word, candidates):
    lower_word = word.lower()
    word_chars = sorted(lower_word)
    anagrams = []

    for candidate in candidates:
        lower_candidate = candidate.lower()
        candidate_chars = sorted(lower_candidate)
        if candidate_chars == word_chars and lower_candidate != lower_word:
            anagrams.append(candidate)

    return anagrams
