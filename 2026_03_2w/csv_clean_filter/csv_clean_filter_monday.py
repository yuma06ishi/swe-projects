import csv
import argparse

def read_csv(path):
    with open(path,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        return list(reader)
    
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    args=p.parse_args()

    rows=read_csv(args.input)
    print(f" Total rows:{len(rows)}")
    for row in rows[:3]:
        print(row)

if __name__=="__main__":
    main()
             