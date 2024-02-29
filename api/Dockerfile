FROM python:3.9.9-slim-buster as base

FROM base as builder
# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev      \
  # git+https
  git \
  python3-dev \
  graphviz \
  libgraphviz-dev \
  pkg-config \
  unixodbc-dev

COPY requirements.txt .

RUN pip install --upgrade pip==21.3.1

# Create Python Dependency and Sub-Dependency Wheels.
RUN --mount=type=cache,target=/root/.cache \
  pip wheel --wheel-dir /usr/src/app/wheels  \
  -r requirements.txt

FROM base
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# RUN apk --no-cache add libpq ffmpeg
# RUN addgroup -gid 1000 django && adduser -uid 1000 -G django -s /bin/bash -D django
# Install required system dependencies

RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  libgeos-dev \
  npm \
  netcat \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# COPY --from=builder /install /usr/local

COPY --from=builder /usr/src/app/wheels /wheels/
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
  && rm -rf /wheels/

RUN npm i -g nodemon

# COPY --chown=django:django . .
COPY . .
EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
