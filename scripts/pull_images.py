import subprocess

# Define an array of image names
image_names = [
    "debian:latest", 
    "eclipse-temurin:Latest",
    "minimal-ubuntu20.04-py38-cpu-inference:latest",
    "minimal-ubuntu20.04-py38-cuda11.6.2-gpu-inference:latest",
    "minimal-ubuntu22.04-py39-cpu-inference:latest",
    "minimal-ubuntu22.04-py39-cuda11.6.2-gpu-inference:latest", 
    "python:3.9", 
    # Add more image names as needed
]


# Loop through the array and pull each image
for image in image_names:
    subprocess.run(["docker", "pull", image])
