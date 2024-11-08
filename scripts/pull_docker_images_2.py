import subprocess
import json
from textwrap import indent

if __name__ == "__main__":
    username = "eran.levinzon@gmail.com"
    password = "Dinofun72phx!!!"
    repo = "testrepo"
    base_url = "https://hub.docker.com/v2"
    login_url = f"{base_url}/users/login"
    repo_url = f"{base_url}/repositories/{username}/{repo}"

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
