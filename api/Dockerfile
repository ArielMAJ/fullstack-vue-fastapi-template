FROM python:3.9

ADD . .

RUN pip install -r requirements.txt


EXPOSE 3000

ENTRYPOINT ["python", "-m", "src.main"]
