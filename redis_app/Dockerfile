# Use the official Python 3.8 slim image as the base image which is smaller and quicker download time 
FROM python:3.8-slim as Build
# Set the working directory in the container to /app and any subsequent commands will be run from this directory
WORKDIR /app
# copy all files from the current directory to the /app directory inside the container
COPY . .
# install the required dependencies for the application
RUN pip install flask redis
#what port the application will listen on
EXPOSE 5002
# this launches the flask application
CMD ["python", "count.py"] 