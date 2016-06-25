import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
from ftfy import fix_text


class Analyze(object):
    """Object that aids in the analysis of text from different sources."""

    def __init__(self, text_file_path):
        """Initalize Analyze object given the path to a file with text."""
        self.stop_words = self._get_stop_words()
        self.raw_text = self._get_raw_text(text_file_path)
        self.text = self._process(self.raw_text)

    def _get_raw_text(self, text_file_path):
        with open(text_file_path, 'r') as f:
            raw_text = [line.decode('utf-8').strip() for line in f.readlines()]
        return raw_text

    def _get_stop_words(self):
        stop_words = stopwords.words('english')
        stop_words.extend(list(string.punctuation))
        stop_words.extend(string.whitespace)
        return stop_words

    def _process(self, text):
        raw_text = map(fix_text, text)
        return raw_text

    def get_words(self):
        """Return a list of the words in the text."""
        words_nested = [word_tokenize(x) for x in self.text]
        words = [word.lower() for li in words_nested for word in li]
        return words

    def get_sentences(self):
        """Return a list of the sentences in the text."""
        # TODO
        pass
