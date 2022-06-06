# Template for telegram bots

## Run

### Requirements:

- `python3.10`
- `pipenv`
- `mongo`

### Prepare:

1) Create file `.env` using `sample.env`
2) Command `pipenv install`

### Start:

Command `pipenv run python app.py`

## Deploy

### Requirements:

- `docker`
- `docker-compose-plugin`
- `bash`

### Prepare:

1) Create file `.env` using `sample.env`
2) Open `bash`

### Start:

Command `. scripts/deploy.sh`

### Stop:

Command `. scripts/stop.sh`

### Logs:

Command `. scripts/logs.sh`

### Get into containers:

- Command `. scripts/app.sh`
- Command `. scripts/mongo.sh`

### Get dump (./dump):

Command `. scripts/mongodump.sh`
