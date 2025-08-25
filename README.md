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
With Docker installed and running, build the Docker image with the following command

<br>

```
docker build -t churn-app .
```

<br>

And run it

<br>

```
docker run -p 8501 churn-app
```

## Introduction

This repository was made to build a classifier that predicts Churn rates and displays data using the streamlit web framework.

<br/>

The data was collected from [this database](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis) and it was cleaned and resampled to have a better representation of the minority class.
After that, I built a RF Classifier that predicted Churn with 89,3% precision in the validation set. The data was displayed in an app with Streamlit. 

<br/>


## Results

**Images of the application that can be acessed with [this link](https://churn-dash.streamlit.app/).**

![](https://github.com/isaiapedro/churn-prediction/blob/main/assets/homepage.png)

<br>
<br>

![](https://github.com/isaiapedro/churn-prediction/blob/main/assets/prediction.png)

## Conclusion

Thanks for reading up until here. I had a ton of fun doing this notebook and got a lot of useful insights on Unbalanced data and how to work with Streamlit applications.

If you want to see more Kaggle solutions, see the Flower Classification Problem or go to my github page. Feel free to reach me on [LinkedIn](https://www.linkedin.com/in/isaiapedro/) or my [Webpage](https://github.com/isaiapedro/Portfolio-Website).

Bye! 👋
