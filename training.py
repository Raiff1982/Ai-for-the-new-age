<<<<<<< HEAD
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load and preprocess data
def load_data():
    # Example with MNIST dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)

# Define the model
def build_model(input_shape):
    model = Sequential([
        tf.keras.layers.Flatten(input_shape=input_shape),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(10, activation='softmax')
    ])
    return model

# Train the model
def train_model(model, x_train, y_train, epochs=5, batch_size=32):
    model.compile(optimizer=Adam(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

# Save the trained model
def save_model(model, filepath):
    model.save(filepath)

if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = load_data()
    model = build_model(input_shape=(28, 28))
    train_model(model, x_train, y_train)
    save_model(model, "pi2_0_model.h5")
=======
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load and preprocess data
def load_data():
    # Example with MNIST dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)

# Define the model
def build_model(input_shape):
    model = Sequential([
        tf.keras.layers.Flatten(input_shape=input_shape),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(10, activation='softmax')
    ])
    return model

# Train the model
def train_model(model, x_train, y_train, epochs=5, batch_size=32):
    model.compile(optimizer=Adam(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

# Save the trained model
def save_model(model, filepath):
    model.save(filepath)

if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = load_data()
    model = build_model(input_shape=(28, 28))
    train_model(model, x_train, y_train)
    save_model(model, "pi2_0_model.h5")
>>>>>>> 15b9ee2ee2931a43c5ec86ae50651f777b149473
