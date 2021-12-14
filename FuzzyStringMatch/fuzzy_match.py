# Found this great package that returns similarity score for strings. This can be useful when you can't join
# to get data and there are minor dissimilarities with the keys.
# https://pypi.org/project/fuzzywuzzy/
# Also, install python-Levenshtein to remove a warning associated

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

string_1 = "Is this same?"
string_2 = "is this same"
string_3 = "this is same"

# Checks for exact match
fuzz.ratio(string_1, string_2) #88

# Doesn't worry about punctuations
fuzz.partial_ratio(string_1, string_2) #92

# Doesn't care about the order of the words
fuzz.token_sort_ratio(string_2, string_3) #100

# Handles lower and upper cases with some other parameters (punctuations too, I guess)
fuzz.WRatio(string_1, string_2) #100

# To check multiple strings to a particular string
choices = ["is this same", 'this might be same', 'this same is']

process.extract(string_1, choices) # [('is this same', 100), ('this same is', 95), ('this might be same', 86)]

# Get the best choice from the options
process.extractOne(string_1, choices) # ('is this same', 100)
