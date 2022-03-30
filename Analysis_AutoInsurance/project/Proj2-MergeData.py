"""


import os
import glob
import pandas as pd
os.chdir("/Users/sethhowells/Desktop/MSDS/FALL 21/DataViz/WEEK 2/Tokyodatasets/csv")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
"""

# importing libraries
import pandas as pd
import glob
import os
  
# merging the files
joined_files = os.path.join("/Users/sethhowells/Desktop/MSDS/FALL 21/DataViz/WEEK 2/Tokyodatasets/csv", "*.csv")
  
# A list of all joined files is returned
joined_list = glob.glob(joined_files)
  
# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)
