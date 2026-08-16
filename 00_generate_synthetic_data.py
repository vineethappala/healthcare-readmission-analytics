import os
import numpy as np
import pandas as pd

# ============================================================
# 1. PROJECT CONFIGURATION
# ============================================================

np.random.seed(42)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(RAW_DATA_DIR, exist_ok=True)

START_DATE = pd.Timestamp("2024-01-01")
END_DATE = pd.Timestamp("2025-12-31")

NUM_PATIENTS = 2500
NUM_ENCOUNTERS = 5000


# ============================================================
# 2. DIAGNOSIS REFERENCE DATA
# ============================================================

diagnoses = pd.DataFrame({
    "diagnosis_code": [
        "D001", "D002", "D003", "D004",
        "D005", "D006", "D007", "D008",
        "D009", "D010", "D011", "D012"
    ],
    "diagnosis_name": [
        "Diabetes",
        "Heart Failure",
        "COPD",
        "Pneumonia",
        "Hypertension",
        "Asthma",
        "Coronary Artery Disease",
        "Kidney Disease",
        "Infection",
        "Stroke",
        "Gastrointestinal Disorder",
        "Other"
    ],
    "diagnosis_category": [
        "Chronic",
        "Cardiovascular",
        "Respiratory",
        "Respiratory",
        "Chronic",
        "Respiratory",
        "Cardiovascular",
        "Renal",
        "Infectious",
        "Neurological",
        "Gastrointestinal",
        "Other"
    ]
})


# ============================================================
# 3. PATIENT DATA
# ============================================================

patient_ids = [
    f"P{i:05d}"
    for i in range(1, NUM_PATIENTS + 1)
]

birth_dates = pd.to_datetime(
    np.random.randint(
        pd.Timestamp("1940-01-01").value // 10**9,
        pd.Timestamp("2006-12-31").value // 10**9,
        NUM_PATIENTS
    ),
    unit="s"
)

patients = pd.DataFrame({
    "patient_id": patient_ids,
    "date_of_birth": birth_dates,
    "gender": np.random.choice(
        ["Female", "Male"],
        size=NUM_PATIENTS,
        p=[0.52, 0.48]
    ),
    "race": np.random.choice(
        [
            "White",
            "Black",
            "Hispanic",
            "Asian",
            "Other"
        ],
        size=NUM_PATIENTS,
        p=[0.42, 0.20, 0.18, 0.10, 0.10]
    ),
    "insurance_type": np.random.choice(
        [
            "Commercial",
            "Medicare",
            "Medicaid",
            "Self-Pay"
        ],
        size=NUM_PATIENTS,
        p=[0.42, 0.35, 0.18, 0.05]
    ),
    "zip_code": np.random.choice(
        [
            "60440",
            "60441",
            "60446",
            "60450",
            "60453",
            "60477"
        ],
        size=NUM_PATIENTS
    )
})


# ============================================================
# 4. ENCOUNTER DATA
# ============================================================

encounter_ids = [
    f"E{i:06d}"
    for i in range(1, NUM_ENCOUNTERS + 1)
]

encounter_patient_ids = np.random.choice(
    patient_ids,
    size=NUM_ENCOUNTERS,
    replace=True
)

admission_dates = pd.to_datetime(
    np.random.randint(
        START_DATE.value // 10**9,
        END_DATE.value // 10**9,
        NUM_ENCOUNTERS
    ),
    unit="s"
)

admission_types = np.random.choice(
    ["Emergency", "Elective", "Urgent"],
    size=NUM_ENCOUNTERS,
    p=[0.55, 0.25, 0.20]
)

departments = np.random.choice(
    [
        "Emergency",
        "Cardiology",
        "Internal Medicine",
        "Pulmonology",
        "Neurology",
        "Orthopedics",
        "General Surgery"
    ],
    size=NUM_ENCOUNTERS,
    p=[0.28, 0.14, 0.20, 0.10, 0.08, 0.08, 0.12]
)

diagnosis_codes = np.random.choice(
    diagnoses["diagnosis_code"],
    size=NUM_ENCOUNTERS
)

length_of_stay = np.random.choice(
    [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15],
    size=NUM_ENCOUNTERS,
    p=[
        0.12, 0.15, 0.15, 0.14, 0.12,
        0.09, 0.07, 0.05, 0.04, 0.04, 0.03
    ]
)

discharge_dates = admission_dates + pd.to_timedelta(
    length_of_stay,
    unit="D"
)

total_charges = np.round(
    np.random.lognormal(
        mean=8.5,
        sigma=0.7,
        size=NUM_ENCOUNTERS
    ),
    2
)

discharge_disposition = np.random.choice(
    [
        "Home",
        "Home with Follow-Up",
        "Skilled Nursing Facility",
        "Transfer"
    ],
    size=NUM_ENCOUNTERS,
    p=[0.58, 0.25, 0.10, 0.07]
)

encounters = pd.DataFrame({
    "encounter_id": encounter_ids,
    "patient_id": encounter_patient_ids,
    "admission_date": admission_dates,
    "discharge_date": discharge_dates,
    "admission_type": admission_types,
    "department": departments,
    "diagnosis_code": diagnosis_codes,
    "length_of_stay": length_of_stay,
    "total_charges": total_charges,
    "discharge_disposition": discharge_disposition
})


# ============================================================
# 5. SORT ENCOUNTERS FOR READMISSION ANALYSIS
# ============================================================

encounters = encounters.sort_values(
    ["patient_id", "admission_date"]
).reset_index(drop=True)


# ============================================================
# 6. DERIVE 30-DAY READMISSION
# ============================================================

encounters["next_admission_date"] = (
    encounters.groupby("patient_id")["admission_date"]
    .shift(-1)
)

days_to_next_encounter = (
    encounters["next_admission_date"]
    - encounters["discharge_date"]
).dt.days

encounters["readmitted_30_days"] = np.where(
    (days_to_next_encounter >= 0)
    & (days_to_next_encounter <= 30),
    "Yes",
    "No"
)

encounters = encounters.drop(
    columns=["next_admission_date"]
)


# ============================================================
# 7. FOLLOW-UP DATA
# ============================================================

follow_up_rows = []

follow_up_counter = 1

for _, encounter in encounters.iterrows():

    # Higher likelihood of documented follow-up
    # for encounters discharged with follow-up instructions.
    if encounter["discharge_disposition"] == "Home with Follow-Up":
        follow_up_probability = 0.75
    else:
        follow_up_probability = 0.35

    has_follow_up = np.random.random() < follow_up_probability

    if has_follow_up:

        follow_up_date = (
            encounter["discharge_date"]
            + pd.Timedelta(
                days=int(np.random.randint(3, 31))
            )
        )

        follow_up_type = np.random.choice(
            [
                "Primary Care",
                "Specialist",
                "Telehealth"
            ],
            p=[0.50, 0.35, 0.15]
        )

        completed = np.random.choice(
            ["Yes", "No"],
            p=[0.85, 0.15]
        )

        follow_up_rows.append({
            "follow_up_id": f"F{follow_up_counter:06d}",
            "encounter_id": encounter["encounter_id"],
            "follow_up_date": follow_up_date,
            "follow_up_type": follow_up_type,
            "completed": completed
        })

        follow_up_counter += 1


follow_ups = pd.DataFrame(follow_up_rows)


# ============================================================
# 8. ADD SMALL DOCUMENTED DATA-QUALITY SCENARIOS
# ============================================================

# Missing demographic values
missing_patient_indexes = np.random.choice(
    patients.index,
    size=20,
    replace=False
)

patients.loc[
    missing_patient_indexes,
    "race"
] = np.nan


# Missing follow-up completion values
if len(follow_ups) > 0:

    missing_followup_indexes = np.random.choice(
        follow_ups.index,
        size=min(15, len(follow_ups)),
        replace=False
    )

    follow_ups.loc[
        missing_followup_indexes,
        "completed"
    ] = np.nan


# ============================================================
# 9. EXPORT CSV FILES
# ============================================================

patients.to_csv(
    os.path.join(RAW_DATA_DIR, "patients.csv"),
    index=False
)

diagnoses.to_csv(
    os.path.join(RAW_DATA_DIR, "diagnoses.csv"),
    index=False
)

encounters.to_csv(
    os.path.join(RAW_DATA_DIR, "encounters.csv"),
    index=False
)

follow_ups.to_csv(
    os.path.join(RAW_DATA_DIR, "follow_ups.csv"),
    index=False
)


# ============================================================
# 10. GENERATION SUMMARY
# ============================================================

print("\nSynthetic healthcare dataset generated successfully.\n")

print(f"Patients:   {len(patients):,}")
print(f"Encounters: {len(encounters):,}")
print(f"Diagnoses:  {len(diagnoses):,}")
print(f"Follow-ups: {len(follow_ups):,}")

print("\nReadmission distribution:")
print(
    encounters["readmitted_30_days"]
    .value_counts()
)

print("\nFiles created in:")
print(RAW_DATA_DIR)