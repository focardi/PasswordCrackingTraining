# Automated Training of Password Cracking Tools

This repository collects data and scripts of paper "Automated Training of Password Cracking Tools".

## Mask attacks

- [guesses.py](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/guesses.py): computes the number of guesses for a give password using trained masks
- [simulation_mask_attack.py](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/simulation_mask_attack.py): simulate a mask attack using trained masks and tested masks
- [testing_statsgen.txt.gz](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/testing_statsgen.txt.gz): masks computed by Test_D (gzipped)
- [training_statsgen.txt.gz](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/training_statsgen.txt.gz): masks computed by Train_D (gzipped)
- [training_statsgen_sorted.txt.gz](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/training_statsgen_sorted.txt.gz): masks sorted by |m|/f used in guesses.py (gzipped)

## Rule-based attacks

- [TRule.rule](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule.rule): Rules trained using all the rule sets provided in the hashcat distribution plus OneRuleToRuleThemAll and popular.rule of pantagrule, sorted by descending frequencies
- [TRule_freq.rule](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule_freq.rule): As above with frequencies
- [TRule2.rule](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule2.rule): Rules trained using the the 3726 best rules of TRule and TrainDic_D
- [TRule2_freq.txt](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule2_freq.rule): As above with frequencies
