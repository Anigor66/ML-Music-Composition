import cv2
import tensorflow as tf
import numpy as np

CATEGORIES = ["capacitor","filament","LED","microprocessor","semiconductor diode"]


def prepare(filepath):
    IMG_SIZE = 100
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("64x3-CNN.model")

prediction = model.predict([prepare('C:/Users/Sanket/Desktop/led.jpg')])

print(prediction)
print(CATEGORIES)
for i in range(0, 5):
    if prediction[0][i] > 0.5:
        print(prediction[0][i])
        print("Component:", end="")
        print(CATEGORIES[i])
    else:
        print("Object not found")
