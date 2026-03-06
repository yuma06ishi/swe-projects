'''
parses --input, --keyword, --out

reads file safely (handle FileNotFoundError, PermissionError)

filters (empty keyword keeps all)

prints summary

writes output if requested

works correctly for empty file (0 totals)
'''

import argparse

def read_lines(input):
    with open(input, "r", encoding="utf-8") as f:
        return f.readlines()
    
def safe_read_lines(input):
    try:
        return read_lines(input)
    except FileNotFoundError:
        print("File not Found")
        raise SystemExit(1)
    except PermissionError:
        print("permission error")
        raise SystemExit(1)

def filter_lines(lines,keyword):
    if keyword=="":
        return lines
    return [ln for ln in lines if keyword in ln]

def write_lines(out,lines):
    with open(out, "w", encoding="utf-8") as w:
        w.writelines(lines)

def make_summary(lines, filtered,keyword):
    return (
        f"total lines: {len(lines)}\n"
        f"matched line: {len(filtered)}\n"
        f"keyword: {keyword!r}"


    )

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--keyword", default="")
    p.add_argument("--out")

    args=p.parse_args()

    lines=safe_read_lines(args.input)
    filtered=filter_lines(lines,args.keyword)
    print(make_summary(lines,filtered,args.keyword))
    if args.out:
        write_lines(args.out,filtered)
        print(f"wrote {len(filtered)} to the {args.out}")

if __name__ =="__main__":
    main()
