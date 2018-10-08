FROM python:3.7
ENV _PIP_VERSION 18.0
ENV _PIPENV_VERSION 2018.7.1

WORKDIR /app

RUN pip install pip==${_PIP_VERSION} pipenv==${_PIPENV_VERSION}
RUN pipenv run pip install pip==${_PIP_VERSION}

EXPOSE 8888
VOLUME /app/src

RUN adduser --disabled-password --gecos "" notebook
USER notebook

ADD Pipfile* /app/
RUN pipenv install

ADD jupyter_notebook_config.py /app/
CMD ["pipenv", "run", "jupyter", "notebook", "src/CandidateConsiderations.ipynb"]

