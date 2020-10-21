FROM tensorflow/tensorflow:2.3.1

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    && apt-get -y install apt-utils gcc libpq-dev libsndfile-dev

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
