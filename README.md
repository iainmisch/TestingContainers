# Printing EST Time

This code is a modification of the printing-OS code. In this branch, the program uses the 'datetime'
package to get the time of the operating system in UTC. 

Next, using a simple conversion, the program converts the UTC time into EST time, where this computer is based out of

Problems during development:
1. Location, location, location: where the dockerfile is stored is very important, as well as the syntax of naming it. Ensure that the terminal line is at the same level of where 'Dockerfile' is stored. This caused a lot of time to be enveloped in testing different file locations and research
2. Conversion from UTC to EST is simple, as there is a set time difference between the two. However, I wanted to avoid using magic numbers to subtract an arbitrary amount of time out of the UTC time. As a result, a bit of time was invested into finding different ways to calculate the offset

Running the dockerfile:
1. Ensure that the Dockerfile is not buried deep, and that the command line is at the same level of the Dockerfile
2. Type: 'docker build -t name-of-image .' (. implies creating the image at the same level as the command line)
3. Once built, type: 'docker run name-of-image'
4. Profit
