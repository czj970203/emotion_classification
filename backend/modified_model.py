from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras import regularizers



class myCallback(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('acc') > 0.95):
            print("\nReached 95% accuracy so cancelling training!")
            self.model.stop_training = True


callback1 = myCallback()

def swish_activation(x):
    return (K.sigmoid(x) * x)

train_dir = 'train'
validation_dir = 'val'
test_dir = 'test'

datagen = ImageDataGenerator(
        featurewise_center=False,
        samplewise_center=False,
        featurewise_std_normalization=False,
        samplewise_std_normalization=False,
        zca_whitening=False,
        rotation_range=10,
        zoom_range = 0.0,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=False,
        vertical_flip=False,
        rescale=1./255)

train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(48, 48),
    color_mode='grayscale',
    batch_size=224,
    shuffle=True
)


validation_generator = datagen.flow_from_directory(
    validation_dir,
    target_size=(48, 48),
    color_mode='grayscale',
    batch_size=28,
    shuffle=True
)


test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(48, 48),
    color_mode='grayscale',
    batch_size=28,
    shuffle=True
)

model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation="relu", input_shape=(48, 48, 1), padding='same'),
    keras.layers.Conv2D(32, (3, 3), activation="relu", padding="same"),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.BatchNormalization(axis=1),
    keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same"),
    keras.layers.Conv2D(64, (3, 3), activation="relu", padding="same"),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.BatchNormalization(axis=1),
    keras.layers.Conv2D(96, (3, 3), dilation_rate=(2, 2), activation="relu", padding="same"),
    keras.layers.Conv2D(96, (3, 3), activation="relu", padding="valid"),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.BatchNormalization(axis=1),
    keras.layers.Conv2D(128, (3, 3), dilation_rate=(2, 2), activation="relu", padding="same"),
    keras.layers.Conv2D(128, (3, 3), activation="relu", padding="valid"),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation=swish_activation, kernel_regularizer=regularizers.l2(0.02)),
    keras.layers.Dropout(rate=0.5),
    keras.layers.Dense(64, activation=swish_activation, kernel_regularizer=regularizers.l2(0.02)),
    keras.layers.Dropout(rate=0.5),
    keras.layers.Dense(7, activation="softmax")
])

model.summary()

model.compile(optimizer='adam', loss="categorical_crossentropy", metrics=['accuracy'])
history = model.fit_generator(
    train_generator,
    steps_per_epoch=128,
    epochs=50,
    validation_data=validation_generator,
    validation_steps=128,
    callbacks=[callback1]
)

print(model.evaluate_generator(test_generator))

#参考了VGG16之后对网络结构进行了更改，使其更加轻量化，并加入了Dropout层和regularizer以减轻过拟合现象，对图像做了增强处理，保留
#表情特征，弱化噪声影响。