import os
import pandas as pd

# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")


# ============================================================
# 2. LOAD DATA
# ============================================================

patients = pd.read_csv(
    os.path.join(RAW_DATA_DIR, "patients.csv")
)

encounters = pd.read_csv(
    os.path.join(RAW_DATA_DIR, "encounters.csv")
)

diagnoses = pd.read_csv(
    os.path.join(RAW_DATA_DIR, "diagnoses.csv")
)

follow_ups = pd.read_csv(
    os.path.join(RAW_DATA_DIR, "follow_ups.csv")
)


# ============================================================
# 3. BASIC DATA PROFILING
# ============================================================

print("=" * 60)
print("HEALTHCARE DATA PROFILING")
print("=" * 60)


print("\n--- TABLE ROW COUNTS ---")

print(f"Patients:   {len(patients):,}")
print(f"Encounters: {len(encounters):,}")
print(f"Diagnoses:  {len(diagnoses):,}")
print(f"Follow-ups: {len(follow_ups):,}")


# ============================================================
# 4. UNIQUE ID CHECKS
# ============================================================

print("\n--- UNIQUE ID CHECKS ---")

print(
    "Duplicate patient IDs:",
    patients["patient_id"].duplicated().sum()
)

print(
    "Duplicate encounter IDs:",
    encounters["encounter_id"].duplicated().sum()
)

print(
    "Duplicate diagnosis codes:",
    diagnoses["diagnosis_code"].duplicated().sum()
)

print(
    "Duplicate follow-up IDs:",
    follow_ups["follow_up_id"].duplicated().sum()
)


# ============================================================
# 5. MISSING VALUE ANALYSIS
# ============================================================

print("\n--- MISSING VALUES ---")

print("\nPatients:")
print(patients.isna().sum())

print("\nEncounters:")
print(encounters.isna().sum())

print("\nFollow-ups:")
print(follow_ups.isna().sum())


# ============================================================
# 6. ENCOUNTER DATE ANALYSIS
# ============================================================

encounters["admission_date"] = pd.to_datetime(
    encounters["admission_date"]
)

encounters["discharge_date"] = pd.to_datetime(
    encounters["discharge_date"]
)

print("\n--- ENCOUNTER DATE RANGE ---")

print(
    "Earliest admission:",
    encounters["admission_date"].min()
)

print(
    "Latest admission:",
    encounters["admission_date"].max()
)


# ============================================================
# 7. LENGTH OF STAY
# ============================================================

print("\n--- LENGTH OF STAY ---")

print(
    encounters["length_of_stay"].describe()
)


# ============================================================
# 8. CHARGE ANALYSIS
# ============================================================

print("\n--- TOTAL CHARGES ---")

print(
    encounters["total_charges"].describe()
)


# ============================================================
# 9. CATEGORICAL DISTRIBUTIONS
# ============================================================

print("\n--- ADMISSION TYPE ---")

print(
    encounters["admission_type"]
    .value_counts()
)


print("\n--- DEPARTMENT ---")

print(
    encounters["department"]
    .value_counts()
)


print("\n--- READMISSION ---")

print(
    encounters["readmitted_30_days"]
    .value_counts()
)


print("\n--- FOLLOW-UP COMPLETION ---")

print(
    follow_ups["completed"]
    .value_counts(dropna=False)
)


# ============================================================
# 10. REFERENTIAL INTEGRITY CHECKS
# ============================================================

print("\n--- REFERENTIAL INTEGRITY ---")

patient_ids = set(
    patients["patient_id"]
)

encounter_patient_ids = set(
    encounters["patient_id"]
)

invalid_patient_links = (
    encounter_patient_ids - patient_ids
)

print(
    "Encounters with invalid patient IDs:",
    len(invalid_patient_links)
)


encounter_ids = set(
    encounters["encounter_id"]
)

followup_encounter_ids = set(
    follow_ups["encounter_id"]
)

invalid_encounter_links = (
    followup_encounter_ids - encounter_ids
)

print(
    "Follow-ups with invalid encounter IDs:",
    len(invalid_encounter_links)
)


diagnosis_codes = set(
    diagnoses["diagnosis_code"]
)

encounter_diagnosis_codes = set(
    encounters["diagnosis_code"]
)

invalid_diagnosis_links = (
    encounter_diagnosis_codes - diagnosis_codes
)

print(
    "Encounters with invalid diagnosis codes:",
    len(invalid_diagnosis_links)
)


print("\n" + "=" * 60)
print("PROFILING COMPLETE")
print("=" * 60)