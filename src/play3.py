import json
import os
import ollama
import time


def query_ollama(prompt, model='mistral', context=''):
    context_prompt = context + prompt
    response = ollama.generate(
        model=model,
        prompt=context_prompt)
    return response['response'].strip()


def create_valid_file():
    if not os.path.exists('train.jsonl'):
        die('No train.jsonl file found!')

    with open('train.jsonl', 'r') as file:
        train_lines = file.read().splitlines()

    total_lines = len(train_lines)
    twenty_percent = round(total_lines * 0.2)

    val_lines = train_lines[:twenty_percent]
    train_lines = train_lines[twenty_percent:]

    with open('train.jsonl', 'w') as file:
        file.write('\n'.join(train_lines))

    with open('valid.jsonl', 'w') as file:
        file.write('\n'.join(val_lines))


def die(message):
    raise Exception(message)


def main():
    if not os.path.exists('instructions.json'):
        die('No instructions file found!')

    with open('instructions.json', 'r') as file:
        instructions = json.load(file)

    total = len(instructions)

    start = time.perf_counter()

    print("------------------------------")
    for i, instruction in enumerate(instructions):
        print(f"({i + 1}/{total}) {instruction}")
        print("------------------------------")

        instruction_text = instruction[0]
        tic = time.perf_counter()
        answer = query_ollama(instruction_text)
        toc = time.perf_counter()
        print(answer)  # for terminal output
        print(f"Answer generated in {toc - tic:0.4f} seconds.")

        result = {'text': f'<s>[INST] {instruction}[/INST] {answer}</s>'}
        output = json.dumps(result) + "\n"
        output = output.replace('[\/INST]', "[/INST]").replace('<\/s>', "</s>")

        print("\n\n------------------------------\n")

        with open('train.jsonl', 'a') as file:
            file.write(output)

    create_valid_file()

    end = time.perf_counter()

    print(F"Done! Training and validation JSONL files created {end - start:0.4f} seconds..")


if __name__ == "__main__":
    main()
