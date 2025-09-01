import streamlit as st
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
from io import BytesIO

# -----------------------------------------------------------
# 🖼 Image Compression using K-Means Clustering
# -----------------------------------------------------------

st.title("🖼 Image Compression using K-Means Clustering")

# Upload image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)

    # ✅ Resize very large images for faster processing
    max_size = 512
    if max(image.size) > max_size:
        w, h = image.size
        ratio = h / w
        image = image.resize((max_size, int(max_size * ratio)))

    # Convert to numpy array
    img_array = np.array(image)

    # ✅ Handle both grayscale & color images
    if len(img_array.shape) == 2:   # Grayscale
        w, h = img_array.shape
        d = 1
        img_reshaped = img_array.reshape(-1, 1)
    else:  # RGB or RGBA
        w, h, d = img_array.shape
        img_reshaped = img_array.reshape(-1, d)

    # Choose number of clusters
    k = st.slider("Select Number of Colors (K)", min_value=2, max_value=64, value=8)

    # Apply K-Means with spinner
    with st.spinner("Compressing image..."):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
        kmeans.fit(img_reshaped)

    # Reconstruct compressed image
    compressed_img = kmeans.cluster_centers_[kmeans.labels_]
    compressed_img = np.clip(compressed_img.astype("uint8"), 0, 255)
    compressed_img = compressed_img.reshape(w, h, d)

    # Show before vs after (smaller width = 300px)
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original", width=300)
    with col2:
        st.image(compressed_img, caption=f"Compressed ({k} colors)", width=300)

    # Convert back to PIL
    compressed_pil = Image.fromarray(compressed_img)

    # ✅ Download without saving to disk
    buf = BytesIO()
    compressed_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        "📥 Download Compressed Image",
        data=byte_im,
        file_name="compressed_image.png",
        mime="image/png"
    )

    # -----------------------------------------------------------
    # ℹ️ Explanation Section
    # -----------------------------------------------------------
    st.subheader("📘 How it Works?")
    st.markdown("""
    1. Image pixels are treated as data points (R,G,B values).
    2. K-Means clustering groups these pixels into **K clusters** (dominant colors).
    3. Each pixel is replaced by its cluster's representative color.
    4. Result: Image looks similar but with fewer unique colors → **compressed**.
    """)

    st.subheader("✅ Why is this Useful?")
    st.markdown("""
    - **Image Compression** → Reduces file size.  
    - **Machine Learning Preprocessing** → Removes noise, simplifies data.  
    - **Artistic Effects** → Creates posterized / low-color style images.  
    - **Educational Demo** → Visual way to understand clustering algorithms.
    """)
