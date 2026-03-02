import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import pickle
from utils import load_intents, prepare_data, vectorize_text, encode_labels

#Loading data
data = load_intents("data/intents.json")
patterns, tags = prepare_data(data)

#Vectorize
X, vectorizer = vectorize_text(patterns)

#Encode labels
y, label_encoder = encode_labels(tags)
y = to_categorical(y)

#Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X.toarray(), y, test_size = 0.2, random_state=42
)