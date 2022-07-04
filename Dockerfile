FROM python:3.9
RUN pip install flask
COPY . /opt/
RUN ls /opt/
COPY flask_app/app.py /opt/
WORKDIR /opt
RUN python setup.py install
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
