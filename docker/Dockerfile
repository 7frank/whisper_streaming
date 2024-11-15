FROM python:3.9-slim

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


EXPOSE 43007

# First command starting the server
CMD ["python", "whisper_server.py", "--backend", "faster-whisper", "--language", "en", "--min-chunk-size", "1", "--silence-size", "2", "--model", "tiny", "--model_cache_dir", "~/.cache/whisper-streaming"]

# Second command for the client (Note: You might want to create a separate service for this)
# CMD ["python", "web_app.py"]