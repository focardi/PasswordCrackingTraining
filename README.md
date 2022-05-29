# Automated Training of Password Cracking Tools

This repository collects data and script of paper "Automated Training of Password Cracking Tools".

## Mask attacks

- [guesses.py](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/guesses.py): computes the numer of guesses for a give password using trained masks
- [simulation_mask_attack.py](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/simulation_mask_attack.py): simulate a mask attack using trained masks and tested masks
- testing_statsgen.png: plot generated by simulation_mask_attack.py showing training and testing
- testing_statsgen.txt: masks computed by Test_D
- training_statsgen.txt: masks computed by Train_D
- training_statsgen_sorted.txt: masks sorted by |m|/f used in guesses.py

## Rule-based attacks

- TRule.rule: Rules trained using all the rule sets provided in the hashcat distribution plus OneRuleToRuleThemAll and popular.rule of pantagrule, sorted by descending frequencies

- TRule_freq.rule: As above with frequencies

- TRule2.rule: Rules trained using the the 3726 best rules of TRule and TrainDic_D

- TRule2_freq.txt: As above with frequencies