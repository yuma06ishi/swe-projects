import csv
import argparse

def read_csv(input):
    with open(input, "r",encoding="utf-8") as f:
        readline=csv.DictReader(f)
        return list(readline)
    
def filter_rows(rows,column,value):
    return [row for row in rows if row[column]==value]

def select_columns(rows,columns):
    return [{col:row[col] for col in columns} for row in rows]

def write_csv(output, rows,fieldnames):
    with open(output,"w",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    p.add_argument("--filter-col")
    p.add_argument("--filter-val")
    p.add_argument("--select-cols")
    p.add_argument("--out")
    args=p.parse_args()

    rows=read_csv(args.input)
    final_rows=rows

    if args.filter_col and args.filter_val:
        final_rows=filter_rows(final_rows,args.filter_col,args.filter_val)
    
    if args.select_cols:
        columns=args.select_cols.split(",")
        final_rows=select_columns(final_rows,columns)
        fieldname=columns
    elif rows:
        fieldname=rows
    else: filedname=[]

    print(f"total: {len(rows)}")
    print(f"final:{len(final_rows)}")

    if args.out:
        write_csv(args.out,final_rows,fieldname)
        print(f"wrote output CSV tp {args.out}")


if __name__=="__main__":
    main()

