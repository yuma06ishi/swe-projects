'''
Problem: Build a CLI tool that:

--input required

--keyword optional default "" (empty means keep all)

--out optional (if provided, write filtered lines)

Always print summary:

total lines

matched lines

keywor
'''

import argparse

def read_lines (path):
    with open(path,"r",encoding="utf-8") as f:
        lines = f.readlines()
        return lines
    
def filter_lines(lines,keyword):
    if keyword=="":
        return lines
    return [ln for ln in lines if keyword in ln]

def write_lines(path,lines):
    with open(path, "w",encoding="utf-8") as f:
        f.writelines(lines)

def write_summary(total,matched, keyword):
    return (
        f"Total line: {total}\n"
        f"Matched line: {matched}\n"
        f"keyword: {keyword!r}"
    )
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    p.add_argument("--keyword",default="")
    p.add_argument("--out")
    args=p.parse_args()

    try:
        lines=read_lines(args.input)
    except FileNotFoundError:
        print("File not found")
        raise SystemExit(1)
    
    filterd=filter_lines(lines,args.keyword)
    print(write_summary(len(lines),len(filterd),args.keyword))

    if args.out:
        write_lines(args.out,filterd)
    



if __name__ == "__main__":
    main()
