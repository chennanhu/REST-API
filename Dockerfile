FROM python:3


COPY requirements.txt .
WORKDIR .
ADD main.py .
ADD script.py .

RUN pip install -r requirements.txt

CMD [ "python", "main.py"]