import streamlit as st

st.title("Video Player")

# Path to your video file
video_file_path = "video.mp4"

# Display the video
st.video(video_file_path)
