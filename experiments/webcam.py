import cv2
from inference import get_model
import supervision as sv
from inference.core.utils.image_utils import load_image_bgr

model = get_model(model_id="yolov8l-640")
annotator_box = sv.BoxAnnotator(thickness=4)
annotator_label = sv.LabelAnnotator(text_scale=2, text_thickness=2)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.infer(frame)[0]
    results = sv.Detections.from_inference(results)
    annotated_frame = annotator_box.annotate(frame, results)
    annotated_frame = annotator_label.annotate(annotated_frame, results)

    cv2.imshow('Webcam Live Demo', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
