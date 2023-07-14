# Testing Containers

testing making python containers using docker

This is simply to test if I can make a python container using docker

This branch uses a setup.py file when compiling

Differences between Requirements.txt and Setup.py:
  - Requirements: List of the pre-requisets needed in order to run the .py file. Lists the necessary packages and their versions, essentially **tells you what program needs to run**
  - Setup: Metadata specifications for the program. Defines how the program is going to be packaged and distributed. Intended for sharing files, as well as telling computer what packages are needed to install

To run:
1. Create an image by typing 'docker build -t nameOfMyImage .'
2. Type 'docker run nameOfMyImage' should print out Hello World! in console
