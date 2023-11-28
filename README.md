# TataSteel

This Python project enables you to leverage `ChatGPT` to capture your meetings and convert the data into a table for data-entry into `SalesForce`.

At the time of writing (Nov. 28th 2023), a 16k context window is free using: `gpt-3.5-turbo-16k`. You just need to add your own API key to `openai-key.txt` from [OpenAI](https://platform.openai.com/api-keys).

## The Problem

> How do you capture years of complex business rules?

### The Strategy

Think of each of the business rules as a separate task. Record the audio and output that as structured data. The first data-entry task could be your overall agenda&hellip; This could be a quick way to help calibrate your Prompt Engineering in the Python script.

## Task 1

### Record your meeting

Record each of your business rules one-by-one with this pattern:

- write down your agenda, IE: what we want to achieve.
- set the audio to record & capture the whole meeting.
- towards the end, have one person clearly recap the key points. This will help summarise your meeting.
- **Highly Recommended** for best results: selectively cut your audio before uploading. This is a good use of your time if the meeting was interupted, etc. while this step is optional it depends on the quality of your audio.

> Remember: garbage in, garbage out!

## Task 2

### Transcribe using CoLab

Before you begin you will need to login to Google services, then click:

[Transcribe using CoLab](https://colab.research.google.com/drive/1g_iEaWrFTwciQ2Moz65h4DGCKNi-eYXk)

> wait for the tiny clock to disappear(!) when you upload your audio!

- upload the audio to CoLab, use an easy filename: `agenda.mp3`
- tap the `folder` icon on the left panel, called: `Files` to start your download.
- drag your audio file into that white space.
- the indicator in the bottom left looks like a tiny clock. This tells you the file's upload progress. When it's 100% complete, it will disappear(!).
- `agenda.mp3` will now appear on the left panel.
- enter your recording's filename. IE: `agenda.mp3`.
- press play and wait. This will transcribe your audio into searchable text.
- CoLab will beep.
- it will prompt you to save `agenda.txt` to your computer (then it should do it automatically).

## Task 3

### Run the demo

> The script has one dependency

- First run: `pip install openai` or `pip3 install openai` if you're on an M-Series Apple device without an environment such as `Conda`.
- To run the demo with the default `input.txt`, just type: `python3 ./gen.py`.

### How does it work?

This script relys on _Prompt Engineering_ to quantify text and turn it into a facts table. `ChatGPT` has been instructed in `gen.py` how to automatically turn a text doc into a facts table, the demo should give you a clear idea of how key columns are indicated from the `input.txt`.

### Generate a meeting table

- find the `agenda.txt` file.
- rename it: `input.txt`.
- copy that file into the same directory as the Python script.
- run the script in Python: `python3 ./gen.py`.
- Python automatically outputs a markdown document that you can view like HTML.

## Task 4

### Data Entry

- use the table & pick out key ideas to help you amend the detail of your business rules.
- send it to your data-entry team to input into SalesForce.
- consider defining a **validation procedure** for your data-entry task.

* * *

## Running the Prompt Engineering script

Clone the repository:

```sh
git clone https://github.com/inspiredlabs/tatasteel
```

Move into the repository:

`cd tatasteel`

The script has one dependency:

`pip install openai`

Run the demo:

`python3 ./gen.py`.
