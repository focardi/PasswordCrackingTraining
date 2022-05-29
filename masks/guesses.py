import re
import sys

if len(sys.argv) < 2:
    print(f'** Password guessability through masks **')
    print(f'   Usage: python3 {sys.argv[0]} password')
    exit(1)

password=sys.argv[1]

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
BASENAME = 'training_statsgen_sorted'
SOURCE =  f'{BASENAME}.txt'

def compute_mask(pwd):
    r=''
    for c in pwd:
        if c in lower:
            r+='?l'
        elif c in upper:
            r+='?u'
        elif c in digits:
            r+='?d'
        elif c in symbols:
            r+='?s'
        else:
            print(f'Unrecognized char: {c}')
            exit(1)
    return r

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

mask = compute_mask(password)

print(f'[*] Computing guesses for password \'{password}\' mask = \'{mask}\'')

# Builds a list with trained frequencies
progress  = 0
print(f'[*] Reading masks from training: {SOURCE}')
with open(SOURCE,'r') as f:
    for d in f:
        m,f = read_mask(d)
        if m==mask:
            print(f'[*] Guesses = {progress}')
            exit(0)
        progress += compute_guesses(m)

print('[-] Not found!')
