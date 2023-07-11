# Dockerfile, Image, Container

FROM python:3.9

# Set the working directory 
WORKDIR /app

# Copy the requirements txt file to the container
# Contains all of the imports needed to make the code work
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application's code to the container
COPY . .

# Specify command to run the program
CMD [ "python", "./HelloWorld.py" ]