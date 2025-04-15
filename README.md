
# Surface_Crack Detection

## 📌 Project Overview

This repository contains a surface crack detection system developed using deep learning techniques. The goal is to automate the identification of surface cracks in infrastructure such as roads, walls, and buildings to improve maintenance efficiency and safety.

## 📁 Repository Structure

```
.
├── Surface_Crack/                           # Source code and utilities
├── crack dataset/                           # Dataset used for training and testing
├── .gitattributes                           # Git LFS attributes
├── README.md                                # Project documentation
├── crack detection final code-checkpoint.ipynb  # Checkpoint for the main notebook
├── crack detection final code.ipynb         # Main Jupyter Notebook for training & testing
├── crack video .mp4                         # Demo video of the detection process
```

## ⚙️ Features

- Image classification using deep learning (CNN-based approach)
- Real-time surface crack detection demo
- Dataset preprocessing and augmentation
- Evaluation metrics and visualization

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- Jupyter Notebook
- Git Large File Storage (LFS)

## 📂 Dataset

The dataset used in this project is included in the `crack dataset/` directory and contains images of cracked and non-cracked surfaces.

## 🚀 Getting Started

### Prerequisites

Make sure the following dependencies are installed:

```bash
pip install tensorflow opencv-python matplotlib numpy
```

### Run the Project

1. Clone the repository:
```bash
git clone https://github.com/your-username/Surface_Crack_Detection.git
cd Surface_Crack_Detection
```

2. Launch the notebook:
```bash
jupyter notebook "crack detection final code.ipynb"
```

3. Optionally, watch the demo video: `crack video.mp4`

## 📊 Results

The model achieved high accuracy on the validation dataset with good generalization on unseen images. Visualizations of predictions and evaluation metrics are available in the notebook.

## 🎥 Demo

A short video showcasing the surface crack detection process is included in the repository.

## 📌 Future Work

- Integrate with a mobile/web app for real-time detection
- Expand the dataset with diverse surface conditions
- Improve model accuracy and reduce false positives

## 🙋‍♂️ Author

**Dinesh110205**  
Feel free to reach out for collaborations or suggestions.

## 📄 License

This project is licensed under the MIT License.
