FROM python:3.7.5-alpine3.9

ENV http_proxy 'http://websurfing1-htl1.esi.adp.com:8080/'
ENV https_proxy 'http://websurfing1-htl1.esi.adp.com:8080/'
ENV no_proxy 'http://websurfing1-htl1.esi.adp.com:8080/'

COPY . /app

# Update & Install dependencies
RUN apk update \
        && apk add --no-cache git openssh-client \
        && pip install pipenv

RUN cd app && pipenv install && pipenv run python main.py && cd .. 

# Clean
RUN rm -rf ~/.cache/pip