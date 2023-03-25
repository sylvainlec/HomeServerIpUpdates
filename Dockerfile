FROM python:3.9-alpine
COPY app .
RUN pip install requests
CMD python -u main.py