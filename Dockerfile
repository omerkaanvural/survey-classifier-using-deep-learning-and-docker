FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN python3 -m nltk.downloader stopwords

COPY ./app /app/app

ENTRYPOINT ["python", "app/main.py"]