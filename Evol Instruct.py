#!/usr/bin/env python
# coding: utf-8

import json
import random

# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
# Define the OpenAI API key
client = OpenAI(api_key='your api key')

# Define the evolution strategies
class EvolutionStrategy:
    def __init__(self):
        pass  # No initialization for llm_pipeline needed (needed if you use hugging face)
    
    def evolving(self, instruction):
        # Define multiple prompts for in-depth evolving
        add_constriants_prompt = (
            "I want you to act as a Prompt Rewriter.\n"
            "Your objective is to rewrite the following instruction into a more complex version to make it a bit harder for AI systems like ChatGPT and GPT4 to handle. "
            "The rewritten instruction must be reasonable, understandable, and answerable by humans. "
            "You should add one more constraint or requirement into the instruction, without making it verbose. "
            "The rewritten instruction can only add 10 to 20 words.\n\n"
            "#Given Prompt#:\n" +
            instruction +
            "\n#Rewritten Prompt#:"
        )
        deepening_prompt = (
            "I want you to act as a Prompt Rewriter.\n"
            "Your objective is to rewrite the given prompt into a more complex version to challenge advanced AI systems like ChatGPT and GPT4. "
            "The revision must remain reasonable and understandable for humans.\n"
            "You should increase the depth and breadth of the inquiry in the given prompt.\n"
            "Do not exceed an addition of 10 to 20 words.\n\n"
            "#Given Prompt#:\n" +
            instruction +
            "\n#Rewritten Prompt#:"
        )

        concretizing_prompt = (
            "I want you to act as a Prompt Rewriter.\n"
            "Your task is to concretize the given prompt, replacing general concepts with more specific ones to enhance its complexity. "
            "The new version should be a bit more challenging for AI, yet still understandable by humans.\n"
            "Avoid verbosity and limit your addition to 10 to 20 words.\n\n"
            "#Given Prompt#:\n" +
            instruction +
            "\n#Rewritten Prompt#:"
        )

        increased_reasoning_steps_prompt = (
            "I want you to act as a Prompt Rewriter.\n"
            "Please rewrite the given prompt to necessitate multiple-step reasoning, making it more challenging for sophisticated AI. "
            "The revised prompt should be clear and answerable by humans.\n"
            "Remember, do not make the prompt verbose and limit your additions to 10 to 20 words.\n\n"
            "#Given Prompt#:\n" +
            instruction +
            "\n#Rewritten Prompt#:"
        )
        
        # Define the prompt for in-breadth evolving
        create_new_instruction_prompt = (
            "I want you to act as a Prompt Creator.\n"
            "Your goal is to draw inspiration from the given prompt to create a brand new prompt. "
            "This new prompt should belong to the same domain as the given prompt but cover a more rare topic. "
            "The length and difficulty level should be similar. The created prompt must be reasonable and answerable by humans.\n\n"
            "#Given Prompt#:\n" +
            instruction +
            "\n#Created Prompt#:"
        )
        # Add other prompt templates as needed
        
        # Randomly select one of the prompt templates
        prompt_templates = [deepening_prompt, concretizing_prompt, increased_reasoning_steps_prompt]
        chosen_prompt = random.choice(prompt_templates)

        
        # Send the chosen prompt to the OpenAI API and get the response
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Choose the model you have access to
            prompt=chosen_prompt,
            max_tokens=256  # Adjust the max_tokens if needed
        )
        
        # Extract the rewritten prompt from the response
        evolved_instruction = response.choices[0].text.strip()
        
        # Check for the presence of the placeholder text in the evolved instruction
        if any(placeholder in evolved_instruction for placeholder in ['#Given Prompt#', '#Rewritten Prompt#', 'given prompt', 'rewritten prompt']):
            # If placeholder text is found, it means the evolution was not successful
            return instruction  # Return the original instruction unchanged
        
        return evolved_instruction

    def eliminate_evolving(self, original_instruction, evolved_instruction):
        # Define rules for elimination
        too_short = len(evolved_instruction.split()) < 6 
        contains_sorry = "sorry" in evolved_instruction.lower()
        no_information_gain = (original_instruction == evolved_instruction)
        only_stopwords = all(word in {"a", "the", "and", "of", "in", ".", ",", ";"} for word in evolved_instruction.split())
        prompt_leakage = any(phrase in evolved_instruction for phrase in ["given prompt", "rewritten prompt", "#Rewritten Prompt#"])

        # Check if any criteria for elimination are met
        if too_short or contains_sorry or no_information_gain or only_stopwords or prompt_leakage:
            return False
        return True


# Load initial instruction dataset
with open('original_dataset.json', 'r') as file:
    D0 = json.load(file)

evolution_strategy = EvolutionStrategy()

# Iterate over the instruction dataset and evolve instructions
for instruction_data in D0:
    original_instruction = instruction_data['instruction']
    # Randomly choose an evolving strategy
    evolved_instruction = evolution_strategy.evolving(original_instruction)

    # Eliminate unsuccessful evolutions
    if evolution_strategy.eliminate_evolving(original_instruction, evolved_instruction):
        instruction_data['instruction'] = evolved_instruction
        # Generate response for the evolved instruction using OpenAI API
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Choose the model you have access to
            prompt=evolved_instruction,
            max_tokens=256  # Adjust the max_tokens if needed
        )
        instruction_data['response'] = response.choices[0].text.strip()
    else:
        # If evolution is not successful, keep the original instruction
        pass

# Save the evolved instruction dataset
with open('evolved_dataset.json', 'w') as file:
    json.dump(D0, file, indent=4)





