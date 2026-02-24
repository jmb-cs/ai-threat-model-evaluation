# Evaluation of AI-driven threat modelling tools

Repository with examples of threat models created by AI-driven threat modelling tools, and implementation of an evaluation method for judging the "correctness" of the models.

## Repo Structure
The repository contains the raw threat models pulled from STRIDEgpt, the STRIDEgpt input and base models for each system, and full results of comparing each baseline with all of the generated threat models.

The raw generated threat models are found in:
- gemini_2_5_pro
- gpt_5_1
- qwen_3_235b_thinking
With the reformatted threat models are in the `results`-folder

Baseline threat models are found in `threat_templates`, the full threat model in json format, along with the system description and other parameter setting for STRIDEgpt.

The measured comparisons are found in the `stats`-folder, with the full comparison results in the `<model_name>_scored_<type>.json` files, and the actual overlapping results in the `<model_name>_similar_<type>.json` files. The `similarity_summary.json`contains the accumulated results for each baseline per model.

## Setup project on Ubuntu

1. Create virtual environment `python3 -m venv threat_venv`
2. Activate the environment with `source threat_venv/bin/activate`
3. Install needed modules `pip3 install -r requirements.txt`

*You might need to install graphviz on your OS as well*

## Reproducing results
The results can be verified by running STRIDEgpt separately, using the exact same models, and then downloading the results of each part of the threat modelling process, for this you should insert the *description* and select the matching *general application notions* in STRIDEgpt. The files should then be inserted in the models folder, and any extra lines after the markdown tables should be removed, as this will break the reformatting flow. 

After this, you will need to run the `extract_threat_models.py`-file in the terminal, edit the file by changing the `application`variable to the name of the basemodel you wish to rerun, this should match the corresponding folder.

After this you can reproduce the comparison results by running the jupyter notebook, corresponding the chosen basemodel, for example for the IoT system, this would be the `compare_iot.ipyb`.

## DFDs

It uses the *data-flow-diagram* module in python, the package and syntax is described here:
[DFD module](https://github.com/pbauermeister/dfd/blob/main/doc/README.md).

To render the dfd descriptions use  \
`data-flow-diagram [--output-file <OUTPUT-FILE-NAME>] [--format <gif,jpg,pdf>] <INPUT-FILE-NAME>`

The default command outputs the diagram as <INPUT-FILE-NAME>.svg, and it is possible to specify
a different output file name and format, there are more formats than the ones listed above.
