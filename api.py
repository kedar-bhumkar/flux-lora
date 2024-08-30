import json
from urllib import request, parse
import random
import os
from monitor import monitor_directory
import argparse
from workflow_api import workflow
from util import getCharacter, getPrompts
from constants import default_batch_size, default_subject, default_prompts_file, default_folder_to_watch

def queue_prompt(prompt):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)

def initialize_prompt(text, subject):
    prompt = json.loads(workflow)
    prompt["5"]["inputs"]["batch_size"] = default_batch_size
    prompt["6"]["inputs"]["text"] = text
    prompt["29"]["inputs"]["lora_name"] = subject + "_replicate.safetensors"
    return prompt

def replace_text(text, subject, config):
    text = text.replace("{subject}", subject)
    text = text.replace("{clothes}", subject + "  " + config["clothing"])   
    text = text.replace("{age}", subject + " is " + str(config["age"]))
    text = text.replace("{gender}", config["gender"])
    text = text.replace("{ethnicity}", config["ethnicity"])
    return text

def main():
    folder_to_watch = default_folder_to_watch
    parser = argparse.ArgumentParser(description="Run flux on any character.")
    parser.add_argument("--ch", type=str, required=True, help="the base character")
   
    args = parser.parse_args()
    subject = args.ch if args.ch else default_subject    
    config = getCharacter(subject)

    prompts = getPrompts(default_prompts_file)
    total_prompts = len([p for p in prompts if p.strip()])

    for counter, text in enumerate(prompts):            
            text = text.strip()
            if text:  # Ensure the prompt is not empty         
                text = replace_text(text, subject, config)
                prompt = initialize_prompt(text, subject)                
                print(f"Processing prompt {counter+1} of {total_prompts} : {text}")
                text = ""
                queue_prompt(prompt)                           
                #wait till process is complete. Since the request is non-blocking we need to monitor the folder or wait until the timeout.                
                monitor_directory(folder_to_watch)
            else:
                print("Skipping empty prompt")
    print("All prompts processed.")
    return


if __name__ == "__main__":
    main()


