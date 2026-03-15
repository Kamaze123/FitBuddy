import numpy as np
import tensorflow as tf
import pickle
import json
import random
import re

# Load trained model
model = tf.keras.models.load_model("model/chatbot_model.keras")

# Load vectorizer and label encoder
with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

#Load intents
with open("data/intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)


user_states = {}
user_data = {}

#Intent prediction
def predict_intent(text):
    X = vectorizer.transform([text]).toarray()
    prediction = model.predict(X, verbose = 0)
    tag_index = np.argmax(prediction)
    tag = label_encoder.inverse_transform([tag_index])[0]
    confidence = np.max(prediction)
    return tag, confidence

#Response from intent prediction
def get_response(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "Sorry, I don't understand."

#BMI function
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

#Calorie function
def calculate_calories(weight, height, age):
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    return round(bmr)

def get_bot_response(user_input, user_id="default"):

    state = user_states.get(user_id)

    #BMI flow
    if state == "bmi_height":

        user_data[user_id] = {"height": float(user_input)}
        user_states[user_id] = "bmi_weight"
        return "Enter your weight in kg"

    if state == "bmi_weight":

        user_data[user_id]["weight"] = float(user_input)

        height = user_data[user_id]["height"]
        weight = user_data[user_id]["weight"]

        bmi = calculate_bmi(height, weight)

        user_states[user_id] = None

        return f"Your BMI is {bmi}"


    #Calorie flow
    if state == "calorie_weight":

        user_data[user_id] = {"weight": float(user_input)}
        user_states[user_id] = "calorie_height"

        return "Enter your height in cm"

    if state == "calorie_height":

        user_data[user_id]["height"] = float(user_input)
        user_states[user_id] = "calorie_age"

        return "Enter your age"

    if state == "calorie_age":

        user_data[user_id]["age"] = int(user_input)
        
        data = user_data[user_id]

        calories = calculate_calories(
            data["weight"],
            data["height"],
            data["age"]
        )

        user_states[user_id] = None

        return f"Your estimated daily calorie requirement is {calories} kcal"

    #Normal intent
    tag, confidence = predict_intent(user_input)

    if confidence < 0.5:
        return "I'm not sure I understand that. Here's what I can help you with:\n\n- Weight loss & fat burning\n- Muscle gain & bulking\n- Gym & home workout plans\n- Nutrition & protein sources\n- BMI & calorie calculation\n- Supplement advice\n\nJust ask me anything!"

    if tag == "bmi_calculation":
        user_states[user_id] = "bmi_height"
        return "Sure! What is your height in cm?"

    if tag == "calorie_calculation":
        user_states[user_id] = "calorie_weight"
        return "Let's calculate your calories. Enter your weight in kg"

    return get_response(tag)

