'''Trains a simple convnet on the my char dataset.
Gets to 99.25% test accuracy after 12 epochs
'''

from __future__ import print_function
import numpy as np
import os
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

import PIL
from PIL import Image
from .. import root_dir

# constant and path varaibles
batch_size = 32
num_classes = 9
epochs = 50

# input image dimensions
char_label = ["bo", "co", "gho", "go", "jo", "kho", "ko", "mo", "tho"]
IMG_SIZE = 150
IMG_CHANNEL = 3
IMG_SHAPE = (IMG_SIZE, IMG_SIZE, IMG_CHANNEL)

aug_crop_img_dir_final = os.path.join(root_dir.data_path(), "aug_crop_char_img_final")
lr = 0.001

def process_train_data():
    for folder_num, folder in enumerate(char_label):

        work_folder = os.path.join(aug_crop_img_dir_final, folder)
        train_images = [os.path.join(work_folder, path) for path in os.listdir(work_folder)]

        print("preparing %s folder. total images: %s" % (folder, str(len(train_images))))

        data = np.ndarray((len(train_images), IMG_SIZE, IMG_SIZE, IMG_CHANNEL),
                      dtype = np.uint8)

        label = []

        for i, image_file in enumerate(train_images):
            img = Image.open(image_file)
            img_px = np.array(img)  #convert PIL image to numpy array

            data[i] = img_px
            label.append(folder_num)

        if (folder_num == 0):
            train_data = data
            train_label = label

        else:
            train_data = np.vstack((train_data, data))
            train_label = train_label + label

    return train_data, train_label



# the data, split between train and test sets
(x_train, y_train) = process_train_data()

x_train = x_train.astype('float32')
#x_test = x_test.astype('float32')

x_train /= 255
#x_test /= 255

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
#y_test = keras.utils.to_categorical(y_test, num_classes)

print("\ntrain_data shape:", x_train.shape)
print("train_label_shape:", y_train.shape)

model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3),
                 activation = 'relu',
                 input_shape = IMG_SHAPE))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(100, activation='relu'))

model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size = batch_size,
          epochs = epochs,
          verbose = 2,
	  shuffle = True,
          validation_split = 0.20)


score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
