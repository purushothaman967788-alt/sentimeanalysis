import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

def process_review(review):
    review_lower = review.lower()
    review_puncs_nums_removed = re.sub(r"[^a-z\s]", "", review_lower)
    review_tokens = word_tokenize(review_puncs_nums_removed)
    stop_words = stopwords.words('English')
    review_tokens_stopwords_removed = [token for token in review_tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token, pos='n') for token in review_tokens_stopwords_removed]
    return " ".join(lemmatized_tokens)

if __name__ == "__main__":
   review = "The prodict was really nice!!!"
   print(process_review(review))
         