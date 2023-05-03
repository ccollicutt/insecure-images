FROM python:2.7
COPY app.py /
RUN useradd python -u 10001 --user-group
USER 10001
CMD ["python","-u","/app.py"]