# Automated Image Processing Pipeline with Cloud Functions and Cloud Storage
*A cloud engineering project by kaiser-lord*

---

## 📘 Overview
This project builds an event-driven, serverless pipeline on Google Cloud Platform (GCP) that automatically processes images uploaded to a Cloud Storage bucket

---

## 🎯 Objectives

- Develop a serverless image processing pipeline, to automatically process images uploaded to a bucket  
- Implement serverless architecture, and automation
- Make extensive use of Google Cloud services

---

## ☁️ Architecture
 The application uses a serverless architecture with Cloud Functions, and Cloud Storage buckets to store uploaded and processed images respectively

![Architecture Diagram](todo-app-architecture.png)

- **User**: Uploads images to the input bucket via browser or CLI.
- **Input Bucket**: Stores uploaded images, triggering the Cloud Function via Eventarc.
- **Cloud Function**: Resizes images to 200x200 pixels using Pillow.
- **Output Bucket**: Stores processed thumbnails.


**Components:**
| Layer | Services / Tools | Description |
|-------|------------------|-------------|
| Layer                      | Services / Tools                                      | Description                                      
| **Compute**                | **Cloud Functions (2nd Gen)**                         | Serverless environment running the image-processor function to resize images |
| **Storage**               | **Cloud Storage**                                      | Input bucket (input-images) for uploads and output bucket (image-output) for thumbnails |
| **Application Code**       | **Python**, **Pillow Library**                        | Backend logic for image resizing and interaction with Cloud Storage |






## 📫 Contact
**Juan Bautista Sartorio**  
LinkedIn: [linkedin.com/in/juan-bautista-sartorio-isasi](https://www.linkedin.com/in/juan-bautista-sartorio-isasi/)  
GitHub: [github.com/kaiser-lord](https://github.com/kaiser-lord)
