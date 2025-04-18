FROM python:3.12

WORKDIR /usr/src/app

ARG REQ_TXT
COPY ${REQ_TXT} ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r ${REQ_TXT}
