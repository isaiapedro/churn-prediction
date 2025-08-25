# Base Python image
FROM python:3

WORKDIR /churn-prediction

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy only necessary files
COPY Dashboard.py /churn-prediction/

# Expose default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "Dashboard.py", "--server.port=8501", "--server.enableCORS=false"]