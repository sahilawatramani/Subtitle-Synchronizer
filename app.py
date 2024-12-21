import os
import subprocess
import logging
from flask import Flask, request, render_template, send_file, flash, redirect

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Define folder for uploaded files
UPLOAD_FOLDER = 'C:\\Users\\Victus\\OneDrive\\Desktop\\subtitle-sync\\uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions for video uploads
ALLOWED_EXTENSIONS = {'mp4', 'mkv', 'avi'}

# Configure logging
logging.basicConfig(level=logging.DEBUG)


def allowed_file(filename):
    """Check if a file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    print("Rendering index.html")
    """Render the home page."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    """Handle video uploads and subtitle synchronization."""
    try:
        video_file = request.files.get('video')
        offset = int(request.form.get('offset', 0))

        if not video_file:
            flash("No video file uploaded.")
            return redirect('/')

        if not allowed_file(video_file.filename):
            flash("Invalid video file format. Allowed formats: mp4, mkv, avi.")
            return redirect('/')

        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
        video_file.save(video_path)

        # Extract subtitles from the video
        subtitle_path = os.path.join(app.config['UPLOAD_FOLDER'], 'extracted_subtitles.srt')
        ffmpeg_path = "C:\\Users\\Victus\\Downloads\\ffmpeg-7.1-essentials_build\\ffmpeg-7.1-essentials_build\\bin\\ffmpeg.exe"
        extract_command = [ffmpeg_path, '-i', video_path, '-map', '0:s:0', subtitle_path]
        result = subprocess.run(extract_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0 or not os.path.exists(subtitle_path):
            flash("No subtitles found in the video.")
            return redirect('/')

        # Synchronize subtitles with the given offset
        corrected_subtitle_path = os.path.join(app.config['UPLOAD_FOLDER'], 'corrected_subtitles.srt')
        synchronize_subtitles(subtitle_path, corrected_subtitle_path, offset)

        flash("Subtitle synchronization successful! Download your file below.")
        return send_file(corrected_subtitle_path, as_attachment=True)
    except Exception as e:
        logging.error("An error occurred:", exc_info=e)
        flash(f"An error occurred: {e}")
        return redirect('/')


def synchronize_subtitles(input_srt, output_srt, offset=0):
    """Synchronize subtitle timing by adjusting offsets."""
    import pysrt
    subs = pysrt.open(input_srt)
    for sub in subs:
        sub.start.seconds += offset
        sub.end.seconds += offset
    subs.save(output_srt)


if __name__ == '__main__':
    app.run(debug=True)
