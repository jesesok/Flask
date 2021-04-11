FROM python:3.9
COPY . /application
RUN pip install -r /application/requirements.txt
ENTRYPOINT ["python"]
CMD ["/app.py"]
