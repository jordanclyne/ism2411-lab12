#csv_practice.py
#Author: Jordan Clyne
#Module 12 Lab: Read a Sales CSV, Write a Cleaned Report

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

#Exercise 1: Get the File
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

#Exercise 2: Read and Print Raw Rows
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
