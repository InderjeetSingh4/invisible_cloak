from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import time

app = Flask(__name__)

# --- Global variables for state management ---
cap = None
background_frame = None
camera_active = False # State variable to control camera activity
selected_color = 'blue'

# Color ranges dictionary
color_ranges = {
    'red': ([0, 120, 70], [10, 255, 255], [170, 120, 70], [180, 255, 255]),
    'green': ([35, 100, 100], [85, 255, 255]),
    'blue': ([90, 100, 100], [130, 255, 255]),
    'yellow': ([20, 100, 100], [30, 255, 255]),
    'pink': ([140, 100, 100], [170, 255, 255]),
    'white': ([0, 0, 200], [180, 30, 255])
}

def create_placeholder_image(text):
    """Creates a black image with centered white text."""
    placeholder = np.zeros((720, 1280, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    (text_width, text_height), baseline = cv2.getTextSize(text, font, 2, 3)
    x = (1280 - text_width) // 2
    y = (720 + text_height) // 2
    cv2.putText(placeholder, text, (x, y), font, 2, (255, 255, 255), 3, cv2.LINE_AA)
    return placeholder

def capture_background_logic():
    """Captures the background. Assumes camera is already active."""
    global background_frame
    print("--- 📸 Capturing background in 5 seconds... ---")
    time.sleep(5)
    ret, frame = cap.read()
    if ret:
        background_frame = cv2.flip(frame, 1)
        print("--- ✅ Background captured successfully! ---")
    else:
        print("--- ❌ Failed to capture background. ---")

def generate_frames():
    """Generates video frames. If camera is inactive, yields a placeholder."""
    while True:
        if not camera_active or not cap.isOpened():
            placeholder = create_placeholder_image("Camera is Off")
            ret, buffer = cv2.imencode('.jpg', placeholder)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            time.sleep(0.1)
            continue

        ret, current_frame = cap.read()
        if not ret or background_frame is None:
            continue

        frame_flipped = cv2.flip(current_frame, 1)
        
        # --- THIS IS THE CORRECTED LINE ---
        hsv = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2HSV)
        
        range_data = color_ranges.get(selected_color, color_ranges['blue'])
        if selected_color == 'red':
            lower1, upper1, lower2, upper2 = [np.array(x) for x in range_data]
            mask1, mask2 = cv2.inRange(hsv, lower1, upper1), cv2.inRange(hsv, lower2, upper2)
            final_mask = mask1 + mask2
        else:
            lower, upper = [np.array(x) for x in range_data]
            final_mask = cv2.inRange(hsv, lower, upper)
        kernel = np.ones((5, 5), np.uint8)
        final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_DILATE, kernel, iterations=1)
        inverted_mask = cv2.bitwise_not(final_mask)
        foreground = cv2.bitwise_and(frame_flipped, frame_flipped, mask=inverted_mask)
        background_replacement = cv2.bitwise_and(background_frame, background_frame, mask=final_mask)
        result = cv2.add(foreground, background_replacement)
        ret, buffer = cv2.imencode('.jpg', result)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/start_camera')
def start_camera():
    global camera_active
    if not camera_active:
        camera_active = True
        print("Camera started by user.")
        capture_background_logic()
    return jsonify(success=True)

@app.route('/stop_camera')
def stop_camera():
    global camera_active
    camera_active = False
    print("Camera stopped by user.")
    return jsonify(success=True)

@app.route('/recapture_background')
def recapture_background():
    if camera_active:
        capture_background_logic()
        return jsonify(success=True)
    return jsonify(success=False, message="Camera is not active.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_color/<color_name>')
def set_color(color_name):
    global selected_color
    selected_color = color_name
    return jsonify(success=True)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam. Check index or permissions.")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    print("Server started. Camera is ready.")
    app.run(debug=True, port=5001)

  