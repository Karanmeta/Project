# Face Recognition Attendance System

A real-time face recognition attendance system built with Python, OpenCV, and dlib. This system can enroll faces from images and perform real-time recognition using a webcam for attendance tracking.

## 🚀 Features

- **Face Enrollment**: Automatically enroll multiple people by organizing their images in folders
- **Real-time Recognition**: Live face recognition using webcam with bounding box visualization
- **Attendance Logging**: Automatic attendance marking with timestamp logging
- **High Accuracy**: Uses dlib's ResNet-based face recognition model for robust performance
- **Efficient Search**: FAISS integration for fast similarity search across enrolled faces
- **Image Augmentation**: Support for various image augmentations to improve recognition robustness
- **Configurable Thresholds**: Adjustable distance and confidence thresholds via YAML configuration

## 📋 Requirements

- Python 3.10+
- OpenCV 4.8.0.74
- dlib 19.22.99
- NumPy 1.24.3
- FAISS-CPU 1.7.4
- PyMongo 4.3.3 (for future database integration)
- PyYAML 6.0

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Karanmeta/Project.git
   cd Project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download required models** (if not included)
   - The system uses pre-trained dlib models stored in the `models/` directory
   - `shape_predictor_68_face_landmarks.dat`
   - `dlib_face_recognition_resnet_model_v1.dat`

## 📁 Project Structure

```
Project/
├── images/                     # Training images organized by person
│   ├── Karan Mehta/           # Person 1's images
│   ├── Pawankumar Navinchandra/  # Person 2's images
│   └── Yashesh Patel/         # Person 3's images
├── embeddings/                # Generated face embeddings (.npy files)
├── models/                    # Pre-trained dlib models
│   ├── shape_predictor_68_face_landmarks.dat
│   └── dlib_face_recognition_resnet_model_v1.dat
├── myenv/                     # Virtual environment
├── __pycache__/              # Python cache files
├── .vscode/                  # VS Code settings
├── main.py                   # Real-time recognition script
├── enroll.py                 # Face enrollment script
├── recognize.py              # Recognition logic
├── database.py               # Attendance logging
├── utils.py                  # Utility functions
├── test.py                   # Testing script
├── config.yaml               # Configuration file
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🎯 Usage

### 1. Prepare Training Data

Organize your training images in the following structure:
```
images/
├── PersonName1/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
├── PersonName2/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
```

The system supports various image augmentations (blur, rotation, noise, etc.) as seen in the sample data.

### 2. Enroll Faces

Run the enrollment script to process all images and generate face embeddings:

```bash
python enroll.py
```

This will:
- Process all person folders in the `images/` directory
- Extract face embeddings using dlib's ResNet model
- Save averaged embeddings to the `embeddings/` folder
- Display enrollment summary with success/failure counts

### 3. Start Real-time Recognition

Launch the real-time attendance system:

```bash
python main.py
```

This will:
- Initialize your webcam
- Perform real-time face detection and recognition
- Display bounding boxes around detected faces
- Show person names and accuracy scores
- Log attendance with timestamps
- Press 'q' to quit

## ⚙️ Configuration

Edit `config.yaml` to adjust system parameters:

```yaml
thresholds:
  distance: 0.6    # Euclidean distance threshold for face matching
  confidence: 0.9  # Minimum confidence for face detection

images:
  folder: "images/"  # Path to training images
```

## 🔧 Core Components

### Face Enrollment (`enroll.py`)
- Automatically processes all person folders
- Extracts 128-dimensional face embeddings
- Handles multiple images per person with averaging
- Validates single-face images for quality control

### Real-time Recognition (`main.py`)
- Captures live video from webcam
- Processes frames for face detection
- Performs similarity search using FAISS
- Renders bounding boxes and labels
- Implements debouncing for attendance logging

### Recognition Engine (`recognize.py`)
- Core face recognition logic
- FAISS index management for efficient search
- Distance-based matching with configurable thresholds
- Returns bounding box coordinates and match confidence

### Attendance Logging (`database.py`)
- Currently logs to console with timestamps
- Designed for easy integration with databases (MongoDB ready)
- Expandable for file-based or cloud logging

## 🎨 Current Enrolled Users

The system currently has embeddings for:
- Karan Mehta
- Pawankumar Navinchandra  
- Yashesh Patel

Each person has multiple training images including various augmentations for robust recognition.

## 🚀 Future Enhancements

- [ ] Database integration for persistent attendance records
- [ ] Web dashboard for attendance management
- [ ] Multiple camera support
- [ ] Real-time attendance alerts
- [ ] Face anti-spoofing detection
- [ ] REST API for integration with other systems
- [ ] Mobile app companion

## 📊 Performance

- **Recognition Speed**: Real-time processing (30+ FPS)
- **Accuracy**: High accuracy with dlib's ResNet model
- **Scalability**: FAISS enables efficient search across large datasets
- **Memory Efficient**: Compact 128D embeddings per person

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Dependencies Credits

- **OpenCV**: Computer vision library for image processing
- **dlib**: Face detection and recognition models
- **FAISS**: Efficient similarity search and clustering
- **NumPy**: Numerical computing support

## 📞 Support

For issues and questions:
1. Check existing GitHub issues
2. Create a new issue with detailed description
3. Include system information and error logs
