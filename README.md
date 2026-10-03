# 🖼️ Image to Speech Converter

<p align="center">
  <br />
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11">
  <img src="https://img.shields.io/badge/EasyOCR-Text%20Recognition-2E8B57?style=for-the-badge" alt="EasyOCR">
  <img src="https://img.shields.io/badge/pyttsx3-Text%20to%20Speech-F97316?style=for-the-badge" alt="pyttsx3">
  <br />
</p>

<p align="center">
  <strong>Turn Text Inside Images Into Spoken Words.</strong>
  <br />
  <strong>Image → Text → Speech</strong>
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#features">Features</a> ·
  <a href="#how-it-works">How It Works</a> ·
  <a href="#installation">Installation</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#roadmap">Roadmap</a>
</p>

---

## 📌 Overview

**Image to Speech Converter** is a Python-based application that transforms text embedded in images into audible speech using Optical Character Recognition (OCR) and Text-to-Speech (TTS) technologies.

The project combines **EasyOCR** and **pyttsx3** to create a simple pipeline that reads text from an image, extracts its content, and converts it into spoken audio.

Whether it's printed text, a document, or an image containing written information, the system provides a straightforward way to make visual text accessible through audio.

> **The core idea:** Making written information inside images accessible through speech.

---

## ✨ Core Features

| Feature                          | Description                                       |
| -------------------------------- | ------------------------------------------------- |
| 🖼️ Image Input                  | Reads text-containing images                      |
| 🔍 Optical Character Recognition | Extracts text using EasyOCR                       |
| 🧠 Text Processing               | Combines recognized text into readable content    |
| 🔊 Text-to-Speech                | Converts extracted text into spoken audio         |
| 🎧 Audio Playback                | Plays generated speech using pyttsx3              |
| 🖥️ Console Output               | Displays recognized text in the terminal          |
| 🌐 Language Support              | Uses EasyOCR's configurable language recognition  |
| ⚡ Simple Execution               | Runs through a single Python script               |
| 🔒 Local Processing              | Performs the main OCR and speech pipeline locally |

---

## 🧠 How It Works

The application follows a simple three-stage processing pipeline.

```text
        ┌──────────────────────┐
        │                      │
        │      Image Input     │
        │                      │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │                      │
        │      EasyOCR         │
        │                      │
        │   Text Recognition   │
        │                      │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │                      │
        │   Extracted Text     │
        │                      │
        │   Text Processing    │
        │                      │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │                      │
        │      pyttsx3         │
        │                      │
        │   Speech Generation  │
        │                      │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │                      │
        │     Audio Output     │
        │                      │
        └──────────────────────┘
```

### 1. Image Input

The application reads an image from the specified location.

### 2. Text Recognition

EasyOCR analyzes the image and identifies the text present within it.

### 3. Text Processing

The recognized text segments are combined into a single string for speech generation.

### 4. Speech Generation

The extracted text is passed to the pyttsx3 engine, which generates speech using the system's available speech engine.

### 5. Audio Playback

The generated speech is played through the available audio output device.

---

## 🧩 Core Components

### EasyOCR — Optical Character Recognition

EasyOCR is responsible for identifying and extracting text from images.

It processes the input image and returns recognized text segments that can be used by the application.

### pyttsx3 — Text-to-Speech

pyttsx3 converts the extracted text into spoken audio.

It uses the available system speech engine and supports local speech synthesis.

### Python — Application Logic

Python connects the image processing, OCR, text processing, and speech generation components into a single workflow.

---

## 📂 Project Structure

```text
Image-to-Speech/
│
├── images/
│   └── Text.jpg                 # Sample input image
│
├── main.py                      # Main application
├── requirements.txt             # Python dependencies
│
├── README.md                    # Project documentation
├── CONTRIBUTING.md              # Contribution guidelines
├── SECURITY.md                  # Security policy
└── LICENSE                      # Project license
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.11
* pip
* Git
* An image containing readable text
* Audio output device

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YashPalkandwar1908/Image-to-Speech.git

cd Image-to-Speech
```

### 2. Create a Virtual Environment

**Windows**

```powershell
python -m venv venv

venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Add Your Image

Place your image inside the `images/` directory.

The current implementation uses:

```text
images/Text.jpg
```

### 2. Run the Application

```bash
python main.py
```

### 3. View the Extracted Text

The recognized text will be displayed in the terminal.

### 4. Listen to the Speech

If text is successfully detected, the application will convert it into speech and play the audio.

---

## 💻 Application Example

### Input

<details>
<summary>Sample input image</summary>

```text
images/Text.jpg
```

</details>

### Processing

```text
Input Image
    │
    ▼
EasyOCR
    │
    ▼
Recognized Text
    │
    ▼
Text Processing
    │
    ▼
pyttsx3
    │
    ▼
Spoken Audio
```

### Output

```text
Detected Text:

[Text recognized from the input image]

Playing generated speech...
```

---

## 🛠️ Technology Stack

| Category              | Technology  | Purpose                      |
| --------------------- | ----------- | ---------------------------- |
| Programming Language  | Python 3.11 | Application logic            |
| OCR Engine            | EasyOCR     | Extracting text from images  |
| Text-to-Speech        | pyttsx3     | Converting text into speech  |
| Image Processing      | Pillow      | Image handling               |
| Dependency Management | pip         | Installing required packages |

---

## 🔍 Important Files

### `main.py`

The main application script responsible for initializing EasyOCR, reading the input image, extracting text, and generating speech.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `images/Text.jpg`

Sample image used as the input for OCR processing.

---

## 🔮 Roadmap

The project can be extended with the following capabilities:

| Feature                   | Description                                      |
| ------------------------- | ------------------------------------------------ |
| 📁 Multiple Image Support | Process multiple images in one execution         |
| 📄 PDF Support            | Extract and read text from PDF documents         |
| 🌍 Multilingual OCR       | Support additional OCR languages                 |
| 🎙️ Voice Selection       | Allow users to select available speech voices    |
| ⚡ Speech Speed Control    | Adjust speech playback rate                      |
| 💾 Audio Export           | Save generated speech as an audio file           |
| 🖥️ GUI Interface         | Introduce a graphical user interface             |
| 📷 Live Camera Input      | Extract and read text directly from camera feeds |
| 🔍 Image Preprocessing    | Improve recognition through image enhancement    |
| ♿ Accessibility Features  | Improve usability for visually impaired users    |

---

## ⚠️ Current Limitations

The current implementation is a lightweight image-to-speech application.

Its performance depends on:

* Image resolution and quality
* Text visibility and readability
* Font size and formatting
* Lighting and image contrast
* OCR recognition accuracy
* Availability of a compatible system speech engine

The application currently uses a predefined image path rather than an interactive image-upload interface.

---

<p align="center">
  <strong>Built with Python, OCR & Text-to-Speech ❤️</strong>
  <br />
  <sub>Making text in images accessible through audio.</sub>
</p>
