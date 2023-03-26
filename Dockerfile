FROM python:3.9-alpine
COPY app .
COPY app/modules/prodModule.py modules/module.py
RUN pip install requests opyoid
CMD python -u main.py