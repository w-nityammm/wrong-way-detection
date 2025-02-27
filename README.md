# Wrong-Way-Detection

This project aims to detect vehicles traveling in the wrong direction using computer vision and machine learning techniques. The project also served as the foundation for [a research paper](https://ieeexplore.ieee.org/abstract/document/10725591) published in IEEE Xplore and presented at the 15th ICCCNT 2024, held at IIT Mandi from June 24 to 28, 2024.

## Project Structure

The repository contains the following key files and directories:

- `data/`: Directory containing dataset files
- `model/`: Directory for model-related files
- `number-plate-test/`: Test scripts for number plate detection
- `wrong-way-vehicle-detection-yolov8/`: YOLOv8 implementation for wrong-way vehicle detection
- `detect_wrong.py`: Main script for wrong-way detection
- `export.py`: Script to export the trained model
- `hubconf.py`: PyTorch Hub configuration
- `main.py`: Entry point of the application
- `requirements.txt`: List of Python dependencies
- `speed.py`: Script for vehicle speed estimation
- `test.py`: Test script
- `tracker.py`: Object tracking implementation
- `train.py`: Script for training the model
- `val.py`: Validation script
- `visualize.py`: Visualization utilities
- `yolov5.pt`: Pre-trained YOLOv5 weights file

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/w-nityammm/wrong-way-detection.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the wrong-way detection:

```
python main.py
```

For training the model:

```
python train.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [Unlicense License](LICENSE).
