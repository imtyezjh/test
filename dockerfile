FROM python:2.7
ADD hello.py / 
RUN pip install flask 
EXPOSE 5000
CMD ["python","./hello.py"]
