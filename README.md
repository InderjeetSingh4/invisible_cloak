# invisible_clock_web
Real-Time Invisible Cloak with Python, OpenCV, and Flask
This project is a web-based application that creates a real-time "invisible cloak" effect using a webcam. It uses computer vision techniques to detect a specific color in the video stream and replace it with a static background image, making objects of that color appear invisible.

How It Works
The application is built on a client-server model:

Backend (Python & Flask): A Flask web server uses OpenCV to access the webcam. When the application starts, it first captures a static image of the background. Then, for each subsequent frame from the webcam, it performs color detection. A mask is generated for the selected "invisible" color. This mask is then used to combine the live video feed with the initial background image, effectively replacing the colored object with the background. The resulting video is streamed to the frontend.

Frontend (HTML, CSS, JavaScript): A simple web interface displays the video stream. It provides controls for the user to start/stop the camera, recapture the background (if the lighting or scene changes), and select which color to make invisible from a color palette. JavaScript handles the user interactions and communicates with the Flask backend asynchronously using the Fetch API.

Features
Real-Time Video Processing: Creates the invisibility effect live from your webcam feed.

Dynamic Color Selection: Easily switch the color of the cloak (Red, Green, Blue, Yellow, Pink, White) via a user-friendly interface.

Interactive Web Controls: Buttons to start the camera, stop the camera, and recapture the background.

Clean, Modern UI: A responsive and dark-themed interface for a better user experience.

Flask-Powered Backend: A robust and simple backend to handle video processing and streaming.

Technologies Used
Backend:

Python

Flask

OpenCV-Python

NumPy

Frontend:

HTML5

CSS3

JavaScript

Setup and Installation
Follow these steps to run the project on your local machine.

Prerequisites:

Python 3.7+

pip (Python package installer)

A webcam connected to your computer.

Installation Steps:

Clone the repository:

Bash

git clone https://github.com/ChiragAvasthi/invisible_cloak_web.git
cd invisible-cloak
Create and activate a virtual environment (recommended):

Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
macOS / Linux:

Bash

python3 -m venv venv
source venv/bin/activate
Install the required Python packages:
Create a requirements.txt file with the following content:

Flask
opencv-python
numpy
Then, install the packages:

Bash

pip install -r requirements.txt
Run the Flask application:

Bash

python app.py
Access the application:
Open your web browser and go to http://127.0.0.1:5000 or the address shown in your terminal.

How to Use
Once the application is running, open the web page.

Click the "Start Camera" button.

The application will show a 5-second countdown. Move completely out of the camera's view during this time so it can capture a clean background image.

After the background is captured, step back in front of the camera.

Hold up an object that matches the selected color (the default is blue). The object should now appear "invisible," showing the background behind it.

Click on the color swatches at the bottom to change which color is made invisible.

If the lighting changes or you want to reset the background, click the "Recapture" button and move out of the frame again.

Click "Off Camera" to stop the video feed.

File Structure
.
├── app.py              # Main Flask application, handles all backend logic and video processing.
├── static/
│   ├── style.css       # CSS for styling the web interface.
│   └── script.js       # JavaScript for frontend interactivity and API calls.
└── templates/
    └── index.html      # The main HTML file for the user interface.







