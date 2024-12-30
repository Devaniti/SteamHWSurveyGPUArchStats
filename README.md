# arch_mapping.csv

* Manually authored list of mappings between GPU names and Architecture names

* For many GPUs (especially AMD) same name can refer to different GPUs of different architectures (e.g. `AMD Radeon R7 Graphics`)

* There are also cases when GPUs with same names can have different chips of different architectures (e.g. `GeForce GT 740`)

* Errors are also possible, if you think you've found one feel free to open pull request

# arch_stats.csv

* Automatically generated using data from [jdegene/steamHWsurvey](https://github.com/jdegene/steamHWsurvey) repo and arch_mapping.csv

* Meant to be periodically updated when there's new data in the [jdegene/steamHWsurvey](https://github.com/jdegene/steamHWsurvey) repo

# arch_stats_latest.csv

* Same as `arch_stats.csv` but only includes latest data and removes date column

* This is duplicate of data in the `arch_stats.csv` and meant only for convenience when only latest data is required

# Notes

* There are a lot of notes regarding original dataset in the [jdegene/steamHWsurvey README](https://github.com/jdegene/steamHWsurvey?tab=readme-ov-file#shscsv)

* Thanks to [jdegene](https://github.com/jdegene) for maintaining original dataset 👍
