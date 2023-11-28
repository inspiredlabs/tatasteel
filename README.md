# TataSteel

This Python project enables you to leverage `ChatGPT-3.5` to capture your meetings and convert the data into a table for data-entry into `SalesForce`.

## The Problem

> How do you capture years of complex business rules?

## The Strategy

Think of each of the business rules as a separate task. Record the audio and output that as structured data. The first data-entry task could be your overall agenda&hellip; This could be a quick way to help calibrate your Prompt Engineering in the Python script.

## Task 1

### Record your meeting

Record each of your business rules one-by-one with this pattern:

- write down your agenda, IE: what we want to achieve.
- set the audio to record & capture the whole meeting.
- towards the end, have one person clearly recap the key points. This will help summarise your meeting (optional: selectively cut your audio before uploading it to the AI. This is a good use of your time if the meeting was interupted, etc.).

## Task 2

### Transcribe using CoLab

- upload the audio to CoLab, use an easy to track filename: `agenda.mp3`
- the indicator in the bottom left looks like a tiny clock and tells you the file's upload progress. When it's 100% complete, it will disappear.
- enter your recording's filename. IE: `agenda.mp3`.
- press play and wait. This will transcribe your audio into searchable text.
- it will beep. Then it will prompt you to save `agenda.txt` to your computer.

## Task 3

### Prompt Engineering

- find the `agenda.txt` file.
- rename it: `source.txt`.
- copy that file into the same directory as the Python script.
- By using Prompt Engineering, Python will automatically organise your meeting into a table, creating key columns that form a table of your data.

## Task 4

### Data Entry

- use the table & pick out key ideas to help you amend the detail of your business rules.
- send it to your data-entry team to input into SalesForce*.
- now is a good time to consider a validation procedure for your data-entry task.

* * *

## Running the Prompt Engineering script in Python

Clone the repository:

```sh
git clone https://github.com/inspiredlabs/tatasteel
```
