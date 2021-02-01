FROM python:3.8

RUN apt-get update
RUN apt-get install -y swi-prolog

RUN pip install problog pyswip

RUN mkdir progetto_AI

COPY sette_e_mezzo_DTProblog/ ./progetto_AI/

WORKDIR progetto_AI/

CMD [ "python", "main.py" ]



