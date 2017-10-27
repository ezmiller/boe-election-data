# NYC Bureau of Election Data - General Elections, 2009 & 2013

CSV files containing parsed NYC Bureau of Elections data for 2009 and 2013. The BoE
data has bee parsed from the original text files which contained all election data
in distinct rows with specific start/stop columns for each piece of data.

For a description of the layout of the BoE text files, see the BoE's 
[tally-export-file-description.pdf](https://github.com/ezmiller/boe-election-data/blob/master/tally-export-file-description.pdf).

For each election year of data, there are three CSV files:
  * boe-ge-/*year*/-election-data.csv
  * boe-ge-/*year*/-candidates.csv
  * boe-ge-/*year*/-ed-totals.csv

The files contain tables that could be joined in an SQL type database. The unique
key in each is a string consisting of the first 15 columns in the BoE files: what
the BoE data description file refers to as the "Key Fields". An example would be:
`2013G952NY78`.

### boe-ge-/*year*/-election-data.csv

This file contains all the fields described in the BoE's document referenced above
*except* the fields containing candidate information (see the fields under "Candidate
Information" in the BoE document referenced above).

### boe-ge-/*year*/-ed-totals.csv

This file includes rows containing "total" results for reach Election District.
These rows were identifiable because the "Formatted District" field contained the string
"TOTAL".

### boe-ge-/*year*/-candidates.csv

This file contains the candidate data for each candidate that was on the ballot in
each Election District. In the BoE, tally export file, this information was included
in each row of data. Here it has been broken out for convience. To match candidate 
data to a particular ED result, join this data using the ID field.

