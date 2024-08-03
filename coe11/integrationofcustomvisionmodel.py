import requests
import json

endpoint = "<Your Custom Vision Endpoint>"
prediction_key = "<Your Prediction Key>"
project_id = "<Your Project ID>"
publish_iteration_name = "<Your Iteration Name>"
image_path = "path/to/your/image.jpg"

with open(image_path, "rb") as image:
    data = image.read()

headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/octet-stream"
}

response = requests.post(f"{endpoint}/customvision/v3.0/Prediction/{project_id}/classify/iterations/{publish_iteration_name}/image",
                         headers=headers, data=data)

predictions = response.json()
print(json.dumps(predictions, indent=2))
