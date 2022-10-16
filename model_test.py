import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import PIL
import PIL.Image
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

img_height , img_width = 299 , 299

medi_scanner_model = tf.keras.models.load_model("/medi-scanner/keras_save/burns")
test_image = PIL.Image.open("C:/medi-scanner/testimages/test-image (79).png").resize((img_height , img_width))
test_image = np.array(test_image)/255.0
test_image = test_image.reshape(1 , 299 , 299 , 3)
print(test_image.shape)
prediction = medi_scanner_model.predict(test_image)
print(prediction[0])
print(np.argmax(prediction))