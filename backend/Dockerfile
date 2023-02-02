FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD [ "-m", "flask", "run", "--host=0.0.0.0", "--port=5000" ]