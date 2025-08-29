# training_and_saving_model.py

import os
import librosa
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib
from tqdm import tqdm

# Define dataset paths
# Load the pre-trained model and label encoder
metadata_path = 'F:/child/child/Sounds/donateacry_corpus/run1.csv'
audio_dataset_path = 'F:/child/child/Sounds/donateacry_corpus'


# Load metadata CSV file
metadata = pd.read_csv(metadata_path)
print("Metadata loaded successfully!")

# Function to extract MFCC features
def features_extractor(file):
    audio, sample_rate = librosa.load(file, res_type='kaiser_fast')
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
    return mfccs_scaled_features

# List to store extracted features and class labels
extracted_features = []

# Iterate through the dataset and extract features
for index_num, row in tqdm(metadata.iterrows(), total=metadata.shape[0]):
    file_name = os.path.join(os.path.abspath(audio_dataset_path), 'fold' + str(row["fold"]) + '/', str(row["slice_file_name"]))
    final_class_labels = row["class"]
    
    try:
        # Extract features
        data = features_extractor(file_name)
        extracted_features.append([data, final_class_labels])
    except:
        print(f"Error processing file: {file_name}")

# Convert extracted features to a DataFrame
extracted_features_df = pd.DataFrame(extracted_features, columns=['feature', 'class'])

# Convert feature lists to NumPy arrays
X = np.array(extracted_features_df['feature'].tolist())
y = np.array(extracted_features_df['class'].tolist())

# Encode class labels
labelencoder = LabelEncoder()
y = labelencoder.fit_transform(y)

# Split dataset into 80% training & 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training Data: {X_train.shape}, Test Data: {X_test.shape}")

# Train the XGBoost Classifier
model = XGBClassifier(n_estimators=300, learning_rate=0.05, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Save the trained model and label encoder
joblib.dump(model, 'audio_classification_model_xgb.pkl')
joblib.dump(labelencoder, 'label_encoder.pkl')

print("Model training complete! ✅")
print("Model and Label Encoder have been saved.")

# Predict on test set (optional, to check accuracy)
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.2f}")

