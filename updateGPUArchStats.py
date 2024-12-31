import csv
import os

# pull latest master in steamHWsurvey repo
os.system("git -C steamHWsurvey switch --discard-changes --recurse-submodules master")
os.system("git -C steamHWsurvey pull")

arch_mapping = {}
with open('arch_mapping.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        arch_mapping[row[0]] = row[1]

arch_stats = {}

with open('steamHWsurvey/shs_platform.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] == 'pc' and row[2] == 'Video Card Description (Windows)':
            date = row[0]
            gpu = row[3]
            percentage = float(row[5])
            arch = arch_mapping.get(gpu, 'Unknown')
            current_stats = arch_stats.setdefault(date, {})
            current_stats.setdefault(arch, 0)
            current_stats[arch] += percentage

with open('arch_stats.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['date', 'gpu architecture', 'percentage'])
    for date, stats in arch_stats.items():
        for arch, percentage in stats.items():
            writer.writerow([date, arch, percentage])

with open('arch_stats_latest.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['gpu architecture', 'percentage'])
    latest_date = max(arch_stats.keys())
    latest_stats = arch_stats[latest_date]
    for arch, percentage in latest_stats.items():
        writer.writerow([arch, percentage])
