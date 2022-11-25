FROM python:3.10.7
WORKDIR /app
COPY . /app
COPY templates /app/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["app.py" ]