# My Speech-To-Text App

This project is an audio processing application that listens to uploaded audio files and reacts when it detects a specific word in the audio. The frontend is built with React and the backend is developed with FastAPI, a Python web framework, along with Google's Speech-to-Text service.

The application listens to audio files and when it detects the word "לחזור", it responds with a signal. This signal is currently implemented as a boolean response from the backend, but can be modified as per your requirements.

## Structure

The application is divided into two main parts:

- `frontend/`: Contains the React application that allows users to upload audio files.
- `backend/`: Houses the FastAPI server, which accepts the audio files, converts them into a suitable format, sends them to the Google Speech-to-Text API, and returns the results.

## Setup

Before starting, make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ittaifl/demo-app.git
    cd my-app
    ```

2. **Set up your Google application credentials:**

    In order to use Google's Speech-to-Text service, you need to set up your Google application credentials. Follow these steps to do so:

    - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
    - Enable the [Speech-to-Text API](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries) for your project.
    - Generate a service account key for your project. This will give you a JSON file. Rename this file to `google-credentials.json`.
    - Place the `google-credentials.json` file in the `backend/` directory.

    The backend service needs this to authenticate with Google's Speech-to-Text service.

3. **Build and start the services:**

    Open a terminal, navigate to the project directory, and run:

    ```bash
    docker-compose up --build
    ```

    This will start the frontend service at `http://localhost:3000` and the backend service at `http://localhost:8000`.

## Usage

To use the application, navigate to `http://localhost:3000` in your web browser. You'll be presented with a simple interface that allows you to upload an audio file. Once you've selected a file, the frontend will send it to the backend for processing. If the word "לחזור" is detected in the audio, the backend will return a positive response.


## Support

If you encounter any problems during the setup or usage of this application, feel free to reach out at ittaifl@gmail.com :)

