# ai-chatbot

This is a chatbot you are able to train on any custom knowledge base using OpenAI's ChatGPT API.

**Pre-requisites:**
1. Code editor of your choice
2. python 3.11 and pip
3. to check if it is properly installed run `python --version` and `pip --version`
4. run `python -m pip install -U pip` to update pip to the latest version

**Set-up guide:**
1. run these following commands in the terminal:
    - `pip install openai`
    - `pip install gpt_index==0.4.24`
    - `pip install langchain==0.0.148`
    - `pip install PyPDF2`
    - `pip install Pycryptodome`
    - `pip install Flask`
2. Get your own OpenAI API Key and replace in `app.py` (DO NOT SHARE)
3. create a new folder called `docs` and place pdf files of what you want to train
4. Make sure all files are in the same location
5. Save all files and run `cd "YOUR_FILE_LOCATION"` to move into the correct location
6. run `python app.py` and open on your local URL `can be found in the terminal`

**Demo: Bot was trained on Beej's Guide to C Programming textbook** <br>
(![image](https://github.com/altonph/ai-chatbot/assets/89827405/f58a46b3-e4ae-4675-ac09-e8ec41bf08e6)

