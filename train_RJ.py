from dpd_format import MobilenetV3
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
from livelossplot.keras import PlotLossesCallback
from tensorflow.python import keras
from tensorflow.keras.callbacks import ModelCheckpoint
import random as rn
# tf.enable_eager_execution()
from datetime import datetime
from keras.preprocessing.image import ImageDataGenerator
#
datagen = ImageDataGenerator(
    rotation_range=15,
    horizontal_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1
    #zoom_range=0.3
    )
datetime_str = datetime.now().strftime("%m_%d_%H_%M")
BATCH_SIZE = 16

NUM_CLASSES=10
EPOCH=1
DATASET='cifar10'
INPUT_SHAPE=(32, 32)
np.random.seed(123)
rn.seed(123)
tf.random.set_seed(123)
mobilenet_v3 = MobilenetV3(INPUT_SHAPE,NUM_CLASSES,'small',alpha=0.5)
cos_lr = tf.keras.callbacks.LearningRateScheduler(
    lambda epoch, _: tf.compat.v1.train.cosine_decay(1e-3, epoch,EPOCH)().numpy(), 1)
logging=tf.keras.callbacks.TensorBoard(log_dir='./model', write_images=True)
mobilenet_v3.compile(tf.keras.optimizers.Nadam(1e-3), loss=tf.keras.losses.sparse_categorical_crossentropy,metrics=["sparse_categorical_accuracy"])

mobilenet_v3.summary()
dataset, info = tfds.load(name=DATASET, split=[tfds.Split.TRAIN, tfds.Split.TEST], with_info=True,as_supervised=True,try_gcs=tfds.is_dataset_on_gcs(DATASET))
train_dataset, test_dataset = dataset
#   augmentation



train_num = info.splits['train'].num_examples
test_num = info.splits['test'].num_examples

train_images, train_labels = next(iter(train_dataset.batch(train_num)))
train_labels = train_labels.numpy()
datagen.fit(train_images.numpy())
# tf.compat.v1.set_random_seed(1)

test_images, test_labels = next(iter(test_dataset.batch(test_num)))



def data_processing(x_train, x_test, img_rows, img_cols, channels):
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, channels)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, channels)
    return x_train, x_test

train_images, test_images = data_processing(train_images.numpy(), test_images.numpy(), 32, 32, 3)

test_dataset = test_dataset.map(lambda image,label:(tf.image.resize(image,INPUT_SHAPE),label)).batch(BATCH_SIZE).prefetch(
    tf.data.experimental.AUTOTUNE).repeat()

checkpoint = ModelCheckpoint(
    "./Best_model/model", monitor='val_sparse_categorical_accuracy', verbose=1, save_best_only=True,
    save_weights_only=False, mode='auto', save_freq='epoch', options=None
)
mobilenet_v3.fit_generator(datagen.flow(train_images,train_labels,batch_size=BATCH_SIZE),epochs=EPOCH, steps_per_epoch=max(1,train_num//BATCH_SIZE), validation_data=(test_images,test_labels),validation_steps=max(1,test_num//BATCH_SIZE), callbacks=([checkpoint,cos_lr,logging]))

