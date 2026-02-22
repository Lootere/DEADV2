from rapidfuzz import process, fuzz

class SpellChecker:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.cache = {}

    def check_word(self, word):
        if word in self.cache:
            return self.cache[word]  # Return cached result
        else:
            closest_matches = process.extract(word, self.dictionary, scorer=fuzz.ratio, limit=5)
            suggestions = [match[0] for match in closest_matches if match[1] > 80]  # Threshold for suggestions
            self.cache[word] = suggestions
            return suggestions

    def check_sentence(self, sentence):
        words = sentence.split()
        results = {}
        for word in words:
            results[word] = self.check_word(word)
        return results

# Example usage
if __name__ == '__main__':
    dictionary = ['apple', 'banana', 'orange', 'grape', 'fruit']
    spell_checker = SpellChecker(dictionary)
    sentence_to_check = "I love appel and bannana."
    print(spell_checker.check_sentence(sentence_to_check))