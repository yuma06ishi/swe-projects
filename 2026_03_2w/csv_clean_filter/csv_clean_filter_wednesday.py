import argparse
import csv

def read_csv(input):
    with open (input, "r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        return list(reader)
def filter_rows(rows,column,value):
    return [row for row in rows if row[column]==value]

def select_columns(rows,columns):
    return [{col: row[col] for col in columns} for row in rows]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--filter-col")
    p.add_argument("--filter-val")
    p.add_argument("--select-cols")
    args=p.parse_args()

    rows=read_csv(args.input)
    final_rows=rows
    if args.filter_col and args.filter_val:
        final_rows=filter_rows(final_rows,args.filter_col, args.filter_val)
    if args.select_cols:
        columns=args.select_cols.split(",")
        final_rows=select_columns(final_rows,columns)

        print(f"total rows: {len(rows)}")
        print(f"final rows: {len(final_rows)}")
        for rows in final_rows:
            print(rows)
if __name__ =="__main__":
    main()