import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os
import PIL
import PIL.Image
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

base_dir = os.path.dirname("C:\medi-scanner\dataset")
base_dir = os.path.join(base_dir , "dataset")

batch_size = 32
img_height , img_width = 180 , 180

# CLASSIFIER_URL = "https://tfhub.dev/google/imagenet/mobilenet_v2_130_224/classification/5"
# IMAGE_RES = 224

# def plotImages(images_arr):
#     fig, axes = plt.subplots(1, 5, figsize=(20,20))
#     axes = axes.flatten()
#     for img, ax in zip(images_arr, axes):
#         ax.imshow(img)
#     plt.tight_layout()
#     plt.show()

# image_gen_train = tf.keras.preprocessing.image.ImageDataGenerator(
#     validation_split = 0.2,
#     rescale = 1./255,
#     rotation_range = 40,
#     width_shift_range = 0.2,
#     height_shift_range = 0.2,
#     shear_range = 0.2,
#     zoom_range = 0.5,
#     horizontal_flip = True,
#     fill_mode = 'nearest'
# )
# train_data_gen = image_gen_train.flow_from_directory(
#     batch_size = batch_size,
#     directory = base_dir, 
#     shuffle = True,
#     target_size = (img_height , img_width),
#     subset = 'training',
#     class_mode = 'sparse'
# )
# image_gen_val = tf.keras.preprocessing.image.ImageDataGenerator(
#     rescale = 1./255
# )
# val_data_gen = image_gen_val.flow_from_directory(
#     batch_size = batch_size,
#     directory = base_dir,
#     shuffle = True,
#     target_size = (img_height , img_width),
#     subset = 'validation',
#     class_mode = 'sparse'
# )

train_ds = tf.keras.utils.image_dataset_from_directory(
    base_dir,
    validation_split = 0.2,
    subset = "training",
    seed = 123,
    image_size = (img_height , img_width),
    batch_size = batch_size
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    base_dir,
    validation_split = 0.2,
    subset = "validation",
    seed = 123,
    image_size = (img_height , img_width),
    batch_size = batch_size
)

class_names = train_ds.class_names
print(class_names)

train_ds = train_ds.cache()
val_ds = val_ds.cache()

# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#   for i in range(9):
#     ax = plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i].numpy().astype("uint8"))
#     plt.title(class_names[labels[i]])
#     plt.axis("off")
# plt.show()

# model = tf.keras.Sequential([
#     hub.KerasLayer(CLASSIFIER_URL , input_shape=(IMAGE_RES , IMAGE_RES , 3)),
#     tf.keras.layers.Dense(4, activation= 'softmax')
# ])

# model.compile(
#     optimizer='adam',
#     loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#     metrics=['accuracy']
# )

# history = model.fit(
#     train_ds,
#     epochs=21,
#     validation_data=val_ds
# )

num_classes = 4
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255),
    tf.keras.layers.Conv2D(32 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),

    tf.keras.layers.Conv2D(64 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),

    tf.keras.layers.Conv2D(64 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),

    tf.keras.layers.Conv2D(128 , 3 , activation='relu'),
    tf.keras.layers.MaxPooling2D(2 , 2),
    
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256 , activation='relu'),
    tf.keras.layers.Dense(num_classes)
])

model.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
    metrics = (['accuracy'])
)
epochs = 12
history = model.fit(
    train_ds,
    validation_data = val_ds,
    epochs = epochs
)

model.save("/medi-scanner/keras_save/burns")

medi_scanner_model = tf.keras.models.load_model("/medi-scanner/keras_save/burns")
test_image = PIL.Image.open("C:/medi-scanner/testimages/test-image (1).png").resize((img_height , img_width))
test_image = np.array(test_image)/255.0
print(test_image.shape)
prediction = medi_scanner_model.predict(test_image)
prediction.shape

predicted_class = np.argmax(prediction[0] , axis=1)
print(predicted_class)