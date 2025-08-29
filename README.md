# 👶 Baby Cry Classifier (AI-powered Infant Cry Detection System)

This project is an **AI-powered baby cry classification system** that detects the reason behind a baby's cry and classifies it into **five categories**:

- 🍼 Hungry  
- 💨 Burping  
- 😴 Tired  
- 🤰 Belly Pain  
- 😖 Discomfort  

The model is trained using audio features (MFCCs) extracted with **Librosa** and classified using a machine learning model.  
A simple **Flask web app** is provided for easy interaction.

## ⚙️ Features
- Classifies baby cry sounds into 5 categories.  
- Achieves high accuracy (~99% during testing).  
- Simple web-based interface using **Flask**.  
- Easy to extend with more data or categories.  

## 📂 Project Structure
baby-cry-classifier/
│── static/ 
│── templates/ 
│── uploads/
│── models/ 
│── training_and_saving_model.py
│── app.py 
│── requirements.txt 
│── README.md 


## 🔧 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/baby-cry-classifier.git
cd baby-cry-classifier

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
# On Mac/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the model
python training_and_saving_model.py

# 5. Run the Flask app
python app.py

# Now open your browser and go to:
http://127.0.0.1:5000
```


## 🖼️ Usage

Upload an audio file of a baby cry.

The system processes the sound and predicts the cry reason.

Output will be one of the following categories:

🍼 Hungry

💨 Burping

😴 Tired

🤰 Belly Pain

😖 Discomfort

## 📊 Model Details

Feature extraction: MFCCs (Mel-Frequency Cepstral Coefficients)

Libraries used: Librosa, NumPy, Scikit-learn, Flask

Accuracy: ~99% on test data

## 🚀 Future Improvements

Deploy the Flask app to cloud (Heroku, AWS, etc.).

Collect more diverse dataset for better generalization.

Add real-time cry detection through microphone input.
