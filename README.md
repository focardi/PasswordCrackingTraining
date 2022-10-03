# Automated Training of Password Cracking Tools

This repository collects data and scripts of the paper: 

Di Campi, A.M., Focardi, R., Luccio, F.L. (2022). 
The Revenge of Password Crackers: Automated Training of Password Cracking Tools. ESORICS 2022 [[DOI](https://doi.org/10.1007/978-3-031-17146-8_16)]

## Mask attacks

- [guesses.py](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/guesses.py): computes the number of guesses for a give password using trained masks. Requires to gunzip `training_statsgen_sorted.txt.gz`
- [simulation_mask_attack.py](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/simulation_mask_attack.py): simulate a mask attack using trained masks and tested masks. Requires to gunzip both `training_statsgen.txt.gz` and `testing_statsgen.txt.gz`.
- [training_statsgen.txt.gz](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/training_statsgen.txt.gz): masks computed by Train_D (gzipped)
- [testing_statsgen.txt.gz](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/testing_statsgen.txt.gz): masks computed by Test_D (gzipped)
- [uncracked_statsgen.txt.gz](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/uncracked_statsgen.txt.gz): masks computed by the passwords that could not be cracked using TRule2.rule rule-based attack (gzipped)
- [training_statsgen_sorted.txt.gz](https://github.com/focardi/PasswordCrackingTraining/blob/master/masks/training_statsgen_sorted.txt.gz): masks sorted by |m|/f used in guesses.py (gzipped)

## Rule-based attacks

- [TRule.rule](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule.rule): Rules trained using all the rule sets provided in the hashcat distribution plus OneRuleToRuleThemAll and popular.rule of pantagrule, sorted by descending frequencies
- [TRule_freq.rule](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule_freq.rule): As above with frequencies
- [TRule2.rule](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule2.rule): Rules trained using the the 3726 best rules of TRule and TrainDic_D
- [TRule2_freq.txt](https://github.com/focardi/PasswordCrackingTraining/blob/master/rules/TRule2_freq.rule): As above with frequencies
