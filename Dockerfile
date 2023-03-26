FROM python:3.9-alpine
COPY app .
COPY app/prodModule.py module.py
RUN pip install requests opyoid
CMD python -u main.py