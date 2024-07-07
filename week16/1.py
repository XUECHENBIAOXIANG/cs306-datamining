
import pandas as pd
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Step 1: Load data from csv files
data = pd.read_csv("iris(1).csv")
X = data.iloc[:, 0:4].values
y = data.iloc[:, 4].values

scaler = StandardScaler()
X = scaler.fit_transform(X)
encoder = LabelEncoder()
y = encoder.fit_transform(y)

y = to_categorical(y)
print("X:", X)
print("y:", y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def keras_model():
    # Create a model
    model = Sequential()
    model.add(Dense(20, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(3, activation='softmax'))  # 3 classes for Iris dataset
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(learning_rate=0.01), metrics=['accuracy'])
    return model

# Instantiate the model
model = keras_model()
# Fit the model
H = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=500, verbose=0)
import matplotlib.pyplot as plt

# Plot the loss
plt.plot(H.history["loss"], label="loss")
plt.plot(H.history["val_loss"], 'r', label="val_loss")
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
import numpy as np
from sklearn.metrics import classification_report

# Make predictions
y_pred_softmax = model.predict(X_test)
y_pred = np.argmax(y_pred_softmax, axis=1)
y_test_classes = np.argmax(y_test, axis=1)

# Print classification report
print(classification_report(y_test_classes, y_pred))
