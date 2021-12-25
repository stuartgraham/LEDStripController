#!/bin/bash
export CFLAGS=-fcommon
pip install RPi.GPIO
python -u main.py