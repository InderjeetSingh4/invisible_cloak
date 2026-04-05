# 🪄 Invisible Clock Web App

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A real-time web application that recreates the famous "Invisibility Clock" effect using Computer Vision. This project detects a specific color in a live webcam stream and dynamically replaces it with a static background image, making objects of that color appear completely invisible.

> **💡 Note:** *[Add a GIF or screenshot of the app working here!]*

---

## ✨ Features

* **🎥 Real-Time Video Processing:** Creates a zero-lag invisibility effect live from your webcam feed.
* **🎨 Dynamic Color Selection:** Easily switch the target cloak color (Red, Green, Blue, Yellow, Pink, White) via a user-friendly web interface.
* **⚙️ Interactive Web Controls:** Asynchronous buttons to start/stop the camera and recapture the background on the fly.
* **🌙 Clean, Modern UI:** A responsive, dark-themed interface built for a seamless user experience.
* **🔌 Flask-Powered Backend:** A robust and lightweight server architecture handling heavy video frame processing and frontend streaming.

---

## 🧠 How It Works (Client-Server Architecture)

1.  **Backend (Python, Flask, OpenCV):** When the app starts, OpenCV captures a clean, static image of the background. For every subsequent frame, it generates a color mask based on the user's selected "invisible" color. The app then blends the live feed with the static background, effectively erasing the colored object.
2.  **Frontend (HTML, CSS, JS):** The UI displays the processed video stream. JavaScript handles asynchronous Fetch API calls to communicate with the Flask server without reloading the page, allowing for dynamic color switching and camera controls.

---

## 🚀 Setup and Installation

### Prerequisites
* Python 3.7+
* A connected webcam

### Installation Steps

**1. Clone the repository:**
`git clone https://github.com/InderjeetSingh4/invisible_cloak_web.git`
`cd invisible_cloak_web`

**2. Create and activate a virtual environment:**
* **Windows:**
`python -m venv venv`
`.\venv\Scripts\activate`

* **macOS / Linux:**
`python3 -m venv venv`
`source venv/bin/activate`

**3. Install the required dependencies:**
`pip install Flask opencv-python numpy`

**4. Run the application:**
`python app.py`

Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## 🎮 How to Use

1.  Click the **"Start Camera"** button on the web interface.
2.  The application will show a 5-second countdown. **Move completely out of the frame** so the system can capture a clean background image.
3.  Step back into the frame and hold up an object matching the selected color (Default is Blue). Watch it disappear!
4.  Use the color palette at the bottom to dynamically change the invisible color.
5.  If the lighting changes, simply click **"Recapture"** and step out of the frame again.

---

## 📂 File Structure

```text
.
├── app.py              # Main Flask server, video processing, and routing
├── static/
│   ├── style.css       # Dark-themed UI styling
│   └── script.js       # Frontend interactivity and Fetch API logic
└── templates/
    └── index.html      # Main user interface layout
