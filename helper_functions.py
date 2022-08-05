import tensorflow as tf
import numpy as np
import pandas as pd
def build_model():
    tf.random.set_seed(42)
    xav = tf.keras.initializers.glorot_normal()
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(100, activation='relu', input_shape=(X.shape[1],)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(50, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(15, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dropout(0.1),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer=tf.keras.optimizers.RMSprop(), loss=tf.keras.losses.binary_crossentropy, metrics=[tf.keras.metrics.AUC()])
    return model

def calc_pie(df):
    """Takes an input of pd.Series, returns wedge lengths"""
    labels = df.value_counts().index
    lengths = df.value_counts().to_numpy()
    
    return labels, lengths