from flask import Flask, render_template, request
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = Flask(__name__)

CONTEXT = ''
PREVIOUS_ANSWER = ''

@app.before_request
def clear_context_and_answer():
    global CONTEXT
    global PREVIOUS_ANSWER
    if request.endpoint == 'index':
        CONTEXT = ''
        PREVIOUS_ANSWER = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submitContext', methods=['POST'])
def submit():
    global CONTEXT
    user_input = request.form['user_input']
    CONTEXT = user_input
    return user_input

@app.route('/getAnswer', methods=['POST'])
def getModelAnswer():
    global CONTEXT
    global PREVIOUS_ANSWER
    model_path = './trained_model'
    tokenizer = T5Tokenizer.from_pretrained(model_path)
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    user_input = request.form['user_input']
    input_text_1 = (f"Context: {CONTEXT} Question: {PREVIOUS_ANSWER} {user_input}")
    input_ids_1 = tokenizer(input_text_1, return_tensors="pt", padding=True, truncation=True).input_ids
    output_ids_1 = model.generate(input_ids_1)
    response_1 = tokenizer.decode(output_ids_1[0], skip_special_tokens=True)

    PREVIOUS_ANSWER += response_1

    return f'AI Says: {response_1}'




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)