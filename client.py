import requests

image_path = r"C:\Users\Ben\Pictures\Ultraman\train\image\images (7).jpg"
url = "http://localhost:8000/upload"

with open(image_path, "rb") as img_file:
    files = {"image": img_file}
    response = requests.post(url, files=files)
    response_JsonObj=response.json()

print("Server response:",response_JsonObj.get("message", "No message received") )
