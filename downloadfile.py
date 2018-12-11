import urllib.request
import shutil


import os

directory="c://srinivas//PythonWorkspace//500002"
if not os.path.exists(directory):
    os.makedirs(directory)
	
	
url = "https://beta.bseindia.com/bseplus/AnnualReport/500002/5000021210.pdf"
output_file = directory + "//5000021210.pdf"
with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
     shutil.copyfileobj(response, out_file)