# Subtitle-Synchronizer

```markdown
# Subtitle Synchronizer

## Overview
Subtitle Synchronizer is a Flask-based web application that allows users to upload a video file, extract subtitles, and adjust the timing of the subtitles based on a user-specified offset. The synchronized subtitles can then be downloaded.

## Features
- Upload video files in mp4, mkv, or avi formats.
- Extract subtitles from the uploaded video.
- Synchronize subtitles by adjusting the offset in seconds.
- Download the corrected subtitle file.

## Technologies Used
- Python 3.x
- Flask
- ffmpeg
- pysrt
- HTML/CSS/JavaScript

## Prerequisites
- Python 3.x
- ffmpeg

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/sahilawatramani/subtitle-sync.git
   cd subtitle-sync
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download and Install ffmpeg**
   - Download ffmpeg from the official site: https://ffmpeg.org/download.html
   - Extract the files and place them in a directory (e.g., `C:\ffmpeg\`).
   - Add the `bin` directory (e.g., `C:\ffmpeg\bin`) to your system's PATH environment variable.

5. **Create Uploads Directory**
   Ensure there is an `uploads` directory in the project root:
   ```bash
   mkdir uploads
   ```

## Configuration
- Modify the `UPLOAD_FOLDER` and `ffmpeg_path` in the `app.py` file to match your local setup if necessary.

## Usage
1. **Run the Flask Application**
   ```bash
   flask run
   ```
   By default, the application runs on `http://127.0.0.1:5000/`.

2. **Access the Web Application**
   Open a web browser and navigate to `http://127.0.0.1:5000/`.

3. **Upload a Video and Synchronize Subtitles**
   - Choose a video file (mp4, mkv, or avi).
   - Enter the subtitle offset in seconds (e.g., -2, 3).
   - Click the "Upload and Synchronize" button.
   - If successful, download the corrected subtitle file.

## Project Structure
- `app.py`: Main Flask application.
- `templates/index.html`: HTML template for the home page.
- `static/css/style.css`: CSS for styling the web page.
- `static/js/script.js`: JavaScript for form validation.
- `requirements.txt`: List of Python packages required for the project.
- `uploads/`: Directory to store uploaded and processed files.

## Error Handling
- Flash messages are used to display errors and notifications to the user.
- Common errors include:
  - No file uploaded.
  - Invalid file format.
  - No subtitles found in the video.
  - ffmpeg errors during subtitle extraction.

## Contributing
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Make your changes and commit them (`git commit -m 'Add new feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [ffmpeg](https://ffmpeg.org/)
- [pysrt](https://pypi.org/project/pysrt/)

```

