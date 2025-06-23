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
- **`models`**, **`utils`** and ```main.py```: Same as above for files ```kanddpl.py``` and ```args.py```
- New tools were also created in the main folder for .joblib file viewing and training with bash.

## How to Use (simple)
- Download and unzip the Kand-Logic dataset into the ```data``` folder.
- Change your directory to ```rss``` and run the bash file via ```./train_seeds.sh```. THe best model from each of the 5 seeds will be saved in the main folder.
- Replace the filepaths in ```evaluate.py``` with your actual filepaths. Make sure to change the project name, entity, c_sup and other flags such as --moco (for running a randomly initialized MoCo-ViT) and --moco-pretrained (MoCo-ViT with weights loaded). Only one of these MoCo flags can be used at once (omit to run without MoCo). Run ```python evaluate.py``` to evaluate all 5 best models. The means and SDs of the metrics will be available in a .txt file.
- The confusion matrices shown in the paper are taken from the training results of the last seed. (The confusion matrices in the evaluation results are not separated by color and shape.)

## Website

For more info, go to the dedicated website for rsbench: [link](https://unitn-sml.github.io/rsbench/).
