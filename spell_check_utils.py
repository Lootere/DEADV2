from fuzzywuzzy import process

# Fast spell check function

def fast_spell_check(word, possible_words):
    closest_match, score = process.extractOne(word, possible_words)
    return closest_match if score >= 80 else word

# Suggestion function

def suggestion(word, possible_words):
    return process.extract(word, possible_words, limit=3)

# Example usage:
if __name__ == '__main__':
    words_list = ['Deadpool', 'Avengers', 'Ironman', 'Batman']
    test_word = 'Deadplool'
    print(f"Corrected: {fast_spell_check(test_word, words_list)}")
    print(f"Suggestions: {suggestion(test_word, words_list)}")