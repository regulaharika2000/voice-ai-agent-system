FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["python", "run.py"]