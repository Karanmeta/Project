import streamlit as st
import cv2
import pickle
import time
import numpy as np
from recognize import recognize_from_image

# Load embeddings (model.pkl)
with open("model.pkl", "rb") as f:
    index, ids = pickle.load(f)

st.title("📷 Real-Time Face Recognition Attendance System")

# Start/stop button
run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])  # placeholder for frames
log_placeholder = st.empty()  # placeholder for logging user ID

cap = None
last_log_time = 0
debounce_interval = 1  # log every 1 second

if run:
    cap = cv2.VideoCapture(0)
    while run and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("⚠️ Camera not accessible")
            break

        # Recognition
        box, user_id, dist = recognize_from_image(frame, index, ids)

        if user_id:
            current_time = time.time()
            if current_time - last_log_time > debounce_interval:
                log_placeholder.success(f"✅ Match: {user_id} (Acc: {1 - dist:.2f})")
                last_log_time = current_time

            # Draw bounding box
            if box:
                left, top, right, bottom = box
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                label = f"{user_id} ({1 - dist:.2f})"
                cv2.putText(
                    frame, label, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2
                )
        else:
            log_placeholder.error("❌ No match found")

        # Convert to RGB for Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

    cap.release()
else:
    st.write("▶️ Click 'Start Camera' to begin recognition")
