import os
import cv2 
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.constraints import maxnorm
from keras.utils import np_utils


def train_powerpuff_model():
    blossom, bubbles, buttercup = [], [], []

    for i in os.listdir('utonium/training/powerpuff/blossom'):
        image = cv2.imread(f'utonium/training/powerpuff/blossom/{i}', 3)
        b,g,r = cv2.split(image)
        rgb_img1 = cv2.merge([r,g,b])
        stretch_near = cv2.resize(rgb_img1, (32, 32),  
                    interpolation = cv2.INTER_NEAREST)
        blossom.append(stretch_near)

    for i in os.listdir('utonium/training/powerpuff/bubbles'):
        image = cv2.imread(f'utonium/training/powerpuff/bubbles/{i}', 3)
        b,g,r = cv2.split(image)
        rgb_img1 = cv2.merge([r,g,b])
        stretch_near = cv2.resize(rgb_img1, (32, 32),  
                    interpolation = cv2.INTER_NEAREST)
        bubbles.append(stretch_near)

    for i in os.listdir('utonium/training/powerpuff/buttercup'):
        image = cv2.imread(f'utonium/training/powerpuff/buttercup/{i}', 3)
        b,g,r = cv2.split(image)
        rgb_img1 = cv2.merge([r,g,b])
        stretch_near = cv2.resize(rgb_img1, (32, 32),  
                    interpolation = cv2.INTER_NEAREST)
        buttercup.append(stretch_near)

    X = [blossom, buttercup, bubbles]
    y = [[1] for _ in blossom] + [[2] for _ in buttercup] + [[3] for _ in bubbles]
    X = np.concatenate(X)
    y = np.concatenate(y)

    X = X.astype('float32')
    X = X / 255.0

    y = np_utils.to_categorical(y)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=X.shape[1:], padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3), input_shape=(4, 32, 32), activation='relu', padding='same'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(Conv2D(32, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(Flatten())
    model.add(Dropout(0.2))
    model.add(Dense(4))
    model.add(Activation('softmax'))

    epochs = 50
    optimizer = 'adam'
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    print(model.summary())

    model.fit(X, y, epochs=epochs, batch_size=64)

    # serialize model to JSON
    model_json = model.to_json()
    with open("powerpuff_model.json", "w") as json_file:
        json_file.write(model_json)

    # serialize weights to HDF5
    model.save_weights("model.h5")
    print("Saved model to disk")
