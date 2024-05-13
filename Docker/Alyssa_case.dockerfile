FROM python:3.11.7

WORKDIR /app

RUN pip install numpy
RUN pip install joblib
RUN pip install flask
RUN pip install jsonify
RUN pip install scikit-learn

COPY Alyssa_website.py .
COPY templates/index.html templates/
COPY Scaler/scaler_*.joblib Scaler/
COPY Model/model_*.joblib Model/

EXPOSE 8080

CMD ["python3", "Alyssa_website.py"]
