#!/bin/bash
for dir in $(ls -d ./*/)
do
  python $dir"/benchmark.py"
done

echo """
"""