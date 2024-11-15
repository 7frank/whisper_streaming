FROM nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04

# Prevent prompts during the build process
ENV DEBIAN_FRONTEND=noninteractive

# Update package list, install prerequisites, and install Python 3.10
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Verify Python installation
RUN python3.12 --version


WORKDIR /app

# Copy poetry related files
COPY pyproject.toml poetry.lock ./


# Install poetry
RUN pip install poetry && \
    poetry config virtualenvs.create true && \
    poetry install --no-dev

# Copy application files
COPY . .

# Set environment variables
ENV WHISPER_DEVICE_TYPE=cpu
ENV WHISPER_MODEL_SIZE=tiny

EXPOSE 43007


RUN mkdir -p app/.cache/whisper-streaming
# First command starting the server

CMD ["poetry", "run",  "python3.12", "whisper_server.py", "--backend", "faster-whisper", "--language", "en", "--min-chunk-size", "1", "--silence-size", "2", "--model_cache_dir", "app/.cache/whisper-streaming"]

# CMD ["tail", "-f", "/dev/null"] 