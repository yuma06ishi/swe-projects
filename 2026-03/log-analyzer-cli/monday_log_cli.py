#monday

import argparse

def read_lines(path):
    with open(path,"r",encoding="utf-8") as f:
        return f.readlines()
    
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--keyword", default="")
    p.add_argument("--out")

    args=p.parse_args()

    lines=read_lines(args.input)
    print(len(lines))

if __name__ =="__main__":
    main()
