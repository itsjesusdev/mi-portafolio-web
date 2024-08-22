import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from googletrans import Translator

# Inicializar el traductor
translator = Translator()

# Cargar el modelo preentrenado MobileNetV2
model = MobileNetV2(weights='imagenet')

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)
    english_label = decoded_predictions[0][0][1]

    # Reemplazar los guiones bajos por espacios
    english_label = english_label.replace('_', ' ')

    # Traducir la etiqueta de la imagen al español
    translation = translator.translate(english_label, src='en' , dest='es')
    spanish_label = translation.text
    return spanish_label

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((root.winfo_width() - 40, root.winfo_height() - 250))
        img_tk = ImageTk.PhotoImage(img)
        panel.configure(image=img_tk)
        panel.image = img_tk
        result = predict_image(file_path)
        result_label.config(text=result)

# Crear la interfaz de usuario
root = tk.Tk()
root.title("PicPredictor")

# Configurar el tamaño de la ventana
window_width = 800
window_height = 600

# Obtener la resolución de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular la posición para centrar la ventana
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Establecer el tamaño y la posición de la ventana
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.configure(bg='#f0f0f0')

# Crear un frame para contener los elementos
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(pady=20)

# Configurar el panel para mostrar la imagen
panel = tk.Label(frame, bg='#f0f0f0')
panel.pack(pady=10)

# Configurar el botón para cargar la imagen
button = tk.Button(frame, text="Cargar imagen", command=load_image, font=('Helvetica', 14), bg='#4CAF50', fg='white', padx=20, pady=10)
button.pack(pady=10)

# Configurar la etiqueta para mostrar el resultado
result_label = tk.Label(frame, text='', font=('Helvetica', 18), bg='#f0f0f0', fg='#333333')
result_label.pack(pady=20)

# Iniciar la aplicación
root.mainloop()