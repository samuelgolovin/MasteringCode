def count_char_frequencies(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

print(count_char_frequencies("hello"))  # Output {'h': 1, 'e': 1, 'l': 2, 'o': 1
print(count_char_frequencies("Once upon a time, in a land far, far away,\
there lived an old lady in an onld house. Only time could tell..."))
