FROM python:3.9-alpine
COPY app .
COPY app/modules/prodModule.py modules/module.py
RUN pip install -r requirements.txt
CMD python -u main.py