'''

vparses --input (required)

parses --keyword (optional default "")

parses --out (optional)

reads lines

filters by keyword (empty keeps all)

prints:

Total lines: X

Matched lines: Y

if --out provided, write filtered lines to that file and print Wrote Y lines to <out>
'''


import argparse

def read_lines(path):
    with open(path,"r",encoding="utf-8") as f:
        return f.readlines()
    
def filter_line(lines,keywords):
    if keywords=="":
        return lines
    else: return [ln for ln in lines if keywords in ln]

def write_line(out, lines):
    with open(out, "w",encoding="utf-8") as f:
        f.writelines(lines)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--keywords", default="")
    p.add_argument("--out")
    arg=p.parse_args()

    lines =read_lines(arg.input)
    filterd=filter_line(lines,arg.keywords)
    print(len(lines))
    print(len(filterd))

    if arg.out:
        write_line(arg.out,filterd)
        print(f"write {len(filterd)} to {arg.out}")

if __name__ == "__main__":
    main()


