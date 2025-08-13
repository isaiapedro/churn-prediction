# Churn Predictor and Dashboard
### (Random Forest Classifier for unbalanced discrete data)

## Contents

- [How to run](#how-to-run)
- [Introduction](#introduction)
- [Data Overview](#data-overview)
- [Results](#results)
- [Conclusion](#conclusion)
  
## How to Run

<br>

**To run the ML notebook:**
With Docker installed, run Docker Desktop and the jupyter notebook image with the following command

<br>

```
docker run -it --rm -p 8888:8888 -v "${pwd}:/tf/notebooks" tensorflow/tensorflow:latest-jupyter
```

<br>


**To run Streamlit:**
Just run the following command

<br>

```
streamlit run app.py
```

## Introduction

This repository was made to build a classifier that predicts Churn rates and displays data using a simple pipeline.

<br/>

The data was collected from [this database](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis) and it was cleaned and resampled to have a better representation of the minority class.
After that, I built a RF Classifier that predicted Churn with 96,9% precision in the validation set. The data was displayed in an app with Streamlit. 

<br/>

The pipeline of the project is based on Airflow to perform scripts that collected Data from a database or API and run both the model and the Streamlit App using Docker.
The Data was collected in MySQL database to make it easy for all the applications to use, which was also containerized using Docker. The Scheme of the pipeline can be seen below.
## Data Overview



## Results



## Conclusion

Thanks for reading up until here. I had a ton of fun doing this notebook and got a lot of useful insights on Unbalanced data and how to work with Streamlit applications.

If you want to see more Kaggle solutions, see the Flower Classification Problem or go to my github page. Feel free to reach me on [LinkedIn](https://www.linkedin.com/in/isaiapedro/) or my [Webpage](https://github.com/isaiapedro/Portfolio-Website).

Bye! 👋
