from fuzzywuzzy import process

class SpellingCorrector:
    def __init__(self, word_list):
        """Initialize with a list of correct words."""
        self.word_list = word_list

    def correct(self, word):
        """Return the closest match for the input word from the word list."""
        closest_match, score = process.extractOne(word, self.word_list)
        return closest_match

    def suggest_corrections(self, input_words):
        """Suggest corrections for a list of input words."""
        suggestions = {}
        for word in input_words:
            suggestions[word] = self.correct(word)
        return suggestions

# Example Usage
# Initialize with a list of correct words
# corrector = SpellingCorrector(['apple', 'banana', 'orange'])
# print(corrector.suggest_corrections(['aple', 'bananna']))