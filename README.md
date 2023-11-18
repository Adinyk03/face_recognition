# Face Recognition Attendance System


Welcome to the Face Recognition Attendance System repository! This Python-based system automates attendance marking using facial recognition technology. By leveraging OpenCV and face_recognition libraries, it recognizes faces in real-time via a webcam and logs attendance details into a CSV file.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [CSV File (Attendance)](#csv-file-attendance)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Face Recognition Attendance System is a Python application that utilizes OpenCV and face_recognition libraries to recognize faces in real-time through a webcam. It provides functionalities to mark attendance automatically while maintaining a record of attendance in a CSV file.

## Features

- **Real-time Face Recognition:** Utilizes a webcam to recognize registered faces and mark attendance.
- **Image-based Face Recognition:** Offers a basic script (`basic.py`) for testing face recognition on sample images.
- **Attendance Logging:** Records attendance with timestamps in a CSV file (`Attendance.csv`).

## Installation

### Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- face_recognition
- numpy

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Adinyk03/face_recognition.git
    cd face_recognition
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Attendance System:**

    - Add images of individuals to the `ImagesAttendance` folder.
    - Run `attendance.py` to start the system and mark attendance using a webcam.
    - To exit the system, press 'q'.

2. **Basic Face Recognition:**

    - Run `basic.py` to test face recognition functionality on sample images in the `ImagesBasic` folder.
    - Observe the output displaying comparison results and face distance.

## Folder Structure

- **ImagesAttendance:** Store images for face registration and attendance marking.
- **ImagesBasic:** Contains sample images for basic face recognition testing.

## CSV File (Attendance)

The `Attendance.csv` file maintains attendance details in the following format:

```
Name,Date,Time
ADITYA NAYAK,2023-11-17,22:06:08
Unknown,2023-11-17,22:06:10
AMMA,2023-11-17,22:06:22
ADITYA NAYAK,2023-11-18,10:26:14
Unknown,2023-11-18,10:26:18
AMMA,2023-11-18,10:26:19
AJJA,2023-11-18,10:26:29
ADITYA NAYAK,2023-11-18,15:28:22
```

The CSV file contains entries for each attendance record, including the person's name, date, and timestamp.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We acknowledge the contributors, libraries, and resources that have contributed to this project's development.

