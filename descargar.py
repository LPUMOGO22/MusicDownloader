import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import re

def DownloadAudio():
    link = link_entry.get()
    if link:
        try:
            youtubeObject = YouTube(link)
            title = youtubeObject.title
            # Remueve caracteres especiales que no son válidos en nombres de archivos
            title = re.sub(r'[\\/*?:"<>|]', '', title)
            audioStream = youtubeObject.streams.filter(only_audio=True).first()
            audioStream.download(filename=f"{title}.mp3")
            messagebox.showinfo("Descarga completada", "La descarga del audio en formato mp3 ha sido completada exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", "Ha ocurrido un error al descargar el audio: {}".format(str(e)))
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un enlace de YouTube.")

# Crear la ventana principal
root = tk.Tk()
root.title("Descargar Audio de YouTube")

# Crear y posicionar los widgets
link_label = tk.Label(root, text="Enlace de YouTube:")
link_label.pack(pady=5)
link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)
download_button = tk.Button(root, text="Descargar Audio", command=DownloadAudio)
download_button.pack(pady=5)

# Ejecutar la interfaz gráfica
root.mainloop()

