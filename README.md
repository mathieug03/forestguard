# ForestGuard

**A student prototype exploring computer vision and mapping for forest-fire monitoring.**

Built for **AVEVA EcoTech Emerge**, where our team reached the **top 10**.

![ForestGuard concept](docs/images/concept.jpg)

## The prototype

Two independent components demonstrate the idea:

- **Image detection:** select an image file or URL, call a hosted Roboflow model, and display annotated detections.
- **Map dashboard:** add coordinates and a message from a Python interface to a Leaflet map through Eel.

The broader concept combines satellite imagery, weather data, and risk prediction. This prototype demonstrates image detection and manual map updates; the full monitoring pipeline remained a proposed next step.

We also explored a local YOLO-based detector as an alternative to Roboflow. Reliable wildfire detection would have required substantial fine-tuning on a dedicated, annotated dataset, so this approach remained experimental.

## Demo screenshots

![Detection output from our recorded prototype demo](docs/images/detection.jpg)

![Map dashboard from our recorded prototype demo](docs/images/dashboard.jpg)

Screenshots are from the team's January 2025 demonstration. The concept image comes from the competition presentation.

## Run locally

The prototype uses Python 3.12, Tkinter, and Chrome for the Eel window.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ROBOFLOW_API_KEY="your-own-key"
python detector.py
```

The detector uses a hosted Roboflow model and requires your own credentials and model access.

For the independent map demo:

```bash
cd dashboard
python main.py
```

Internet access is needed for inference and map assets. The Paris and Los Angeles markers are demonstration coordinates. `experiments/webcam.py` contains the generic local YOLO experiment; wildfire-specific weights and training data are not included.

## Team

Mathieu Gautier, Daouda Keita, and Farhan Zaveri.
