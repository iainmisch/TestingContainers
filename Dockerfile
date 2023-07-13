# Dockerfile, Image, Container

FROM python:3.9

# Set the working directory 
WORKDIR /app

# Copy the application's code to the container
COPY . /app

# Install dependencies through setup.py
RUN pip install .

# Specify command to run the program
CMD [ "python", "HelloWorld.py" ]