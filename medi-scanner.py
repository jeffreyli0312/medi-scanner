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

# train_ds = tf.keras.utils.image_dataset_from_directory(
#     base_dir,
#     validation_split = 0.3,
#     subset = "training",
#     seed = 123,
#     image_size = (img_height , img_width),
#     batch_size = batch_size,
# )

# val_ds = tf.keras.utils.image_dataset_from_directory(
#     base_dir,
#     validation_split = 0.2,
#     subset = "validation",
#     seed = 123,
#     image_size = (img_height , img_width),
#     batch_size = batch_size,
# )

# class_names = train_ds.class_names
# print(class_names)

# train_ds = train_ds.cache()
# val_ds = val_ds.cache()

# num_classes = 4
# model = tf.keras.Sequential([
#     tf.keras.layers.Rescaling(1./255),
#     tf.keras.layers.Conv2D(32 , 5 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(2 , 2),

#     tf.keras.layers.Conv2D(64 , 3 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(2 , 2),

#     tf.keras.layers.Conv2D(128, 3 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(2 , 2),

#     tf.keras.layers.Conv2D(128 , 3 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(2 , 2),
    
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(512 , activation='relu'),
#     tf.keras.layers.Dense(num_classes)
# ])

# model.compile(
#     optimizer = 'adam',
#     loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
#     metrics = (['accuracy'])
# )
# epochs = 20
# history = model.fit(
#     train_ds,
#     validation_data = val_ds,
#     epochs = epochs
# )

# model.save("/medi-scanner/keras_save/burns")

tr_image_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1./255,
    rotation_range = 45,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    channel_shift_range = 0.2,
    validation_split = 0.2
)
tr_data_gen = tr_image_data_gen.flow_from_directory(
    batch_size = batch_size,
    directory = base_dir,
    shuffle = True,
    target_size = (img_height, img_width),
    class_mode = 'binary',
    subset = 'training'
)

val_image_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale = 1./255,
    validation_split = 0.2,
)
val_data_gen = val_image_data_gen.flow_from_directory(
    batch_size = batch_size,
    directory = base_dir,
    shuffle = True,
    target_size = (img_height , img_width),
    class_mode = 'binary',
    subset = 'validation'
)

# num_classes = 4
# model = tf.keras.Sequential([
#     tf.keras.layers.Conv2D(32 , 3 , activation= 'relu' , input_shape= (img_height, img_width , 3)),
#     tf.keras.layers.MaxPooling2D(2, 2),

#     tf.keras.layers.Conv2D(64 , 3 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(2 , 2),

#     tf.keras.layers.Conv2D(64 , 3 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(2 , 2),

#     tf.keras.layers.Conv2D(128 , 3 , activation='relu'),
#     tf.keras.layers.MaxPooling2D(2 , 2),

#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(512 , activation='relu'),
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(num_classes)
# ])

# model.compile(
#     optimizer = 'adam',
#     loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
#     metrics = ['accuracy']
# )

# model.fit_generator(
#     tr_data_gen,
#     epochs = 25,
#     steps_per_epoch = 35,
#     validation_data = val_data_gen,
#     validation_steps = 5,
# )

model_url = "https://tfhub.dev/google/tf2-preview/inception_v3/feature_vector/4"

model = tf.keras.Sequential([
    hub.KerasLayer(model_url , input_shape = (299 , 299 , 3) , trainable = False),
    tf.keras.layers.Dense(32 , activation = 'relu'), 
    tf.keras.layers.Dense(4 , activation = 'softmax')
])

model.compile(
    optimizer = 'adam',
    loss = 'sparse_categorical_crossentropy',
    metrics = ['accuracy']
)

EPOCHS = 13
history = model.fit(
    tr_data_gen,
    epochs = EPOCHS,
    steps_per_epoch = 35,
    validation_data = val_data_gen,
    validation_steps = 9
)

model.save("/medi-scanner/keras_save/burns")