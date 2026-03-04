''''
Problem

Create wednesday_log_cli.py that:

reads lines

filters by keyword (empty keeps all)

computes total and matched

prints a 3-line summary using a make_summary() function

optionally writes output if --out is provided

'''



import argparse

def read_lines(input):
    with open(input, "r",encoding="utf-8") as f:
        return f.readlines()
def filter(lines, keyword):
    if keyword=="":
        return lines
    return [ln for ln in lines if keyword in ln]

def write_lines(output,lines):
    with open(output, "w", encoding="utf-8") as f:
        f.writelines(lines)
    
def summary(lines,filterd,keyword):
   return(
       f"Total lines: {len(lines)}\n"
       f"Matched lines: {len(filterd)}\n"
       f"keyword: {keyword!r}"


   )

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--keyword", default="")
    p.add_argument("--out")
    args=p.parse_args()

    lines=read_lines(args.input)
    filterd=filter(lines,args.keyword)

    print(summary(lines,filterd,args.keyword))
    if args.out:
        write_lines(args.out, filterd)
        print(f"write {len(filterd)}: to {args.out}")

if __name__ =="__main__":
    main()


