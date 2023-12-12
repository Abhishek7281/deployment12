FROM python:3.11

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install  -r requirements.txt

EXPOSE 8502

COPY . /app

ENTRYPOINT ["streamlit","run"]

# CMD ["app.py"]

CMD ["app/app", "--host", "0.0.0.0", "--port", "$PORT"]
