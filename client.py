import os
import cv2
import requests

image_path = r"C:\Users\mm15697\Pictures\T24AfterRetrain.png"
url = "http://localhost:8000/upload"


# For reading an image from disk and send out directly
# with open(image_path, "rb") as img_file:
    # files = {"image": img_file}
    # response = requests.post(url, files=files)
    # response_JsonObj=response.json()

# For reading an image and do some Opencv preprocessing
img_file=cv2.imread(image_path)
# Can do some preprocessing here-----------------



# -----------------------------------------------
# Encode image as JPEG
_, img_encoded = cv2.imencode('.jpg', img_file)
# Get image name
image_name=os.path.basename(image_path)
# Prepare image name, image bytes to be sent
files = {"image": (f"{image_name}", img_encoded.tobytes(), 'image/jpeg')}

# Send out the image and get the server response
response = requests.post(url, files=files)
response_JsonObj=response.json()
print("Server response:",response_JsonObj.get("message", "No message received") )
