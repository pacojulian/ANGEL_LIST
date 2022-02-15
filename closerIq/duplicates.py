import argparse
import pandas as pd
parser = argparse.ArgumentParser(description = '')
 
parser.add_argument("-f", "--file", help = "File to read to find duplicate")
 
args = parser.parse_args()
 
def read_file(): 
    df = pd.read_csv (args.file)
    output = df.name.str.replace('[^a-zA-Z]','',regex=True)
    return output.sort_values()
def write_to_file(key,val):
    with open("duplicates.txt", "a") as file:
        file.write(f"{key}-{val} \n")

def find_duplicate(values):
    stack = []
    for  val in values:
        if(len(stack) == 0):
            stack.append(val)
            pass
        if(stack[-1] in val):
            print("Find Duplicate: ", val)
            write_to_file(stack[-1],val)
        else:
            stack.append(val)
        
def main():
    print('Reading file', args.file)
    values_flatten = read_file().values.tolist()
    find_duplicate(values_flatten)

if __name__ == "__main__":
    main()
