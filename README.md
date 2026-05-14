# 🖼️ Image to Speech Converter 🔊  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue" />
  <img src="https://img.shields.io/badge/OCR-EasyOCR-green" />
  <img src="https://img.shields.io/badge/TTS-pyttsx3-orange" />
</p>

---

## 📌 Overview  

This project converts **text from images into speech** using OCR and Text-to-Speech.

- 📸 Extracts text from images  
- 🧠 Processes using OCR  
- 🔊 Converts text into audible speech  

---

## 📁 Project Structure  

```
Image-to-Speech/
│
├── images/
│   └── Text.jpg
│
├── main.py
├── requirements.txt
```

---

## ⚙️ How It Works  

1. Reads image from `images/Text.jpg`  
2. Extracts text using **EasyOCR**  
3. Converts text into speech using **pyttsx3**  
4. Plays the generated audio  

---

## 🚀 Setup & Run  

### 1️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the script  
```bash
python main.py
```

---

## 🧠 Core Code  

```python
import easyocr
import pyttsx3
from PIL import Image

reader = easyocr.Reader(['en'])

results = reader.readtext('./images/Text.jpg', detail=0)
text = " ".join(results)

print("Detected Text:\n", text)

if text.strip():
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
else:
    print("No text detected.")
```

---

## 🎯 Features  

✔ Image → Text extraction  
✔ Text → Speech conversion  
✔ Offline functionality  
✔ Beginner-friendly implementation  

---

## 🤝 Contributing  

Pull requests are welcome!  

---

## ⭐ Support  

If you like this project, consider giving it a ⭐  
