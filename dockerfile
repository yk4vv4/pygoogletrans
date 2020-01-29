FROM python:alpine
LABEL maintainer="Yuki Kawashima <kawashin@gmail.com>"
RUN pip install googletrans tqdm
COPY app /app
CMD ["/usr/local/bin/python", "/app/main.py"]
