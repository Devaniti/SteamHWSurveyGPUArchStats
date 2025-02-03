# arch_mapping.csv

* Manually authored list of mappings between GPU names and Architecture names

* For many GPUs (especially AMD) same name can refer to different GPUs of different architectures (e.g. `AMD Radeon R7 Graphics`)

* There are also cases when GPUs with same names can have different chips of different architectures (e.g. `GeForce GT 740`)

* Errors are also possible, if you think you've found one feel free to open pull request

* Automatically updated to include new GPUs by `updateGPUArchStats.py`, after which newly added GPUs need to be manually categorized

# arch_stats.csv

* Automatically generated using data from [jdegene/steamHWsurvey](https://github.com/jdegene/steamHWsurvey) repo and arch_mapping.csv

* Meant to be periodically updated when there's new data in the [jdegene/steamHWsurvey](https://github.com/jdegene/steamHWsurvey) repo

# arch_stats_latest.csv

* Same as `arch_stats.csv` but only includes latest data and removes date column

* This is duplicate of data in the `arch_stats.csv` and meant only for convenience when only latest data is required

# arch_stats_dx12.csv / arch_stats_dx12_latest.csv

* They are equivalent to aforementoined ones, with the difference that dx12 ones only includes DX12 compatible system

# arch_stats.png / arch_stats_xkcd.png

* Graphs that show movement of architecture market shares

* For keep graph size manageable, it only include one data point per year

# arch_stats_dx12.png / arch_stats_dx12_latest.png

* Same as aforementioned graphs, but only include dx12 compatible systems

# arch_colors.csv

* Manually authored list of mappings between architectures and graph colors

* Intention is to keep colors of architectures of every vendor to be shades of that vendors signature color

* Automatically updated to include new Architectures by `updateGPUArchStats.py`, after which newly added architectures need manual color assignment

# Notes

* There are a lot of notes regarding original dataset in the [jdegene/steamHWsurvey README](https://github.com/jdegene/steamHWsurvey?tab=readme-ov-file#shscsv)

* Thanks to [jdegene](https://github.com/jdegene) for maintaining original dataset 👍
