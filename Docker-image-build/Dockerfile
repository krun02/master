#baseimage selection
FROM python:3.12-slim

#2 Set the working directory
WORKDIR /app 

#3 Install dependencies
RUN pip install flask==2.3.3

#4 Copy application files to the container
COPY . /app

#5 Specify the environment variable or link to python code 
ENV FLASK_APP=app.py

#6 Define the default command to execute the code
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]





