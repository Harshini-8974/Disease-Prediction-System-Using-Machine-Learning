from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import pandas as pd

l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']
l2 = [0] * len(l1)

# TESTING DATA
tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3,
                          'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9, 'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28,
                          'Heart attack': 29, 'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37,
                          'Urinary tract infection': 38, 'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)

X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df = pd.read_csv("Training.csv")

df.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3,
                           'Drug Reaction': 4,
                           'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                           'Bronchial Asthma': 9, 'Hypertension ': 10,
                           'Migraine': 11, 'Cervical spondylosis': 12,
                           'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                           'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                           'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                           'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                           'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28,
                           'Heart attack': 29, 'Varicose veins': 30, 'Hypothyroidism': 31,
                           'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                           '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37,
                           'Urinary tract infection': 38, 'Psoriasis': 39,
                           'Impetigo': 40}}, inplace=True)

X = df[l1]

y = df[["prognosis"]]
np.ravel(y)


def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb = gnb.fit(X, np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if disease[predicted] == disease[a]:
            h = 'yes'
            break

    if (h == 'yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")


# Create Tkinter GUI
root = Tk()
root.title("Disease Prediction From Symptoms")



# Load the image
image = Image.open("hospital.webp")

# Resize the image
image = image.resize((1200, 800), Image.BICUBIC)

# Decrease transparency by applying an alpha mask
alpha = 128  # Adjust alpha value as needed
mask = Image.new("L", image.size, alpha)
image.putalpha(mask)

# Convert the image to a PhotoImage object
background_image = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


# Styling
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground="white", background="#20B2AA", borderwidth=0)

# Labels
w2 = Label(root, justify=LEFT, text="Disease Prediction From Symptoms", bg="#6495ED", fg="white",
           font=("Elephant", 30))
w2.place(relx=0.5, rely=0.05, anchor="center")

Label(root, text="Symptom 1", bg="#6495ED", fg="white", font=("Helvetica", 12, "bold")).place(relx=0.1, rely=0.2,
                                                                                               anchor="center")
Label(root, text="Symptom 2", bg="#6495ED", fg="white", font=("Helvetica", 12, "bold")).place(relx=0.1, rely=0.3,
                                                                                               anchor="center")
Label(root, text="Symptom 3", bg="#6495ED", fg="white", font=("Helvetica", 12, "bold")).place(relx=0.1, rely=0.4,
                                                                                               anchor="center")
Label(root, text="Symptom 4", bg="#6495ED", fg="white", font=("Helvetica", 12, "bold")).place(relx=0.1, rely=0.5,
                                                                                               anchor="center")
Label(root, text="Symptom 5", bg="#6495ED", fg="white", font=("Helvetica", 12, "bold")).place(relx=0.1, rely=0.6,
                                                                                               anchor="center")

# Dropdowns for symptoms
Symptom1 = ttk.Combobox(root, values=l1)
Symptom1.place(relx=0.3, rely=0.2, anchor="center")

Symptom2 = ttk.Combobox(root, values=l1)
Symptom2.place(relx=0.3, rely=0.3, anchor="center")

Symptom3 = ttk.Combobox(root, values=l1)
Symptom3.place(relx=0.3, rely=0.4, anchor="center")

Symptom4 = ttk.Combobox(root, values=l1)
Symptom4.place(relx=0.3, rely=0.5, anchor="center")

Symptom5 = ttk.Combobox(root, values=l1)
Symptom5.place(relx=0.3, rely=0.6, anchor="center")

# Button to predict
predict_button = Button(root, text="Predict", command=NaiveBayes, padx=10, pady=5, bg="#FFD700", fg="black",
                        font=("Helvetica", 12, "bold"), relief="flat")
predict_button.place(relx=0.5, rely=0.7, anchor="center")

# Display predicted disease
Label(root, text="Predicted Disease", bg="#6495ED", fg="white", font=("Helvetica", 12, "bold")).place(relx=0.5,
                                                                                                        rely=0.8,
                                                                                                        anchor="center")
t3 = Text(root, height=2, width=30, bg="#ADD8E6", fg="black", font=("Helvetica", 12))
t3.place(relx=0.5, rely=0.85, anchor="center")

root.mainloop()
