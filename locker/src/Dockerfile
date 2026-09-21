FROM python:3.9-slim-bookworm
RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN useradd -m ctf
COPY questions_without_timeout.py .
USER ctf
EXPOSE 27312
CMD ["socat", "TCP-LISTEN:27312,fork,reuseaddr", "EXEC:python3 -u questions_without_timeout.py,stderr"]