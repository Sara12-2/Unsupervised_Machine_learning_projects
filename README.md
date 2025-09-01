# Project 1.🌍 Earthquake Epicenter Detection using DBSCAN  

This Streamlit web app detects earthquake epicenters (clusters) from latitude & longitude data using the **DBSCAN clustering algorithm**.  
It allows you to upload earthquake datasets (CSV), explore clustering results, and visualize epicenters on a scatter plot.  

---

## 🚀 Features  
- 📂 Upload CSV files containing **latitude, longitude, and magnitude**.  
- ⚡ Apply **DBSCAN clustering** to detect earthquake epicenters.  
- 🎛️ Adjustable parameters:  
  - **Epsilon (eps)** – radius of neighborhood.  
  - **Min Samples** – minimum number of points to form a cluster.  
- 📊 View **clustered data & summary**.  
- 🌐 Interactive visualization of earthquake clusters on a 2D scatter plot.  

---

## 📦 Installation  

```bash
git clone https://github.com/your-username/earthquake-dbscan.git
cd earthquake-dbscan
pip install -r requirements.txt
```
### 📂 Example Dataset Format
```bash
latitude	longitude	magnitude
34.05	-118.25	4.2
35.68	139.76	5.1
37.77	-122.42	3.8
```
⚠️ Required columns: latitude, longitude
(Optional: magnitude for extra info)
#### ▶️ Run the App
```bash
streamlit run app.py
```
### ⚙️ Requirements

Python 3.8+

streamlit

pandas

matplotlib

scikit-learn

### 📌 Future Improvements

Add heatmap visualization of earthquake density.

Support for time-series analysis (earthquake progression).

Option to download clustered dataset as CSV.


---

### 📂 Project 2 — Image Compression using K-Means (`README.md`)

# 🖼 Image Compression using K-Means Clustering  

This Streamlit app compresses images using **K-Means clustering** by reducing the number of unique colors.  
It allows you to upload an image, select the number of colors, visualize before vs after compression, and download the compressed image.  

---

## 🚀 Features  
- 📂 Upload images (`.jpg`, `.jpeg`, `.png`).  
- 🎛️ Choose the number of colors (**K clusters**) interactively.  
- ⚡ Compress large images (auto-resized for speed).  
- 🖼️ Side-by-side comparison (Original vs Compressed).  
- 📥 Download compressed image directly.  
- 📘 Learn how K-Means is applied to image compression.  

---

## 📦 Installation  

```bash
git clone https://github.com/your-username/image-compression-kmeans.git
cd image-compression-kmeans
pip install -r requirements.txt
```
### ▶️ Run the App
```bash
streamlit run app.py
```
### ⚙️ Requirements

Python 3.8+

streamlit

numpy

scikit-learn

pillow

### 📌 Future Improvements

Add batch image compression.

Support for different clustering algorithms (e.g., MiniBatchKMeans).

Option to compare file sizes (before vs after).

Allow export in JPEG format with adjustable quality.
