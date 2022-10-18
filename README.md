# Generic Real Estate Consulting Project

Hello Everyone, 
We are group 29.

## README
**Research Goal:**
- predict rental prices for both residential properties and apartments throughout Victoria, Australia. 
- investigate the role of both internal and external variables on rental prices, and recommend where they are most likely to increase.
- determine the appropriate level of rent an online real estate company should be listing their properties
- determine which properties are most likely to increase in the next five years.


**Requirements:** 

Please see requirements.txt and requirements_2.txt to install packages required to run the pipeline



To run the pipeline, please visit the `notebooks` directory and run the files in order:


1. `internal_dataset_scraping.ipynb`: This notebook downloads the raw data into the `data/raw` directory.
2. `internal_dataset_preprocessing.ipynb`: This notebook details all preprocessing steps and outputs it to the `data/curated` directory.
3. `distance_to_cbd.ipynb`: This notebook retrieves the from each property to the CBD
4. `distance_to_train_station.ipynb`: This notebook retrieves the from each property to closest train station
5. `feature_analysis.ipynb`: This notebook is used to conduct analysis on the curated data and build a statistical model to explain relationships between the input and response variables 

Then visit the `scripts` directory and run the files in order: 

from the house_renting_scrapy folder 

1. scrapy the webpages of realstate into "pages" folder
2. run scrapy.py, we will get a file, named "m.csv", it is a list about house information.
3. run school_distance.py, we will get a "school.txt", it is a list about the distance between house to nearest school, hospital
4. run merge.py, it will merge "m.csv" and "school.txt" together, we will get a "merge.csv". We rename it as "house_renting.csv". 

from the scrapy_population folder 

1. `save_page_into_local.py`: this script reads the links in "suburb_link.txt", and downloads all the webpages into a folder: "pages" automatically.
2. `extract_population_from_local.py`: this script extracts population, postcode and suburb name into "suburb_population.csv"

 from the scrapy_suburb_rent folder

3. copy the "pages" folder in above into this folder. We will extract the another group of data from this folder.
4. `extract_renting_growth.py`: this script extracts the renting information into "renting_growth.csv"

Then visit the `notebooks` directory and run the files in order: 

6. `summary_notebook.ipynb`: This notebook is used to conduct analysis on the curated data.
7. `visualisation_maps.ipynb`: This notebook is used to create maps based on analysis for further visual insights.

