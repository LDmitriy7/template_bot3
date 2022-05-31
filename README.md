# Template for telegram bots

---

## Environment variables

- `BOT_TOKEN` [Required] - Telegram bot token
- `DB_HOST` [Required] - Mongo database host
- `DB_NAME` [Required] - Mongo database name

---

## Running

### Requirements:

- `python3.10`
- `pipenv`
- `mongo`

### Preparing:

1) Create environment file `.env`
2) Command `pipenv install`
3) Command `pipenv shell`

Command `python app.py`

---

## Deploying

### Requirements:

- `docker`
- `docker-compose-plugin`

### Preparing:

1) Create environment file `.env`

Command `. deploy.sh`

---