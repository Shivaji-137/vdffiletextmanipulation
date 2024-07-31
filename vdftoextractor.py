"""
Written by Shivaji Chaulagain for text modification/manipulation of the .vdf file obtained from vedas software for bachelor thesis. For further enquiries, contact us.
"""
import re
import sys
import pandas as pd

class VDFExtract:
    def __init__(self, file_path, lim):
        self.filename = file_path
        self.pattern1 = r'(s\d+)\s+(-?\d+)'  # pattern search for "726.97   12.10  1627.57   s25 -22   s54 14   s82 10"
        self.pattern2 = r"^s\s\s?\d+\s+\w+\s+\w+"  # pattern search "for s  1   STRE NH   f3650 100"
        self.lim = int(lim)  # Convert limit to integer

    def readfile(self):
        first_pairs = []
        second_pairs = []
        with open(self.filename, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                matches = re.findall(self.pattern1, line)
                match2 = re.findall(self.pattern2, line)
                if matches:
                    first_pairs.append(matches)
                if match2:
                    second_pairs.append(match2[0])
        return first_pairs, second_pairs

    def filter(self):
        extracted_pairs, another_pairs = self.readfile()
        print(f"number of row original data: {len(extracted_pairs)}")
        reextracted = []
        dicval = {}
        for i in extracted_pairs:
            res = ""
            for j in i:
                a, b = j
                init = a + f"({abs(int(b))})"
                if abs(int(b)) > self.lim:
                    res += " " + init
            reextracted.append(res.strip())
        
        for j in another_pairs:
            lsplit = j.split("   ", 1)
            key = "".join(lsplit[0].split())
            val = lsplit[1]
            dicval[key] = val
        return reextracted, dicval

    def modify(self, reextracted, dicval):
        keys = list(dicval.keys())
        xval = []
        for j in reextracted:
            p = j
            for k in keys:
                if k in j:
                    z = re.sub(rf"\b{k}\b", dicval.get(k), j)
                    p = z
            xval.append(p)
        return xval

if __name__ == "__main__":
    if len(sys.argv) == 4:
        symbol = ["\u03BD", "\u03B2", "\u03B4", "\u03BA"]  # unicode character for nu, beta, delta, kappa
        filename = sys.argv[1]
        limit = sys.argv[2]  # greater than 10
        savefile_path = sys.argv[3]

        try:
            vdfto = VDFExtract(filename, limit)
            first, second = vdfto.filter()
            
            modfres = vdfto.modify(first, second)
            secondmod = vdfto.modify(modfres, second)
            thirdmod = vdfto.modify(secondmod, second)
            fourthmod = vdfto.modify(thirdmod, second)
            fifthmod = vdfto.modify(fourthmod, second)  # Changed from thirdmod to fourthmod
            result = [i.replace("STRE", symbol[0]).replace("BEND", symbol[1]).replace("TORS", symbol[2]).replace("OUT", symbol[3]) for i in fifthmod]
            print(f"Number of row of final result: {len(result)}")
            pd.DataFrame(result, columns=["Assignment"]).to_csv(savefile_path, index=False)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Usage: python script.py <filename> <limit> <savefile_path>")

       
        
