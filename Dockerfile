FROM python:3.10

WORKDIR /code/app

COPY ./requirements.txt /code/app/requirements.txt

RUN pip install --no-cache-dir -r /code/app/requirements.txt

COPY . /code/app

USER 65534:65534
EXPOSE 8000/tcp

CMD ["uvicorn", "2_advanced:app", "--host", "0.0.0.0", "--port", "8000"]
