import argparse
parser = argparse.ArgumentParser
parser, add_argument("n")
args = parser.parse_args()
n = args.n
for i in range (1,n*2+1):
    if i % 2 == 0:
        print(i)