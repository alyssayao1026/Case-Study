# Case-Study
## Introduction
This project focuses on predicting the air pollution index using Machine Learning and Deep Learning models. It includes a website interface for end-users to perform predictions. Additionally, Docker is used for containerisation. For an in-depth report, please refer to the Alyssa_Case_Report.pdf.
## Dependencies

This project relies on the following packages:

- **scipy**: Version 1.11.4
- **Scikit-learn**: Version 1.2.2
- **Flask**: Version 2.2.5
- **Pandas**: Version 2.2.1
- **NumPy**: Version 1.26.4
- **Matplotlib**: Version 3.8.0
- **seaborn**: Version 0.12.2
- **warnings**: Version 3.4.3
- **statsmodels**: Version 0.14.0
- **joblib**: Version 1.2.0

You can install these packages using pip:

```bash
pip install scipy==1.11.4 scikit-learn==1.2.2 Flask==2.2.5 pandas==2.2.1 numpy==1.26.4 matplotlib==3.8.0 seaborn==0.12.2 statsmodels==0.14.0 joblib==1.2.0
```

## Alyssa_case_study.ipynb
This file primarily focuses on data preprocessing, model fitting, and model selection.  
Comments coule be ignored as a more detailed version is provided in the report.  
From this file, we stored the selected best models and the scaler used for standardisation, which will be used for building the subsequent website.  
Additionally, for the part of reading the CSV file, 
```bash
df_raw = pd.read_csv('/Users/alyssa/Desktop/case.study/AirQualityUCI.csv')
```
please download AirQualityUCI.csv and change the path to your own.

## Docker
Please download the entire "Docker" folder and and refrain from moving the files inside unless you are able to modify the file paths for reading. 
Please also ensure you have downloaded Docker on your device.
## Website
After downloading the Docker folder, you can use it to create an image yourself. Alternatively, you can visit Docker Hub, where I have uploaded the image at the following URL: https://hub.docker.com/repository/docker/alyssayao/predict/  
Here are the steps to use it via Docker Hub:
- **1**: Pull the image by running the following command in your terminal:
```bash
docker pull alyssayao/predict:v1.0
```
- **2**: Run the container:
```bah
docker run -d -p 8080:8080 alyssayao/predict:v1.0
```
- **3**: Access the website:
```bash
http://localhost:8080
```
