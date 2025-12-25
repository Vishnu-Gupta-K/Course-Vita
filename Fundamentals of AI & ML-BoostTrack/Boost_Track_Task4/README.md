Model Deployment using Flask

This folder contains a Flask application to deploy the trained machine learning model.

Files:
app.py
final_model.pkl
requirements.txt

Steps:
pip install -r requirements.txt
python app.py

API:
POST /predict

Prediction:
- The deployed model successfully generated predictions.
- Prediction outputs were logged with timestamps.
- This confirms that the API and monitoring logic are functioning correctly.

ouput:
The output will store in the prediction_logs.txt file with timestamps.


Folder Structure:

    ├── Final_Project_Deployment/

    │   ├── app.py

    │   ├── final_model.pkl

    │   ├── prediction_logs.txt

    │   ├── requirements.txt

    │   ├── README.md
