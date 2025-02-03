import csv
import os
import matplotlib.pyplot as plt

# pull latest master in steamHWsurvey repo
os.system("git -C steamHWsurvey switch --discard-changes --recurse-submodules master")
os.system("git -C steamHWsurvey pull")

arch_mapping = {}
with open('arch_mapping.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # ignore the header
        if row[0] == 'name':
            continue
        arch_mapping[row[0]] = row[1]

missing_mappings = set()

plot_colors = {}
with open('arch_colors.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # ignore the header
        if row[0] == 'architecture':
            continue
        plot_colors[row[0]] = row[1]

missing_colors = set()

def update_gpu_arch_stats(description_filter, file_suffix = ""):
    arch_stats = {}

    with open('steamHWsurvey/shs_platform.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] == 'pc' and row[2] == description_filter:
                date = row[0]
                gpu = row[3]
                percentage = float(row[5])
                if gpu not in arch_mapping:
                    missing_mappings.add(gpu)
                arch = arch_mapping.get(gpu, 'Unknown')
                current_stats = arch_stats.setdefault(date, {})
                current_stats.setdefault(arch, 0)
                current_stats[arch] += percentage

    output_file = 'arch_stats' + file_suffix + '.csv'
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date', 'gpu architecture', 'percentage'])
        for date, stats in arch_stats.items():
            for arch, percentage in stats.items():
                writer.writerow([date, arch, percentage])

    output_file_latest = 'arch_stats' + file_suffix + '_latest.csv'
    with open(output_file_latest, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['gpu architecture', 'percentage'])
        latest_date = max(arch_stats.keys())
        latest_stats = arch_stats[latest_date]
        for arch, percentage in latest_stats.items():
            writer.writerow([arch, percentage])

    dates_to_plot = []
    years_found = {}
    
    for date, stats in arch_stats.items():
        year = date[:4]
        if (year not in years_found):
            years_found[year] = True
        else:
            continue
        dates_to_plot.append(date)
    
    archs_to_plot = {}
    for date, stats in arch_stats.items():
        if (date not in dates_to_plot):
            continue
        for arch, percentage in stats.items():
            current_stats = archs_to_plot.setdefault(arch, [])
            current_stats.append((date, percentage))

    archs_to_plot = list(archs_to_plot.items())
    archs_to_plot.sort(key=lambda x: x[0])

    for xkcd in [False, True]:
        if xkcd:
            plt.xkcd()
        else:
            plt.rcdefaults()

        for arch, stats in archs_to_plot:
            stats_dict = dict(stats)
            for date in dates_to_plot:
                if date not in stats_dict:
                    stats.append((date, 0))
            stats.sort(key=lambda x: x[0])
            dates, percentages = zip(*stats)
            if arch not in plot_colors:
                missing_colors.add(arch)
            color = plot_colors.get(arch, '#ff00ff')
            color = color.strip()
            plt.plot(dates, percentages, label=arch, color=color)

        if xkcd:
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')
        else:
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.xlabel('Date')
        plt.ylabel('Percentage')
        plt.title('GPU Architecture Usage')
        fig = plt.gcf()
        fig.set_size_inches(20, 10)
        
        output_plot = 'arch_stats' + file_suffix + ('_xkcd' if xkcd else '') + '.png'
        plt.savefig(output_plot)
        plt.close()

update_gpu_arch_stats('Video Card Description (Windows)')
update_gpu_arch_stats('DirectX 12 Systems (Win10 with DX 12 GPU)', '_dx12')

if missing_mappings:
    for missing in missing_mappings:
        arch_mapping[missing] = 'Unknown'

    arch_mapping = dict(sorted(arch_mapping.items()))
    # add the header back to the beginning
    arch_mapping = {'name': 'architecture'} | arch_mapping

    with open('arch_mapping.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for gpu, arch in arch_mapping.items():
            writer.writerow([gpu, arch])

if missing_colors:
    for missing in missing_colors:
        plot_colors[missing] = ' #ff00ff'

    plot_colors = dict(sorted(plot_colors.items()))
    # add the header back to the beginning
    plot_colors = {'architecture': 'color'} | plot_colors

    with open('arch_colors.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for arch, color in plot_colors.items():
            writer.writerow([arch, color])
