#!/bin/zsh

set -e

./main.py main data/a.txt >/tmp/hashcode_data/a.out
./main.py main data/b.txt >/tmp/hashcode_data/b.out
./main.py main data/c.txt >/tmp/hashcode_data/c.out
./main.py main data/d.txt >/tmp/hashcode_data/d.out
./main.py main data/e.txt >/tmp/hashcode_data/e.out
./main.py main data/f.txt >/tmp/hashcode_data/f.out
