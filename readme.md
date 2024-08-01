## Author: Shivaji Chaulagain 
# for text modification/manipulation of the .vdf file obtained from vedas software for bachelor thesis. For further enquiries, contact us.

Run this from your linux terminal or terminal/prompt in windows.

Pandas must be installed if not.

To install pandas, pip install pandas

Usage: 

   python  vdftoextractor.py  filename limit savefile_path
   
   filename: a full path of .vdf file. works Only for .vdf file
   
   limit: pass limit 10 or desired number i.e for greater than 10
   
   savefile_path: specify the file name you want to save (supported: csv or txt)
   
   for example:
   
         python vdftoextractor.py /home/shivaji/Downloads/freqgas.vdf 10 output.txt 


vdftoextractor.ipynb is jupyter notebook I first wrote code as a scratch

sample input is freqgas.vdf and sample output result is .csv file in output folder
