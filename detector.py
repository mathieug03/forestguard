import os
from inference_sdk import InferenceHTTPClient, InferenceConfiguration
import supervision as sv
from inference.core.utils.image_utils import load_image_bgr
import tkinter as tk
from tkinter import filedialog

def get_image_path(): #Using Tkinter to get the image with a demo graphical interface
    image_path = ""  # Initialize image_path

    def submit():
        nonlocal image_path
        image_path = entry.get()
        root.destroy()

    def browse_file():
        nonlocal image_path
        image_path = filedialog.askopenfilename()
        entry.delete(0, tk.END)
        entry.insert(0, image_path)

    root = tk.Tk()
    root.title("ForestGuard - Input Image Path")

    tk.Label(root, text="ForestGuard", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Label(root, text="Enter image URL or browse for a file:", font=("Helvetica", 12)).pack(pady=5)
    entry = tk.Entry(root, width=50, font=("Helvetica", 12))
    entry.pack(pady=5)
    tk.Button(root, text="Browse", command=browse_file, font=("Helvetica", 12)).pack(pady=5)
    tk.Button(root, text="Submit", command=submit, font=("Helvetica", 12)).pack(pady=10)

    root.mainloop()
    return image_path

image_path = get_image_path()

custom_configuration = InferenceConfiguration(confidence_threshold=0.1) #Configuring the AI Model 
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=os.environ["ROBOFLOW_API_KEY"]
)

image = load_image_bgr(image_path)
with CLIENT.use_configuration(custom_configuration):
    results = CLIENT.infer(image_path, model_id="forest-fire-detector-2-cmeye/5")

print(results) #Get textual results of the detection

# Visualize the detection results

results = sv.Detections.from_inference(results)
annotator = sv.BoxAnnotator(thickness=4)
annotated_image = annotator.annotate(image, results)
annotator = sv.LabelAnnotator(text_scale=2, text_thickness=2)
annotated_image = annotator.annotate(annotated_image, results)
sv.plot_image(annotated_image)
