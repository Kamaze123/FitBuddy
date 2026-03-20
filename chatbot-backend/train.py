from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
import pickle
from utils import load_intents, prepare_data, encode_labels
from sklearn.model_selection import cross_val_score

data = load_intents("data/intents.json")
patterns, tags = prepare_data(data)
y, label_encoder = encode_labels(tags)

model = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=500)),
    ('clf', MultinomialNB(alpha=0.1))
])

scores = cross_val_score(model, patterns, y, cv=5, scoring='accuracy')
print(f"CV Accuracy: {scores.mean():.2f} (+/- {scores.std():.2f})")

model.fit(patterns, y)

pickle.dump(model, open("model/chatbot_model.pkl", "wb"))
pickle.dump(label_encoder, open("model/label_encoder.pkl", "wb"))