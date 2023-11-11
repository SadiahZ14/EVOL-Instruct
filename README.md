# Evol-Instruct: Evolving Instructions for Language Model Training

## Overview
Evol-Instruct is an innovative approach to training large language models (LLMs) by automating the generation of instruction-following data with varying complexity levels. This method alleviates the need for manual, time-consuming, and labor-intensive data creation processes, typically challenging to scale for high-complexity instructions.

Inspired by the research presented in the paper "WizardLM: Empowering Large Language Models to Follow Complex Instructions", Evol-Instruct utilizes an initial dataset of instructions and rewrites them into more complex forms. The fine-tuned model, known as WizardLM, exhibits superior performance in complexity-balanced evaluations and automatic skill assessments compared to human-crafted instruction data and even outperforms OpenAI ChatGPT in certain aspects.

## Features
- **Automated Instruction Evolution**: With Evol-Instruct, you can automatically rewrite simple instructions into more complex ones, enabling the training of more robust LLMs.
- **Human-like Complexity**: The evolved instructions are designed to mimic human-level complexity, enhancing the model's ability to handle real-world tasks.
- **Skill Assessment**: WizardLM demonstrates over 90% of ChatGPT's capacity across 17 out of 29 evaluated skills, showcasing the effectiveness of AI-evolved instructions.

## A summary of the cycle of EVOL-Instruct as presented in the paper ["WizardLM: Empowering Large Language Models to Follow Complex Instructions"](https://arxiv.org/abs/2304.12244).
* Prepare Initial Data:<br>
Start with a set of simple instructions in a JSON format, which will be used as the seed for evolving complex instructions.
* Run Evol-Instruct:<br>
Execute the main script to begin the evolution process:
* Train Your Model:
After generating the evolved instruction data, you can shuffle it with original dataset and fine-tune your LLM using the provided training scripts.

![Evolution and Technical Details 2](https://github.com/SadiahZ14/EVOL-Instruct/assets/100665526/4acb85fc-c6ea-4d87-aca6-828f3794d769)

## Contribution
Contributions to Evol-Instruct are welcome! Whether it's feature requests, bug reports, or code contributions, feel free to open an issue or create a pull request.
