FROM python:slim

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "send_message.py"]