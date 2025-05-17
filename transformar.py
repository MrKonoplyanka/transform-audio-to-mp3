from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import os
import uuid
import tempfile
import subprocess

app = FastAPI()

@app.post("/convert")
async def convert_audio(request: Request):
    print("📥 Recibiendo audio binario...")

    file_id = str(uuid.uuid4())
    temp_dir = tempfile.gettempdir()

    input_path = os.path.join(temp_dir, f"{file_id}.oga")
    output_path = os.path.join(temp_dir, f"{file_id}.mp3")

    with open(input_path, "wb") as f:
        f.write(await request.body())

    subprocess.run(["ffmpeg", "-i", input_path, output_path, "-y"])

    return FileResponse(output_path, media_type="audio/mpeg", filename="converted.mp3")
