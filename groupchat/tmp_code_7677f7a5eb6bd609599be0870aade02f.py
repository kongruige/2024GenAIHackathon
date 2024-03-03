import subprocess
from fuzzywuzzy import fuzz, process

# Install the fuzzywuzzy and python-Levenshtein libraries
subprocess.call(['pip', 'install', 'fuzzywuzzy', 'python-Levenshtein'])

def fuzzy_search(text, query):
    results = process.extract(query, text.split(), scorer=fuzz.ratio, limit=5)
    return results

# Test the fuzzy search
sample_text = "Python is an amazing programming language used for various purposes."
query_term = "pyton"

results = fuzzy_search(sample_text, query_term)
for result in results:
    print(result)