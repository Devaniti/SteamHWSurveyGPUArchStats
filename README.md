# arch_mapping.csv

* Manually authored list of mappings between GPU names and Architecture names

* For many GPUs (especially AMD), the same name can refer to different GPUs of different architectures (e.g. `AMD Radeon R7 Graphics`)

* There are also cases when GPUs with the same names can have different chips of different architectures (e.g. `GeForce GT 740`)

* Errors are also possible. If you think you've found one, feel free to open a pull request

* Automatically updated to include new GPUs by `updateGPUArchStats.py`, after which newly added GPUs need to be manually categorized

# arch_stats.csv

* Automatically generated using data from [jdegene/steamHWsurvey](https://github.com/jdegene/steamHWsurvey) repo and arch_mapping.csv

* Meant to be periodically updated when there's new data in the [jdegene/steamHWsurvey](https://github.com/jdegene/steamHWsurvey) repo

# arch_stats_latest.csv

* Same as `arch_stats.csv` but only includes latest data and removes date column

* It is meant only for convenience when only the latest data is required

# arch_stats_dx12.csv / arch_stats_dx12_latest.csv

* They are equivalent to the aforementioned ones, with the difference that the dx12 ones only include DX12-compatible systems

# arch_stats.png

* Graphs that show movement of architecture market shares

* For keep graph size manageable, it only includes one data point per year

# arch_stats_dx12.png / arch_stats_dx12_latest.png

* Same as aforementioned graphs, but only include dx12 compatible systems

# arch_colors.csv

* Manually authored list of mappings between architectures and graph colors

* Intention is to keep colors of architectures of every vendor to be shades of that vendor's signature color

* Automatically updated to include new Architectures by `updateGPUArchStats.py`, after which newly added architectures need manual color assignment

# Notes

* There are a lot of notes regarding the original dataset in the [jdegene/steamHWsurvey README](https://github.com/jdegene/steamHWsurvey?tab=readme-ov-file#shscsv)

* Thanks to [jdegene](https://github.com/jdegene) for maintaining the original dataset 👍
