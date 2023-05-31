# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN npm install
RUN npm run build
RUN npm install -g serve

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Run the command to start the React app
CMD serve -s build -l 3000