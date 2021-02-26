FROM python:3

ENV http_proxy=$http_proxy
ENV https_proxy=$https_proxy

COPY pip.conf /root/.config/pip/

RUN pip install pipenv

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r requirements.txt

CMD pipenv install && pipenv run python main.py