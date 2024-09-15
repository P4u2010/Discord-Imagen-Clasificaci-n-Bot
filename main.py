from tensorflow.keras.models import load_model

# Cargar el modelo desde el archivo .h5
model = load_model('ruta_a_tu_archivo/keras_model.h5')

# Mostrar un resumen del modelo
model.summary()