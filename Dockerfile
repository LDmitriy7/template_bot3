FROM python:3.10.4

COPY Pipfile.lock Pipfile.lock
RUN pip3 install pipenv && pipenv install

COPY . .

CMD pipenv run python app.py
