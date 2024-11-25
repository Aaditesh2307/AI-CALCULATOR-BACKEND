from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

# Create the FastAPI router
router = APIRouter()



@router.post('')  # Add a valid route path
async def run(data: ImageData):
    try:
        # Decode the base64 image
        image_data = base64.b64decode(data.image.split(",")[1])  # Assumes data:image/png;base64,<data>
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)

        # Call analyze_image function
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)

        # Prepare the response
        data = []
        for response in responses:
            data.append(response)

        print('Responses in route:', responses)  # Log all responses for debugging
        return {"message": "Image processed", "data": data, "status": "success"}

    except Exception as e:
        # Log the error and return a response
        print("Error in /calculate route:", e)
        return {"message": "Error processing image", "error": str(e), "status": "failure"}
