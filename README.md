# Generic Real Estate Consulting Project

Hello Everyone, 
We are group 29.

## VISUALISATION

We have also done some feature analysis using visualising both internal and external data, which can be recreted using the `visualisation.ipynb` file under the `notebooks` section.

## API

To get the distance to CBD, please run `distance_to_cbd.ipynb`file under the `notebooks` section.

To get the distance to train stations, please run `distance_to_train_station.ipynb`file under the `notebooks` section.

#  How to run the script

##  rental_growth_predictions

(1) download and save all the webpages from realestate website manually, and put them into pages folder.
There are about 300 webpages that I have downloaded, I only upload 6 webpages to github. Otherwise, put 300 webpages will be too big, about 200 MB.

(2) run scrapy.py, we will get a file, named "m.csv", it is a list about house information.

(3) run school_distance.py, we will get a "school.txt", it is a list about the distance between house to nearest school, hospital

(4) run merge.py, it will merge "m.csv" and "school.txt" together, we will get a "merge.csv". We rename it as "house_renting.csv".


##  population_prediction

(1) run "save_page_into_local.py", it will read the links in "suburb_link.txt", and download all the webpages into a folder: "pages"

(2) run "extract_population_from_local.py", it will extract population, postcode and suburb name into "subub_population.csv"

##  scrapy_suburb_rent

(1) copy the "pages" folder in 2.2 into this folder. We will extract the data from this folder.

(2) run "extract_renting_growth.py", it will extract the renting information into "renting_growth.csv"