# RSbench

This is the codebase for the report: "MoCoDPL - The impact of self-supervision on neuro-symbolic learning", largely influenced by ["A Neuro-Symbolic Benchmark Suite for Concept Quality and Reasoning Shortcuts"](https://arxiv.org/abs/2406.10368) and ["An Empirical Study of Training Self-Supervised Vision Transformers
"](https://arxiv.org/abs/2104.02057) papers. The project added a pipeline for self-supervision to the original DPL neuro-symbolic model by replacing its convolutional encoder with MoCo-ViT. A pretrained version can be loaded by using the flag ```--moco-pretrained```. The pretrained encoder is trained for 1000 epochs on the Kand-Logic dataset itself (not transfer learning).

## Content Overview

- **`rsscount`**: Use this module to count RSs in your datasets.
  
- **`rsseval`**: Evaluate the presence and impact of RSs using the `rsbench` datasets.
  
- **`rssgen`**: Generate datasets designed to study and analyze RSs effectively.

Most changes made are in ```rsseval/rss```.

## List of Changes
- **`backbones`**: Added main_moco.py, vits.py, the moco folder and model weights for the MoCo-ViT encoder. Changes have been made to the vits.py file compared to the codebase at [link](https://github.com/facebookresearch/moco-v3) to accommodate DPL-compatible image encoding.
- **`data`**: For the dataset, please follow the instructions at [link](https://unitn-sml.github.io/rsbench/) to download the original Kand-Logic dataset. A custom dataset can be generated, but the concepts annotated do not match the format required by the current implementation.
- **`datasets`**: Most changes occur in ```kandinsky.py``` to implement the MoCo-ViT encoder.
- 
- 
## Website

For more info, go to the dedicated website for rsbench: [link](https://unitn-sml.github.io/rsbench/).
