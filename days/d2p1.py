import csv
import pandas as pd
num = 0

with open('data/d2_input.csv','r') as f:
        lines = [l.strip() for l in f]

reports = [[int(x) for x in l.split()] for l in lines]

for r in reports:
    if all(1<=y-x<=3 for x,y in zip(r,r[1:])) or all(1<=x-y<=3 for x,y in zip(r,r[1:])):
        num += 1


def is_report_safe(report: list[int]) -> bool:
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    all_increasing = all(diff > 0 for diff in diffs)
    all_decreasing = all(diff < 0 for diff in diffs)

    if not (all_increasing or all_decreasing):
        return False
    
    all_distances_safe = all(abs(diff) >= 1 and abs(diff) <= 3 for diff in diffs)
    
    return all_distances_safe

def is_report_safe_v2(report: list[int]) -> bool:
    if is_report_safe(report):
        return True
    for i in range(0, len(report)):
        sub_report = report[:i]+ report[i + 1 :]
        if is_report_safe(sub_report):
            return True
    return False