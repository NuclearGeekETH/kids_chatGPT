# NuclearGeek's ChatGPT for Kids

A simple text-based chatbot for kids powered by OpenAI GPT-3.5-turbo. It has a nice UI and support for text-to-speech.

## Prerequisites

You'll need Python 3.6 or newer installed on your computer.

## Setting up the project

1. Create a folder on your computer for this project, like "chatgpt-kids".
2. Download the Python files and `index.html` we created earlier into your project folder ("chatgpt-kids").
3. Inside the project folder, create an empty folder named "templates". Move the `index.html` file into the "templates" folder.

## Setting up the environment

1. Open your computer's terminal (Command Prompt on Windows, Terminal on macOS) and navigate to the project folder ("chatgpt-kids").
2. Create a virtual environment. This helps keep your project's dependencies separate. Run this command in the terminal:
   ```
   python -m venv myvenv
   ```
3. Activate the virtual environment by running:
   - On Windows:
     ```
     myvenv\Scripts\activate
     ```
   - On macOS or Linux:
     ```
     source myvenv/bin/activate
     ```
   Your terminal should show "(myvenv)" before the line where you type commands, indicating the virtual environment is active.

4. Install the required dependencies by running:
   ```
   pip install flask python-dotenv openai
   ```

## Setting up the OpenAI API key

1. Sign up for an account on [OpenAI](https://beta.openai.com/signup/), if you haven't already.
2. Locate your API key by going to the [API Key section](https://beta.openai.com/account/api-keys) on the OpenAI website.
3. In the project folder, create a file named `.env` (with a dot at the beginning) and add the following line to the file:
   ```
   openai_key=YOUR_API_KEY
   ```
   Replace `YOUR_API_KEY` with the API key you found on the OpenAI website.

## Running the project

1. Make sure your virtual environment is active. If it isn't, activate it by running the command from Step 3 of "Setting up the environment".
2. In the terminal, navigate to the project folder ("chatgpt-kids") and type the following command to start the Flask server:
   ```
   python app.py
   ```
   Replace `app.py` with the name of your Python file, if it's different.
3. After running the command, you should see some output in the terminal, including a line that says something like:
   ```
   * Running on http://127.0.0.1:7863/ (Press CTRL+C to quit)
   ```
4. Open your web browser and type the address shown in the terminal (e.g., `http://127.0.0.1:7863/`). The ChatGPT for Kids page should appear.
5. Enjoy using the chatbot! The text-to-speech feature should work on most devices.

**Note:** To stop the server, press `CTRL+C` or `Cmd+C` in the terminal.