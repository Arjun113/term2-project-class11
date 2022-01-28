# AI website traffic analyzer
This project is meant to analyze raw data collected from a website that has website visiting and online shopping statistics, and model them using TensorFlow.
<br>
We have also included certain other pieces of code, such as examples for the types of cookies and User Agents that are required for the proper functioning of the program. 
<br>
Requirements for the code can be seen in `requirements.txt` 

---------------- 

To use, here are the instructions:
<br>
1. Download the source code as a ZIP from GitHub, and extract it onto your computer. Make sure to not move any of the files outside the folder, as it will cause program failure.  
2. Visit `requirements.txt` and install the required libraries and programs from the web. 
<br>
That's it! All the programs can be run and inspected. 

*********************************
The information and details of every file is as follows:
<br>
1. `mainMLModel.ipynb` is the file detailing the creation of the main ML model, as well as the process of saving it to disk and accessing it later. 
2. `Data.csv` contains the raw training data
3. `NewData.csv` contains is a file that is referenced in another code snippet, contains the headers and is intended to be used as a future data storage for the data collected. 
4. `DemoTerm2Proj access key.txt` contains the access key for our private testing account. This file is not to be modified. 
5. `devicedetector.ipynb` contains the detection routines for data input from the browser
6. `GAnalytics.py` is sample code for the integration of Google Analytics.
7. `nth-clone-249009-9888620ae7fb.json` is our private client ID. This file must not be modified under any circumstances. 
8. `specialDayTracker.py` is our supporting module for device detector in order to make it look more elegant.
9. `modelImplementor.ipynb` is a sample code for the implementation of the above generated model. 
---------

To use with your own Google Analytics ID and view:
1. Replace `nth-clone-249009-9888620ae7fb.json` with your own JSON file in the folder, or just keep both. 
2. Locate the below code in `GAnalytics.py`
<br> 
```
credentials = ServiceAccountCredentials.from_json_keyfile_name('nth-clone-249009-9888620ae7fb.json', ['https://www.googleapis.com/auth/analytics.readonly'])
```
3. Replace `nth-clone-249009-9888620ae7fb.json` with the name of your own JSON file. 
4. Locate the below code in `GAnalytics.py` 
<br>
```Python
'viewId': '217876927',  # Add View ID from GA
```
5. Replace `viewId` with your own View ID from Google Analytics 
--------
                                                               
Credit for dataset - C. Okan Sakar and Yomi Kastro

