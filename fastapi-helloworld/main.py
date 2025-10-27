import os
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Read environment variables
IMAGE_PATH = os.getenv("IMAGE_PATH", "rh-developer.jpg")
DISPLAY_TEXT = os.getenv("DISPLAY_TEXT", "Hello from FastAPI!")

# Mount static directory to serve image files
# Assuming the image file is in the same directory or any static folder
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    # Extract just the filename (for static serving)
    image_filename = os.path.basename(IMAGE_PATH)

    html_content = f"""
    <html>
        <head>
            <title>FastAPI Image Display</title>
            <style>
                body {{
                    text-align: center;
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin-top: 50px;
                }}
                img {{
                    max-width: 400px;
                    border-radius: 12px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                }}
                h1 {{
                    margin-top: 20px;
                    color: #333;
                }}
            </style>
        </head>
        <body>
            <img src="/static/{image_filename}" alt="Image" />
            <h1>{DISPLAY_TEXT}</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
