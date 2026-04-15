from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from predict import predict_disease
import traceback

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Check if file is in request
        if "leaf_image" not in request.files:
            return render_template("result.html", result={
                "disease_detected": False,
                "disease_name": "Upload Error",
                "disease_type": "Error",
                "severity": "none",
                "confidence": 0,
                "symptoms": ["No file uploaded"],
                "possible_causes": [],
                "treatment": ["Please select an image and try again"],
                "error": "No file provided"
            })

        file = request.files["leaf_image"]

        # Check if filename is empty
        if file.filename == "":
            return render_template("result.html", result={
                "disease_detected": False,
                "disease_name": "Upload Error",
                "disease_type": "Error",
                "severity": "none",
                "confidence": 0,
                "symptoms": ["No file selected"],
                "possible_causes": [],
                "treatment": ["Please select an image file and try again"],
                "error": "Empty filename"
            })

        # Check file extension
        if not allowed_file(file.filename):
            return render_template("result.html", result={
                "disease_detected": False,
                "disease_name": "File Format Error",
                "disease_type": "Error",
                "severity": "none",
                "confidence": 0,
                "symptoms": ["Invalid file format"],
                "possible_causes": [],
                "treatment": ["Please upload JPG, PNG, JPEG, GIF, or BMP files only"],
                "error": "Unsupported file type"
            })

        # Check file size
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        file.seek(0)
        
        if file_size > MAX_FILE_SIZE:
            return render_template("result.html", result={
                "disease_detected": False,
                "disease_name": "File Size Error",
                "disease_type": "Error",
                "severity": "none",
                "confidence": 0,
                "symptoms": ["File too large"],
                "possible_causes": [],
                "treatment": ["Please upload images smaller than 10MB"],
                "error": "File exceeds size limit"
            })

        
        filename = secure_filename(file.filename)
        # Add timestamp to make filename unique
        import time
        filename = f"{int(time.time())}_{filename}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Call AI model for prediction
        result = predict_disease(filepath)

        # Clean up: delete uploaded file after analysis
        try:
            os.remove(filepath)
        except:
            pass

        return render_template("result.html", result=result)

    except Exception as e:
        print(f"Error: {traceback.format_exc()}")
        return render_template("result.html", result={
            "disease_detected": False,
            "disease_name": "Processing Error",
            "disease_type": "Error",
            "severity": "none",
            "confidence": 0,
            "symptoms": [f"An error occurred: {str(e)}"],
            "possible_causes": [],
            "treatment": ["Please try uploading the image again"],
            "error": str(e)
        })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.errorhandler(404)
def not_found(error):
    return render_template("index.html"), 404

@app.errorhandler(500)
def server_error(error):
    return render_template("result.html", result={
        "disease_detected": False,
        "disease_name": "Server Error",
        "disease_type": "Error",
        "severity": "none",
        "confidence": 0,
        "symptoms": ["Server error occurred"],
        "possible_causes": [],
        "treatment": ["Please refresh the page and try again"],
        "error": "Internal server error"
    }), 500

if __name__ == "__main__":
    print("🚀 Starting Leaf Disease Analyzer...")
    print("📱 Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)