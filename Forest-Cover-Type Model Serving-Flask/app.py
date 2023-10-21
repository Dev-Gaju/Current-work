import pandas as pd
import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


def get_version_info():
    version_info = {
        "app_name": "Model Serving Demo",
        "version": "0.1"
    }
    return version_info


with open('Lgbm_model.pkl', 'rb') as file:
    top_classifier = pickle.load(file)
with open('ranforest_model.pkl', 'rb') as f:
    second_classifier = pickle.load(f)
with open('blending_model.pkl', 'rb') as ff:
    ensemble = pickle.load(ff)
with open('xgb_model.pkl', 'rb') as xg:
    xgb = pickle.load(xg)
with open('model_mlp.pkl', 'rb') as ml:
    mlp = pickle.load(ml)

df = pd.read_csv('C:/Users\gazur/Desktop/Polyfins_Intern-2023/dataset/forest-cover-type-prediction/train.csv')
df = df.drop(["Id", "Cover_Type"], axis=1)
Features = [col for col in df.columns]
sc = StandardScaler()


def feature_eng(df):
    df = df.drop(['Soil_Type15', 'Soil_Type7'], axis=1)
    Features = [col for col in df.columns]
    df['EHiElv'] = df['Horizontal_Distance_To_Roadways'] * df['Elevation']
    df['EViElv'] = df['Vertical_Distance_To_Hydrology'] * df['Elevation']
    # the compass direction that a terrain faces
    df["Aspect"][df["Aspect"] < 0] += 360
    df["Aspect"][df["Aspect"] > 359] -= 360
    # Hillshade 3D representation of a surface,
    # It's a shade of grey so all the values must lie in the range (0, 255)
    df.loc[df["Hillshade_9am"] < 0, "Hillshade_9am"] = 0
    df.loc[df["Hillshade_Noon"] < 0, "Hillshade_Noon"] = 0
    df.loc[df["Hillshade_3pm"] < 0, "Hillshade_3pm"] = 0
    df.loc[df["Hillshade_9am"] > 255, "Hillshade_9am"] = 255
    df.loc[df["Hillshade_Noon"] > 255, "Hillshade_Noon"] = 255
    df.loc[df["Hillshade_3pm"] > 255, "Hillshade_3pm"] = 255
    df['Highwater'] = (df.Vertical_Distance_To_Hydrology < 0).astype(int)
    df['EVDtH'] = df.Elevation - df.Vertical_Distance_To_Hydrology
    df['EHDtH'] = df.Elevation - df.Horizontal_Distance_To_Hydrology * 0.2
    df['Euclidean_Distance_to_Hydrolody'] = (df['Horizontal_Distance_To_Hydrology'] ** 2 + df[
        'Vertical_Distance_To_Hydrology'] ** 2) ** 0.5
    df['Manhattan_Distance_to_Hydrolody'] = df['Horizontal_Distance_To_Hydrology'] + df[
        'Vertical_Distance_To_Hydrology']
    df['Hydro_Fire_1'] = df['Horizontal_Distance_To_Hydrology'] + df['Horizontal_Distance_To_Fire_Points']
    df['Hydro_Fire_2'] = abs(df['Horizontal_Distance_To_Hydrology'] - df['Horizontal_Distance_To_Fire_Points'])
    df['Hydro_Road_1'] = abs(df['Horizontal_Distance_To_Hydrology'] + df['Horizontal_Distance_To_Roadways'])
    df['Hydro_Road_2'] = abs(df['Horizontal_Distance_To_Hydrology'] - df['Horizontal_Distance_To_Roadways'])
    df['Fire_Road_1'] = abs(df['Horizontal_Distance_To_Fire_Points'] + df['Horizontal_Distance_To_Roadways'])
    df['Fire_Road_2'] = abs(df['Horizontal_Distance_To_Fire_Points'] - df['Horizontal_Distance_To_Roadways'])
    df['Hillshade_3pm_is_zero'] = (df.Hillshade_3pm == 0).astype(int)
    df['min'] = df[Features].min(axis=1)
    df['max'] = df[Features].max(axis=1)
    df['mean'] = df[Features].mean(axis=1)
    df['std'] = df[Features].std(axis=1)
    return df


@app.route('/')
def index():
    version_info = get_version_info()
    # print(version_info)
    return render_template("index.html", version_info=version_info)


def data_process(user_input):
    values = [int(num) for num in user_input.split(',')]
    data = dict(zip(Features, values))
    a = pd.DataFrame([data])
    fe = feature_eng(a)
    return fe


@app.route('/predict1', methods=['POST'])
def predict_result():
    user_input = request.json.get('data')
    fe = data_process(user_input)
    pred_light = top_classifier.predict(fe)
    prediction = pred_light.tolist()
    return jsonify({'prediction': prediction[0]})


@app.route('/predict2', methods=['POST'])
def predict_result1():
    user_input = request.json.get('data')
    fe = data_process(user_input)
    pred_light = second_classifier.predict(fe)
    prediction = pred_light.tolist()
    return jsonify({'prediction': prediction[0]})


@app.route('/predict3', methods=['POST'])
def predict_result2():
    user_input = request.json.get('data')
    fe = data_process(user_input)
    pred_light = top_classifier.predict(fe)
    pred_mlp = mlp.predict(sc.fit_transform(fe))
    pred_xgb = xgb.predict(fe)
    pred_ra = second_classifier.predict(fe)
    meta_fe = np.column_stack((pred_mlp, pred_xgb, pred_light, pred_ra))
    blending = ensemble.predict(meta_fe)
    prediction = blending.tolist()
    return jsonify({'prediction': prediction[0]})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
