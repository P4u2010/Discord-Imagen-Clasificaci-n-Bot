from keras.model import load_model # Importa desde tensorflow.keras
from PIL import Image, ImageOps  # Pillow para manejar imágenes
import numpy as np

def get_class(model_path, label_path, image_path):
    # Desactivar notación científica para mayor claridad
    np.set_printoptions(suppress=True)

    # Cargar el modelo exportado por Teachable Machine
    model = load_model(model_path, compile=False)

    # Cargar las etiquetas (etiquetas exportadas en .txt por Teachable Machine)
    class_names = open(label_path, "r").readlines()

    # Crear el array de la forma correcta para alimentar el modelo de Keras
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Cargar y procesar la imagen
    image = Image.open(image_path).convert("RGB")

    # Redimensionar la imagen a 224x224 píxeles
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Convertir la imagen en un array numpy
    image_array = np.asarray(image)

    # Normalizar la imagen
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Colocar la imagen normalizada en el array
    data[0] = normalized_image_array

    # Realizar la predicción
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Devolver el nombre de la clase y la confianza
    return (class_name.strip(), confidence_score)
