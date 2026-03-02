\# Log Analyzer CLI



Reads a text log file, optionally filters by keyword, prints a summary, and can write filtered lines to an output file.



\## Run

```bash

python log\_cli.py --input sample.log

python log\_cli.py --input sample.log --keyword ERROR

python log\_cli.py --input sample.log --keyword ERROR --out errors.log

