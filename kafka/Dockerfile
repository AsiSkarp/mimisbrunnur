FROM python:3.8-slim


RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*


ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /app/wait-for-it.sh

RUN chmod +x /app/wait-for-it.sh

WORKDIR /app    

COPY requirements.txt /app/

RUN  pip install -r requirements.txt

COPY producer.py /app/

CMD ["./wait-for-it.sh", "kafka:9092", "--", "python", "producer.py"]