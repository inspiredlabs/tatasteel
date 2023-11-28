###### usage: python3 ./mauw.py ######

# reprompt.py prompting with small pieces (4096 - 888), resulting in `3208` output tokens.
# add to this: https://github.com/emmethalm/infiniteGPT/issues
# from: https://twitter.com/ehalm_/status/1655535249290571777

# reprompt.py prompting with small pieces (4096 - 888), resulting in `3208` output tokens.
# add to this: https://github.com/emmethalm/infiniteGPT/issues
# from: https://twitter.com/ehalm_/status/1655535249290571777

import openai
from concurrent.futures import ThreadPoolExecutor # Installed by default

with open('openai-key.txt', 'r') as file:
    openai.api_key = file.read().strip()

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_to_file(responses, output_file):
    with open(output_file, 'w') as file:
        for response in responses:
            file.write(response + '\n')

# Change your OpenAI chat model accordingly

def call_openai_api(chunk):
    response = openai.ChatCompletion.create(
        # gpt-3.5-turbo
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "Data Entry Assistant. You think step-by-step to analyze MARKDOWN, HTML or JSON code and output data that is always tersely written. Do not appologise. Do not summarise, only ever write summaries as code comments. Do not describe whatever content appears to be, for example, if it is a blog post or advert promoting a product, simply return and output valid data in the requested syntax with no extra explanation only ever write valid data in the requested syntax as code or comments."},
            {"role": "user", "content": f"{chunk}"},
        ],
        max_tokens=1200,
        n=1,
        stop=None,
        temperature=0,
    )
    return response.choices[0]['message']['content'].strip()

def split_into_chunks(text, tokens=888):
    words = text.split()
    chunks = [' '.join(words[i:i + tokens]) for i in range(0, len(words), tokens)]
    return chunks

def process_chunks(input_file, output_file):
    text = load_text(input_file)
    chunks = split_into_chunks(text, tokens=1000)

    # Processes chunks in parallel
    with ThreadPoolExecutor(max_workers=8) as executor:
        responses = list(executor.map(call_openai_api, chunks))

    save_to_file(responses, output_file)

# Specify your input and output files

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    process_chunks(input_file, output_file)

# Can take up to a few minutes to run depending on the size of your data input
