import csv
import argparse

def read_csv(input):
    with open(input,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        rows=list(reader)
        return rows
    
def filter_rows(rows, columns,value):
    return [row for row in rows if row[columns]==value]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--filter-col")
    p.add_argument("--filter-value")
    args=p.parse_args()

    rows=read_csv(args.input)
    for row in rows[:3]:
        print(row)


    if args.filter_col and args.filter_value:
        filtered=filter_rows(rows, args.filter_col,args.filter_value)
        print("filtered")
        for row in filtered:
            print(row)

if __name__ =="__main__":
        main()



    