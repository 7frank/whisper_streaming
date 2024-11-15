FROM python:3.12-slim

WORKDIR /app

# Copy poetry related files
COPY pyproject.toml poetry.lock ./

# Install poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copy application files
COPY . .

# Set environment variables
ENV WHISPER_DEVICE_TYPE=cpu
ENV WHISPER_MODEL_SIZE=tiny

EXPOSE 43007


RUN mkdir -p app/.cache/whisper-streaming
# First command starting the server

CMD ["python", "whisper_server.py", "--backend", "faster-whisper", "--language", "en", "--min-chunk-size", "1", "--silence-size", "2", "--model_cache_dir", "app/.cache/whisper-streaming"]
# Second command for the client (Note: You might want to create a separate service for this)
# CMD ["python", "web_app.py"]