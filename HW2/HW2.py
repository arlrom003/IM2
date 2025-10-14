def char_frequency(text):
    freq = {}
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            if ch in freq:
                freq[ch] = freq[ch] + 1
            else:
                freq[ch] = 1
    return freq

user_input = input("Enter string: ")
strings = user_input.split(",")

for s in strings:
    s = s.strip()
    freq = char_frequency(s)
    for key in freq:
        print(key, "=", freq[key], end=", ")
    print()
