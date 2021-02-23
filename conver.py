#import tensorflow as tf

# Convert the model

#converter = tf.lite.TFLiteConverter.from_saved_model('rev2') 
#tflite_model = converter.convert()

# Save the model.
#with open('rev2.tflite', 'wb') as f:
  #f.write(tflite_model)
  
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('arjuna')
converter.target_spec.supported_ops = [
  tf.lite.OpsSet.TFLITE_BUILTINS, # enable TensorFlow Lite ops.
  tf.lite.OpsSet.SELECT_TF_OPS # enable TensorFlow ops.
]
tflite_model = converter.convert()
with open('arjuna.tflite', 'wb') as f:
  f.write(tflite_model)

