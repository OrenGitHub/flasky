FROM python:3.12
RUN pip install flask
COPY main.py main.py
ENV FLASK_APP=main.py
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
