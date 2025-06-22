#!/bin/bash

seeds=(123 456 789 1011 1213)
eps=(10 100 200)
for seed in "${seeds[@]}"
do
    python main.py --dataset kandinsky --model kanddpl --n_epochs 100 --lr 0.001 --seed "$seed" --batch_size 256 --exp_decay 0.9 --c_sup 0.5 --task patterns --backbone conceptizer --wandb "mayleyc" --proj_name "250622_kanddpl_mocopre_100_0.5" --project "Reasoning-Shortcuts-MoCopre-csup0.5-250622" --moco-pretrained
done
echo "All jobs submitted with different seeds."

#250619_kanddpl_nomoco: n_epochs 10, lr 0.001, batch_size 128, exp_decay 0.9, c_sup 0, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-noMoCo-250619"
# 250620_kanddpl_nomoco_100: n_epochs 100, lr 0.001, batch_size 128, exp_decay 0.9, c_sup 0, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-noMoCo-250620"
# 250620_kanddpl_mocopre_10: n_epochs 10, lr 0.001, batch_size 128, exp_decay 0.9, c_sup 0, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-MoCopre10-250620"--moco-pretrained
# 250620_kanddpl_nomoco_100_0.5: n_epochs 100, lr 0.001, batch_size 256, exp_decay 0.9, c_sup 0.5, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-noMoCo-csup0.5-250620"
# 250620_kanddpl_nomoco_100_1: n_epochs 100, lr 0.001, batch_size 256, exp_decay 0.9, c_sup 1, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-noMoCo-csup1-250620"
# 250621_kanddpl_mocoft_100_0.5: n_epochs 100, lr 0.001, batch_size 256, exp_decay 0.9, c_sup 0.5, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-MoCoft-csup0.5-250621" --moco
# 250621_kanddpl_mocopre_100_0.5: n_epochs 100, lr 0.001, batch_size 256, exp_decay 0.9, c_sup 0.5, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-MoCopre-csup0.5-250621" --moco-pretrained
# 250620_kanddpl_mocopre_100_0: n_epochs 100, lr 0.001, batch_size 256, exp_decay 0.9, c_sup 0, task patterns, backbone conceptizer --project "Reasoning-Shortcuts-MoCopre-csup0-250620" --moco-pretrained