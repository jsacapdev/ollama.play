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


def main():
    if os.path.exists('instructions.json'):
        print("Instructions found - deleting...\n")
        os.remove('instructions.json')

    if not os.path.exists('instructions.json'):
        topic = input("What is the topic of this training dataset? ")
        prompt = f"""Please list in JSON format 10 frequently asked questions about {topic} from all levels of users  
        f"working on it.  The questions should start with any of the following: 'Where do I' 
        f"'Is it okay to',  'Can you help me', 'I need to', 'Is there a', 'Do you know', 'Where is the', 
        f"'Can you tell me', 'Can I change', 'What are the', 'How do I', 'When is it', 'Does WordPress have'
        f"'How to', 'What is the difference', 'Can users', 'Can I', 'What is' 
        f"You do not need to provide an answer, or category to each question. The list should be 
        f"a single dimension array of only questions."""
        tic = time.perf_counter()
        instructions = query_ollama(prompt)
        toc = time.perf_counter()
        with open('instructions.json', 'w') as file:
            file.write(instructions)

    with open('instructions.json', 'r') as file:
        instructions = json.load(file)

    print(f"Done! Instructions file generated in {toc - tic:0.4f} seconds.")


if __name__ == "__main__":
    main()
