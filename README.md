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

Please see requirements.txt to install packages required to run the pipeline



To run the pipeline, please visit the `notebooks` directory and run the files in order:


1. `internal_dataset_scraping.ipynb`: This notebook downloads the raw data into the `data/raw` directory.
2. `internal_dataset_preprocessing.ipynb`: This notebook details all preprocessing steps and outputs it to the `data/curated` directory.
3. `distance_to_cbd.ipynb`: This notebook retrieves the from each property to the CBD
4. `distance_to_train_station.ipynb`: This notebook retrieves the from each property to closest train station
5. `feature_analysis.ipynb`: This notebook is used to conduct analysis on the curated data and build a statistical model to explain relationships between the input and response variables 

Then visit the `scripts` directory and run the files in order: 

from the population_growth_predictions file 

1. `save_page_into_local.py`: this script reads the links in "surburb_link.txt", and downloads all the webpages into a folder: "pages"
2. `extract_population_from_local.py`: thi script extracts population, postcode and surburb name into "surburb_population.csv"

 from the rental_growth_predictions

3. copy the "pages" folder in 2.2 into this folder. We will extract the data from this folder.
4. `extract_renting_growth.py`: this script extracts the renting information into "renting_growth.csv"

Then visit the `notebooks` directory and run the files in order: 
6. `summary_notebook.ipynb`: This notebook is used to conduct analysis on the curated data.
7. `visualisation_maps.ipynb`: This notebook is used to create maps based on analysis.
