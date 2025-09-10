# Google Geocode Scraper

This project automates the process of converting coordinates into addresses by interacting with the Google Geocode API Playground.  
It was built to handle large datasets (15k+ points) and demonstrates how to manage bulk geocoding tasks programmatically.

## How it works
- Prepare an `Input.xlsx` file containing a list of coordinates.  
- Run the script, and it will output the corresponding addresses into a results file.  
- A **save-state function** is included to allow resuming if the process is interrupted.  

## Why I built this
I built this as a **proof of concept to avoid incurring API costs while experimenting with large-scale geocoding**.  
I specifically needed **Google’s exact address matches**, so alternative free APIs (like OpenStreetMap) were not suitable for this project.
This project showcases:  
- Handling large input datasets  
- Automating API interactions  
- Adding fault-tolerance with save states  

## Limitations
- The scraping method is not 100% reliable, and occasional crashes may occur but the save state prevents having to start over every time it happens.  
- The script could become unusable due to future changes made to the playground website.  

## Usage
1. Fill `Input.xlsx` with your coordinates.
2. Install requirements - `pip install -r requirements.txt`
3. Run `main.py`.  
4. Collect the output addresses from the generated file.  

## Disclaimer
This project is intended **for learning and demonstration purposes only**.  
Please review and comply with the Google Maps Platform.  
For production use, you should obtain a proper API key from Google.  
