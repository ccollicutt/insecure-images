FROM python:2.7.18
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY app.py /
RUN useradd python -u 10001 --user-group
USER 10001
ENV FLASK_APP=app.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]