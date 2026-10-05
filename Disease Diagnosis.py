# Rule-Based Expert System for Disease Diagnosis

def diagnose(symptoms):
    symptoms = set(symptoms)

    # Rule 1: Flu
    if {"fever", "cough", "body pain", "fatigue"}.issubset(symptoms):
        return "Possible Diagnosis: Flu"

    # Rule 2: Common Cold
    elif {"cough", "sneezing", "runny nose"}.issubset(symptoms):
        return "Possible Diagnosis: Common Cold"

    # Rule 3: COVID-19
    elif {"fever", "cough", "loss of taste"}.issubset(symptoms):
        return "Possible Diagnosis: COVID-19"

    # Rule 4: Migraine
    elif {"headache", "nausea", "sensitivity to light"}.issubset(symptoms):
        return "Possible Diagnosis: Migraine"

    # Rule 5: Food Poisoning
    elif {"stomach pain", "vomiting", "diarrhea"}.issubset(symptoms):
        return "Possible Diagnosis: Food Poisoning"

    # Rule 6: No matching rule
    else:
        return "No specific diagnosis found. Please consult a doctor."


# Main program
print("====================================")
print("  RULE-BASED EXPERT SYSTEM")
print("      Disease Diagnosis")
print("====================================")

print("\nAvailable symptoms:")
print("fever")
print("cough")
print("body pain")
print("fatigue")
print("sneezing")
print("runny nose")
print("loss of taste")
print("headache")
print("nausea")
print("sensitivity to light")
print("stomach pain")
print("vomiting")
print("diarrhea")

# Take symptoms from user
input_symptoms = input("\nEnter your symptoms separated by comma: ")

# Convert input into a list
symptoms = [s.strip().lower() for s in input_symptoms.split(",")]

# Run inference
result = diagnose(symptoms)

# Display result
print("\n------------------------------------")
print(result)
print("------------------------------------")
