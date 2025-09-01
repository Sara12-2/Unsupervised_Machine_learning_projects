import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

# --------------------------
# Streamlit UI
# --------------------------
st.title("🌍 Earthquake Epicenter Detection using DBSCAN")
st.write("This app detects earthquake epicenters (clusters) from given latitude & longitude data using DBSCAN.")

# File uploader
uploaded_file = st.file_uploader("Upload Earthquake CSV file", type=["csv"])

if uploaded_file is not None:
    # Load dataset
    data = pd.read_csv(uploaded_file)
    st.subheader("📊 Sample Data")
    st.write(data.head())

    # Expecting columns: latitude, longitude, magnitude
    if {'latitude', 'longitude'}.issubset(data.columns):
        X = data[['latitude', 'longitude']].values
        X = StandardScaler().fit_transform(X)

        # DBSCAN parameters
        eps_val = st.slider("Set Epsilon (eps)", 0.1, 5.0, 0.5, 0.1)
        min_samples_val = st.slider("Set Min Samples", 1, 20, 5)

        # Apply DBSCAN
        db = DBSCAN(eps=eps_val, min_samples=min_samples_val).fit(X)
        labels = db.labels_
        data['Cluster'] = labels

        st.subheader("🌀 Clustered Data")
        st.write(data.head())

        # Plot clusters
        plt.figure(figsize=(8, 6))
        plt.scatter(data['longitude'], data['latitude'], c=labels, cmap="rainbow", s=50)
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Earthquake Epicenter Detection (DBSCAN)")
        st.pyplot(plt)

        # Show cluster summary
        st.subheader("📌 Cluster Summary")
        st.write(data['Cluster'].value_counts())

    else:
        st.error("CSV must contain 'latitude' and 'longitude' columns")
else:
    st.info("Please upload a CSV file with earthquake data (latitude, longitude, magnitude).")