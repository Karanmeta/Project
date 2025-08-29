import cv2
import dlib
import numpy as np
import faiss
import os
import yaml
from utils import compute_distance
from database import log_attendance
import datetime

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('models/shape_predictor_68_face_landmarks.dat')
face_recognizer = dlib.face_recognition_model_v1('models/dlib_face_recognition_resnet_model_v1.dat')

# Load all enrolled embeddings into FAISS index
def load_embeddings():
    index = faiss.IndexFlatL2(128)  # 128D embeddings (from paper)
    ids = []
    for file in os.listdir('embeddings'):
        if file.endswith('.npy'):
            emb = np.load(os.path.join('embeddings', file))
            index.add(emb.reshape(1, -1))
            ids.append(file.split('.')[0])
    return index, ids

# Updated to return box, user_id, and distance for visualization
def recognize_from_image(input_data, index, ids):
    if isinstance(input_data, str):  # If path
        image = cv2.imread(input_data)
    else:  # If direct frame
        image = input_data
    
    if image is None:
        print("Error: Unable to load image/frame.")
        return None, None, None, None
    
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_detector(rgb)
    results = []  # To handle multiple faces if needed
    for face in faces:
        shape = shape_predictor(rgb, face)
        embedding = np.array(face_recognizer.compute_face_descriptor(rgb, shape)).reshape(1, -1)
        
        # Search FAISS for nearest match
        distances, indices = index.search(embedding, 1)
        dist = distances[0][0]
        if dist < config['thresholds']['distance']:
            user_id = ids[indices[0][0]]
            # Log only once per detection (can debounce in main.py)
            log_attendance(user_id, datetime.datetime.now())  # Console log
            # Return box coordinates (left, top, right, bottom) and details
            box = (face.left(), face.top(), face.right(), face.bottom())
            results.append((box, user_id, dist))
    
    if results:
        # Return the first match for simplicity (or handle multiple)
        return results[0]  # box, user_id, dist
    return None, None, None
