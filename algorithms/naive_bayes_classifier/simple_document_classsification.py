# %%
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec = TfidfVectorizer()

# %%
documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]
tfidf_matrix = tfidf_vec.fit_transform(documents)


# %%
print('non-repeated words:', tfidf_vec.get_feature_names())
# %%
print('ID for each word:', tfidf_vec.vocabulary_)
# %%ß
print('tf-idf value for each word:', tfidf_matrix.toarray())


# %%
