# KandDPL-MoCov3
Implementation of self-supervision method MoCov3 to the DPL neuro-symbolic model, on the Kandinsky dataset (Marconato et al., 2024).


## Link to Original RSbench 

This is adapted from the official codebase for ["A Neuro-Symbolic Benchmark Suite for Concept Quality and Reasoning Shortcuts"](https://arxiv.org/abs/2406.10368) paper, [NeurIPS 2024](https://neurips.cc/Conferences/2024/). This suite provides tools to evaluate and generate datasets focused on [Reasoning Shortcuts (RSs)](https://arxiv.org/abs/2305.19951) .

For more info, go to the dedicated website: [link](https://unitn-sml.github.io/rsbench/).

## Content Overview
Important changes are made in the rsseval/rss folder.

- Backbones: MoCo files were added from [link](https://github.com/facebookresearch/moco-v3/tree/main/moco), and modified for compatibility with KandDPL (added linear layer and torch.split). To run the ```--moco-pretrained``` option, unzip the trained MoCo checkpoint from [link](https://1drv.ms/u/c/73bae07ce4f6ca55/EcR0W17g8F9Irwxqt221TkkBvPV_XPY3FMmQm6W75pfuDA?e=Dctx0A) and place the checkpoint in ``` kanddpl-moco/rsseval/rss/backbones/ ```
- Dataset, Models and Utils: MoCo components (arguments, feature extraction) were added to get_backbone and the KandDPL class.

## Running
###Training:
- A pretrained MoCo model is provided in [link](https://1drv.ms/u/c/73bae07ce4f6ca55/EcR0W17g8F9Irwxqt221TkkBvPV_XPY3FMmQm6W75pfuDA?e=Dctx0A). It is trained on the y label (not concepts) of the original Kandinsky dataset (Marconato et al., 2024) for 1000 epochs.


## References




