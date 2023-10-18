FROM python:3.10

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install python-multipart
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY src /app

EXPOSE 5000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]