# RSbench

This is the codebase for the report: "MoCoDPL - The impact of self-supervision on neuro-symbolic learning", largely influenced by ["A Neuro-Symbolic Benchmark Suite for Concept Quality and Reasoning Shortcuts"](https://arxiv.org/abs/2406.10368) and ["An Empirical Study of Training Self-Supervised Vision Transformers
"](https://arxiv.org/abs/2104.02057) papers. The project added a pipeline for self-supervision to the original DPL neuro-symbolic model by replacing its convolutional encoder with MoCo-ViT. A pretrained version can be loaded by using the flag ```--moco-pretrained```. The pretrained encoder is trained for 1000 epochs on the Kand-Logic dataset itself (not transfer learning).

## Content Overview

- **`rsscount`**: Use this module to count RSs in your datasets.
  
- **`rsseval`**: Evaluate the presence and impact of RSs using the `rsbench` datasets.
  
- **`rssgen`**: Generate datasets designed to study and analyze RSs effectively.

Each component is designed to help you systematically assess and understand RSs in various machine learning models.

## Website

For more info, go to the dedicated website: [link](https://unitn-sml.github.io/rsbench/).
