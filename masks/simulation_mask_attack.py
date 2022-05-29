import re
from matplotlib import pyplot as plt

lower   = 'abcdefghijklmnopqrstuvwxyz'
upper   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits  = '0123456789'
symbols = ' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

assert (len(lower)   == 26)
assert (len(upper)   == 26)
assert (len(digits)  == 10)
assert (len(symbols) == 33)

cost = {
    'l':len(lower),
    'u':len(upper),
    'd':len(digits),
    's':len(symbols),
    }

# Trained masks
BASENAME = 'training_statsgen'
SOURCE =  f'{BASENAME}.txt'

# Masks from test
TESTNAME = 'testing_statsgen.txt'
TESTTOTAL = 144740239

# Plots the simulation
OUTFILE =  'testing_statsgen.png'

# Cost for mask
def compute_guesses(mask):
    r = 1
    for i in range(1,len(mask),2):
        r *= cost[mask[i]]
    return r

# Parser for mask and frequency
def read_mask(d):
    r = re.search('((\?[dlsu])+),([0-9]+)$',d)
    mask = r.group(1)
    freq = int(r.group(3))
    return mask,freq

print(f'[*] Reading all test masks')
test_total=0

# Builds the hashmap
H_test = {}
with open(TESTNAME,'r') as f:
    for d in f:
        m,f = read_mask(d)
        assert(m not in H_test)
        H_test[m] = f
        test_total+=f

assert test_total==TESTTOTAL

print(f'    [*] Total masks {len(H_test)}')
print(f'    [*] Total recovered passwords in testing {test_total}/{TESTTOTAL} ({round(test_total/TESTTOTAL*100,2)})')

# Sorting is done later because we don't have yet the data in memory

# Builds the list with trained and tested frequencies
M_L = []
train_total=0
sim_recovered=0
sim_done=set([])
print(f'[*] Reading masks from training: {SOURCE}')
print(f'[*] ... and then comparing with testing: {TESTNAME}')
with open(SOURCE,'r') as f:
    for d in f:
        m,f = read_mask(d)
        train_total+=f
        if m in H_test:
            M_L.append((m,f,H_test[m]))
            sim_recovered+=H_test[m]
            assert m not in sim_done
            sim_done |= set([m])
        else:
            M_L.append((m,f,0))

# This is not in the paper
print('    [*] Computing statistics for missing masks')
sim_stats={}
sim_nonrecovered=0
sim_missingmasks=0
for m in H_test:
    if m not in sim_done:
        sim_missingmasks+=1
        sim_nonrecovered+=H_test[m]
        if H_test[m] in sim_stats:
            sim_stats[H_test[m]]+=1
        else:
            sim_stats[H_test[m]]=1

assert sim_nonrecovered == test_total-sim_recovered
print(f'    [*] Read {len(M_L)} masks')
print(f'    [*] Total recovered passwords in training {train_total}')
print(f'[*] Total recovered passwords in simulation {sim_recovered}/{test_total} ({round(sim_recovered/test_total*100,2)})')
print(f'[*] Stats nonrecovered: {sim_stats}')
print(f'[*] Missing masks: {sim_missingmasks}/{len(H_test)} ({round(sim_missingmasks/len(H_test)*100,2)}%)')

# We do sorting here, in the paper is done before. It is equivalent as we
# use f_train for sorting
print(f'[*] Sorting masks')
M_L = sorted(M_L, key=lambda x:compute_guesses(x[0])//x[1])

progress  = [1]
recovered = [0]
rec=0
rec_training=0
recovered_training = [0]

print(f'[*] Plotting')
missing=0
annotated=False
annotated2=False
for m,f_train,f_test in M_L:
    rec += f_test
    if f_test==0:
        missing+=1
    rec_training += f_train
    progress.append (progress[-1] + compute_guesses(m))
    recovered.append(round(rec/test_total*100,2))
    recovered_training.append(round(rec_training/train_total*100,2))
    if not annotated and progress[-1] > 10**12:
        annotated=True
        plt.annotate(f'{recovered[-1]}%', xy=(progress[-1],recovered[-1]), xytext=(progress[-1]/10**4,recovered[-1]+10),arrowprops=dict(arrowstyle="->"))
        print(f'    [*] {recovered[-1]} reached at {progress[-1]/10**12}*10^12')
    if not annotated2 and recovered[-1] > 90:
        annotated2=True
        plt.annotate(f'{recovered[-2]}%', xy=(progress[-2],recovered[-2]), xytext=(progress[-2]/10**5,recovered[-2]+5),arrowprops=dict(arrowstyle="->"))
        print(f'    [*] 90% reached at {progress[-2]/10**19}*10^19')

print(f'[*] unmatched training masks = {missing}')
plt.plot(progress,recovered,label='Test$_D$')
plt.plot(progress,recovered_training,label='Train$_D$')
plt.xlabel("Guesses")
plt.ylabel("Recovered %")
plt.xscale('log')

plt.xlim(left=1)
plt.legend()
plt.grid()
plt.savefig(OUTFILE,dpi=300)