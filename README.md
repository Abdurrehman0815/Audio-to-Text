# **Speech-to-Text Transcription Web App**  

## **Overview**  
This project is a **Flask-based web application** that allows users to upload an audio file and receive a transcribed text output. It provides a **simple, fast, and efficient speech-to-text conversion** using OpenAI’s **Whisper** model. The application features a **modern, interactive UI with a dark theme and gradient design**, built using **Tailwind CSS** for an enhanced user experience.  

---

## **Features**  
✔ **Upload and Transcribe Audio** – Users can upload an audio file, and the system will generate a transcribed text output.  
✔ **Fast and Efficient Processing** – Uses **Whisper (tiny)** model for quick and accurate transcription.  
✔ **Minimal and Interactive UI** – Designed with **Tailwind CSS**, featuring a **dark theme with gradients** for better user interaction.  
✔ **Fully Flask-Based** – The entire backend is built with **Flask**, ensuring lightweight and scalable deployment.  
✔ **Auto-Cleanup** – Deletes processed audio files after transcription to optimize storage.  

---

## **Technology Stack**  

### **Frontend**  
- **HTML5, CSS3 (Tailwind CSS)** – Provides a visually appealing, dark-themed UI with smooth user interaction.  
- **JavaScript (Fetch API)** – Handles form submission and server communication.  

### **Backend**  
- **Flask (Python)** – Manages routes and processes transcription requests.  
- **Whisper (tiny model)** – A lightweight yet powerful **AI-based speech recognition model** from OpenAI.  
- **OS & File Handling** – Manages temporary audio files for processing.  

---

## **Machine Learning Model Behind This Project**  
This project utilizes **Whisper**, an advanced **deep learning-based Automatic Speech Recognition (ASR) model** developed by OpenAI.  

🔹 **Model Type:** Transformer-based sequence-to-sequence model  
🔹 **Architecture:** Encoder-Decoder  
🔹 **Training Data:** Multilingual speech datasets with diverse accents and background noise  
🔹 **Functionality:** Converts spoken words into text with high accuracy  

We use the **Whisper tiny model**, which is optimized for **speed and low resource consumption** while maintaining transcription quality.  

## **How It Works**  

1️⃣ **User Uploads an Audio File**  
   - The user selects and uploads an audio file through the web interface.  

2️⃣ **Flask Processes the File**  
   - The backend (Flask) receives the audio file and passes it to the **Whisper AI model** for transcription.  

3️⃣ **Text Output is Generated**  
   - The Whisper model processes the speech and returns the transcribed text, which is then displayed on the web page.  

4️⃣ **Temporary Audio File is Deleted**  
   - To optimize storage, the system automatically removes the uploaded file after processing.  
