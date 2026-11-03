# Mini Ticket Router

Routes text to one of four teams (graphics, autos, medical, politics)
using TF-IDF + Logistic Regression, served via FastAPI.

## Results
- Baseline (most frequent class): 80%
- Model accuracy: 80%

## Run it
pip install -r requirements.txt
uvicorn app:app --reload
Then open http://127.0.0.1:8000/docs

## Known limitation
The model is confident even on text unrelated to the four teams.
Tested with car, medical and graphic sentences

## Next steps
Docker, MLflow tracking, tests, cloud deployment.