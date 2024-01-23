FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /telegram-bot
COPY . /telegram-bot
RUN pip install -r requirements.txt
CMD ["python", "main.py"]