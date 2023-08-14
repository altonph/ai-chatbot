from flask import Flask, render_template, request
from gpt_index import SimpleDirectoryReader, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain.chat_models import ChatOpenAI
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = ''

app = Flask(__name__)

# Define a function to construct the index from documents in a directory
def construct_index(directory_path):
        
    # parameters for indexing
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    # the prompt helper helps deal with LLM context window token limitations
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit= chunk_size_limit)
    
    # handles conversion of prompts to string inputs
    llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature = 0.7, model_name = "gpt-3.5-turbo", max_tokens = num_outputs))

    #read directory and load into documents variable
    documents = SimpleDirectoryReader(directory_path).load_data()

    # saving our index in a variable
    index = GPTSimpleVectorIndex(documents, llm_predictor = llm_predictor, prompt_helper = prompt_helper)

    # saving index to disk
    index.save_to_disk('index.json')

    return index

# Define a function for the chatbot's behavior
def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode = "compact")
    return response.response

@app.route('/', methods=['GET', 'POST'])
def index():
    messages = []
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = chatbot(user_input)
        messages.append({'user_input': user_input, 'bot_response': response})
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    index = construct_index("docs")
    app.run(debug=True)