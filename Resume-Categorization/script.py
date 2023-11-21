import pickle, sys, os
import pandas as pd
import pdfplumber
import  string
from nltk.corpus import stopwords
import shutil , csv

stop_words = set(stopwords.words('english'))
mode_path = 'C:/Users/gazur/Desktop/Polyfins_Intern-2023/Task_data/model/LGBMM.pkl'
tfidf_model ="C:/Users/gazur/Desktop/Polyfins_Intern-2023/Task_data/model/tfidf_models.pkl"


def TakeInput():
    if len(sys.argv) != 2:
        print("Usage: python script.py <pdf_file_path>")
        return
    pdf_file_path = sys.argv[1]
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            text_content = ""
            for page in pdf.pages:
                text_content += page.extract_text()
            return text_content

    except FileNotFoundError:
        print("Pdf File Not Found", pdf_file_path)
    except Exception as e:
        print("An error Occurred :", e)


def preProcess(text):
    clean_text = [char for char in text if char not in string.punctuation]
    clean_text = ''.join(clean_text)
    clean_text = [word for word in clean_text.split() if word.lower() not in stopwords.words('english')]
    clean_text = ' '.join(clean_text)
    return clean_text


def remove_words(text, words_to_remove):
    for word in words_to_remove:
        text = text.replace(word, '')
    return text.strip()


words_to_remove = ['NUMBER', 'State', 'City', 'Name', 'Company']

df2 = [TakeInput()]
df4 = pd.DataFrame(df2, columns=['Data'])
df4['clean_text'] = df4['Data'].apply(lambda w: preProcess(w))
df4['finale_text'] = df4['clean_text'].apply(lambda text: remove_words(text, words_to_remove))


with open(tfidf_model, "rb") as pkl_file:
    loaded_tfidf_model = pickle.load(pkl_file)

ff=loaded_tfidf_model.transform(df4['finale_text'].values)


if os.path.exists(mode_path):
    with open(mode_path, 'rb') as file:
        lgbm = pickle.load(file)
else:
    print(f"File '{mode_path}' not found.")

preds = lgbm.predict(ff)

output_rows = []
for idx, pred in enumerate(preds):
    output_folder = os.path.join(os.path.dirname(sys.argv[1]), pred)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    pdf_filename = os.path.basename(sys.argv[1])
    output_pdf_path = os.path.join(output_folder, pdf_filename)
    shutil.copy(sys.argv[1], output_pdf_path)
    print(f"PDF saved in folder '{output_folder}'.")
    output_rows.append([pdf_filename, pred])

pdf_directory = os.path.dirname(sys.argv[1])
csv_file = os.path.join(pdf_directory , 'categorized_resumes.csv')
csv_header = ['filename', 'category']
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output_rows)
print(f"CSV file '{csv_file}' created and updated successfully.")




