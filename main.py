import easyocr
import pyttsx3
from PIL import Image

# Initialize OCR reader
reader = easyocr.Reader(['en'])

# Read text from image
results = reader.readtext('./images/Text.jpg', detail=0)
text = " ".join(results)
print("Detected Text:\n", text)

# Convert text to speech
if text.strip():
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
else:
    print("No text detected.")
