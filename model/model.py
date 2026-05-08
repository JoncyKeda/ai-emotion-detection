from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense

def build_model(vocab_size=5000):

    model = Sequential()

    model.add(
        Embedding(
            input_dim=vocab_size,
            output_dim=64
        )
    )

    model.add(LSTM(64))

    model.add(Dense(32, activation='relu'))

    model.add(Dense(6, activation='softmax'))

    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model
