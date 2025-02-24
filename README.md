# Arabic PDF OCR App

This Python application converts an Arabic PDF into images, extracts text from each page using Optical Character Recognition (OCR), and saves the extracted text to a `.txt` file. The app uses PyMuPDF, Tesseract OCR, and Python libraries like Pillow for seamless functionality.

---

## Features

- Converts each page of a PDF into images.
- Performs OCR on Arabic text using Tesseract OCR.
- Automatically sorts pages numerically.
- Deletes processed images after OCR.
- Outputs a `.txt` file with the extracted text.

---

## Requirements

### 1. Software

- **Python** (version 3.7 or later)
- **Tesseract OCR** (with Arabic language pack)

### 2. Python Libraries

Install these using pip:

```bash
pip install PyMuPDF Pillow pytesseract
```

---

## Installation

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/omarashrafdev/arabic-pdf-ocr.git
cd arabic-pdf-ocr
```

### **Step 2: Install Dependencies**

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## Platform-Specific Instructions

### **Windows**

1. Download and install [Tesseract OCR for Windows](https://github.com/tesseract-ocr/tesseract).
   - Add Tesseract’s installation directory (e.g., `C:\Program Files\Tesseract-OCR\`) to the system PATH:
     - Press `Win + R` → Type `sysdm.cpl` → Go to **Advanced** → **Environment Variables** → Edit `Path`.
2. Ensure the Arabic language pack is installed:
   - Download `ara.traineddata` from [Tesseract Data Files](https://github.com/tesseract-ocr/tessdata).
   - Copy it to the `tessdata` directory inside Tesseract's installation path.

Verify installation by running:

```bash
tesseract --version
tesseract --list-langs
```

---

### **Linux (e.g., Ubuntu, Fedora)**

1. Install Tesseract and the Arabic language pack:
   ```bash
   sudo apt install tesseract-ocr tesseract-ocr-ara   # Ubuntu
   sudo dnf install tesseract tesseract-langpack-ara  # Fedora
   ```
2. Verify the installation:
   ```bash
   tesseract --version
   tesseract --list-langs
   ```

---

### **macOS**

1. Install Tesseract using Homebrew:
   ```bash
   brew install tesseract
   brew install tesseract-lang
   ```
2. Ensure the Arabic language pack is installed:
   - Arabic is included with the default installation, but you can check with:
     ```bash
     tesseract --list-langs
     ```

---

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Enter the path to your Arabic PDF when prompted:
   ```
   Enter the path to the Arabic PDF file: path/to/your/file.pdf
   ```
3. The app will:

   - Save images for each page in the `pdf_images` directory.
   - Perform OCR on each image.
   - Save the extracted text to `output_text.txt`.
   - Delete the processed images.

4. The output will be stored in `output_text.txt` in the same directory.

---

## Example Output

Sample structure of the output file:

```
--- Page: page_1.png ---
Extracted Arabic text for page 1...

--- Page: page_2.png ---
Extracted Arabic text for page 2...
```

---

## Known Issues

1. If the text quality in the PDF is poor, OCR accuracy may be reduced.
2. Processing very large PDFs might require additional memory.

---

## Contributing

Feel free to open issues or submit pull requests for improvements. Make sure to follow the coding standards and include proper documentation.

---

## License

This project is licensed under the [MIT License](LICENSE).
