# Template for telegram bots

## Environment variables

- `BOT_TOKEN` [Required] - Telegram bot token
- `DB_HOST` [Required] - Mongo database host
- `DB_NAME` [Required] - Mongo database name

## Run

### Requirements:

- `python3.10`
- `pipenv`
- `mongo`

### Prepare:

1) Create environment file `.env`
2) Command `pipenv install`
3) Command `pipenv shell`

### Start:

Command `python app.py`

## Deploy

### Requirements:

- `docker`
- `docker-compose-plugin`
- `bash`

### Prepare:

1) Create environment file `.env`
2) Open `bash`

### Start:

Command `. scripts/deploy.sh`

### Stop:

Command `. scripts/stop.sh`

### Logs:

Command `. scripts/logs.sh`
