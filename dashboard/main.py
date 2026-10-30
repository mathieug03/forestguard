import eel # To communicate with the web interface
import tkinter as tk
import time


eel.init('web')

# Function to send coordinates to the web interface (synchronized with javascript)
@eel.expose
def envoyer_coordonnees(lat, lon, message="Fire"):
    print(f"Envoi de coordonnées : {lat}, {lon}")
    eel.ajouter_point_sur_carte(lat, lon, message)


eel.start('index.html', size=(800, 600), block=False)
eel.sleep(0.01)

# Send some coordinates to the web interface
envoyer_coordonnees(48.8566, 2.3522, "Example: Paris")
eel.sleep(2)
envoyer_coordonnees(34.003342, -118.485832, "LA Wildfires")
eel.sleep(2)

# Graphical interface to send additional coordinates
def envoyer_coordonnees_gui():
    lat = float(entry_lat.get())
    lon = float(entry_lon.get())
    message = entry_message.get()
    envoyer_coordonnees(lat, lon, message)

root = tk.Tk()
root.title("Coordonnées")

tk.Label(root, text="Latitude:").pack(pady=5)
entry_lat = tk.Entry(root)
entry_lat.pack(pady=5)

tk.Label(root, text="Longitude:").pack(pady=5)
entry_lon = tk.Entry(root)
entry_lon.pack(pady=5)

tk.Label(root, text="Message:").pack(pady=5)
entry_message = tk.Entry(root)
entry_message.pack(pady=5)

tk.Button(root, text="Envoyer", command=envoyer_coordonnees_gui).pack(pady=10)

root.mainloop()
