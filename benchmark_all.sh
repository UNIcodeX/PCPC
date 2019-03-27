#!/bin/bash
for dir in `ls -d1 "$PWD/"*/`
do
  cd $dir
  python benchmark.py
done

echo """
"""
