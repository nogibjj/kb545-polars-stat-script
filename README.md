[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## Polars Descriptive Statistics Script

This is a POC of the Python Template, showing that creating a statistic script is automated. This is for Mini-Project 3 for IDS 706 Data Engineering

Tasks Completed Include:

* Adding the proper polars version to the requirements.txt file, specifically polars version 0.19.2. Also added matplotlib
* Added a src folder that held the created script function, which reads the iris.csv (found at https://gist.github.com/netj/8836201), and returns descriptive stats on sepal_length
* Added a function that creates a graph of the average sepal length of 3 different species of Iris, and saves it as a photo. The graph is shown below
* Added a test function called test_stat.py, which runs an assert on the function to gauge if it properly works. It compares the descriptive stats values with what they should be, and verifies that an image has been created
* Edited MakeFile to properly install everything, test the code, format everything proerply, and run a linter


![graph](https://github.com/nogibjj/kb545-polars-stat-script/assets/55768636/0eaf7cdc-fbf9-442e-8b78-05fc26bff35e)
