import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='Nadam', loss='mean_squared_error')
x = np.array(([1.0,2.0,3.2,4.5]) ,dtype=float)
y = np.array(([0.0,0.3010299957,0.5051599783,0.6532125138]) ,dtype=float)
model.fit(x,y,epochs=1000)
print(model.predict([10]))

#Output
#[[1.7007911]]
