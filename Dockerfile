FROM python:3.10-alpine as builder

WORKDIR /build
RUN apk add zlib-dev jpeg-dev gcc musl-dev freetype-dev

COPY requirements.txt .
RUN python -m venv /build/venv
RUN /build/venv/bin/pip install --no-cache-dir -r requirements.txt
RUN find venv -type d -a -name test -exec rm -rf '{}' +
RUN find venv -type d -a -name tests  -exec rm -rf '{}' +
RUN find venv -type f -a -name '*.pyc' -exec rm -rf '{}' +
RUN find venv -type f -a -name '*.pyo' -exec rm -rf '{}' +

FROM python:3.10-alpine
WORKDIR /app
RUN apk add jpeg-dev freetype-dev
COPY --from=builder /build /app
COPY . .

ENV PATH="/app/venv/bin:$PATH"