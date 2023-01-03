FROM python:3.10.9-slim

LABEL org.opencontainers.image.source="https://github.com/ZiRO-Bot/RandomAPI"
LABEL org.opencontainers.image.description="API with random content inside"
LABEL org.opencontainers.image.licenses=Unlicense

WORKDIR /app

COPY . .
RUN python -m pip install -r ./requirements.txt

EXPOSE 2264
CMD ["uvicorn", "app:app", "--host 0.0.0.0", "--port 2264"]
