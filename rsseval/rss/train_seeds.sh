#!/bin/bash

seeds=(123 456 789 1011 1213)

for seed in "${seeds[@]}"
do
    python main.py --dataset kandinsky --model kanddpl --n_epochs 10 --lr 0.001 --seed "$seed" --batch_size 64 --exp_decay 0.9 --c_sup 0 --task patterns --backbone conceptizer --moco-pretrained
done
echo "All jobs submitted with different seeds."