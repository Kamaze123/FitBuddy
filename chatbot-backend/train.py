import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras import regularizers
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import SGD
from sklearn.model_selection import train_test_split
import pickle
from utils import load_intents, prepare_data, vectorize_text, encode_labels

# Load data
data = load_intents("data/intents.json")
patterns, tags = prepare_data(data)

# Vectorize
X, vectorizer = vectorize_text(patterns)

# Encode labels
y, label_encoder = encode_labels(tags)
y = to_categorical(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X.toarray(), y, test_size=0.2, random_state=42
)

# Build model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],), kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.3),
    Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.2),
    Dense(y.shape[1], activation='softmax')
])

sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Early stopping
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

# Train
history = model.fit(
    X_train, y_train,
    epochs=200,
    batch_size=8,
    validation_data=(X_test, y_test),
    callbacks=[early_stop],
    verbose=1
)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.2f}")

from sklearn.metrics import classification_report
import numpy as np

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

print(classification_report(y_true_classes, y_pred_classes, 
      target_names=label_encoder.classes_))


# Save
model.save("model/chatbot_model.keras")

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("model/label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)