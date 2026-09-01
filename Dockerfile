# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install pip requirements first — this layer only rebuilds when
# requirements.txt itself changes, not every time your code changes,
# so rebuilds after a normal code edit are much faster.
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the project
COPY . .

# Collect every app's static/ folder (dashbord/static/..., etc.) into
# STATIC_ROOT so whitenoise (added in settings.py) can serve them.
# gunicorn does NOT serve static files on its own — only `runserver`
# does, and only when DEBUG=True.
RUN python manage.py collectstatic --noinput

# entrypoint.sh may have been saved with Windows line endings (CRLF).
# Linux's shell chokes on that ("bad interpreter" / "exec format error"),
# so strip any trailing \r before it's ever executed.
RUN sed -i 's/\r$//' entrypoint.sh && chmod +x entrypoint.sh

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

EXPOSE 8000

# entrypoint.sh runs migrations, then starts gunicorn — see that file
# for why this isn't just a CMD.
ENTRYPOINT ["./entrypoint.sh"]
