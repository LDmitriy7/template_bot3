FROM python:3.10.4

WORKDIR /app

COPY Pipfile.lock Pipfile.lock
RUN pip3 install pipenv && pipenv install

COPY . .

CMD pipenv run python app.py
