# Healthcare Readmission Analytics — Data Dictionary

## Project Overview

This data dictionary documents the structure, business meaning, and analytical purpose of the synthetic healthcare datasets used in the Healthcare Readmission Analytics project.

All records are synthetically generated for portfolio and analytical demonstration purposes and do not represent real patients or real healthcare events.

---

# 1. Patients

**Table:** `patients`

**Grain:** One row per synthetic patient.

| Column | Data Type | Description |
|---|---|---|
| patient_id | String | Unique synthetic identifier assigned to each patient |
| date_of_birth | Date | Synthetic patient date of birth |
| gender | String | Synthetic gender category |
| race | String | Synthetic race/ethnicity category |
| insurance_type | String | Synthetic insurance coverage category |
| zip_code | String | Synthetic ZIP code used for geographic segmentation |

### Primary Key

`patient_id`

---

# 2. Encounters

**Table:** `encounters`

**Grain:** One row per patient encounter.

| Column | Data Type | Description |
|---|---|---|
| encounter_id | String | Unique identifier for each healthcare encounter |
| patient_id | String | Identifier linking the encounter to the patient |
| admission_date | DateTime | Date and time the encounter began |
| discharge_date | DateTime | Date and time the encounter ended |
| admission_type | String | Encounter admission classification |
| department | String | Hospital department associated with the encounter |
| diagnosis_code | String | Reference code linking the encounter to the diagnosis table |
| length_of_stay | Integer | Number of days between admission and discharge |
| total_charges | Decimal | Synthetic encounter charge amount |
| discharge_disposition | String | Synthetic disposition category following discharge |
| readmitted_30_days | String | Derived indicator identifying whether a subsequent qualifying encounter occurred within 30 days of discharge |

### Primary Key

`encounter_id`

### Foreign Keys

- `patient_id` → `patients.patient_id`
- `diagnosis_code` → `diagnoses.diagnosis_code`

---

# 3. Diagnoses

**Table:** `diagnoses`

**Grain:** One row per diagnosis reference code.

| Column | Data Type | Description |
|---|---|---|
| diagnosis_code | String | Unique synthetic diagnosis reference code |
| diagnosis_name | String | Synthetic diagnosis name used for analytical grouping |
| diagnosis_category | String | Higher-level diagnosis category |

### Primary Key

`diagnosis_code`

---

# 4. Follow-Ups

**Table:** `follow_ups`

**Grain:** One row per documented follow-up event.

| Column | Data Type | Description |
|---|---|---|
| follow_up_id | String | Unique identifier for the follow-up record |
| encounter_id | String | Identifier linking the follow-up to the originating encounter |
| follow_up_date | DateTime | Date and time of the documented follow-up |
| follow_up_type | String | Type of follow-up interaction |
| completed | String | Indicates whether the documented follow-up was completed |

### Primary Key

`follow_up_id`

### Foreign Key

`encounter_id` → `encounters.encounter_id`

---

# 5. Key Analytical Definitions

## 30-Day Readmission

A 30-day readmission is identified when the same patient has a subsequent encounter with an admission date occurring between 0 and 30 days after the prior encounter's discharge date.

The readmission indicator is derived from encounter history rather than randomly assigned.

## Length of Stay

Length of stay represents the number of days between the encounter admission and discharge dates.

## Follow-Up Completion

Follow-up completion indicates whether a documented post-discharge follow-up event was completed.

---

# 6. Data Quality Considerations

The synthetic dataset intentionally contains a small number of data-quality scenarios for analytical validation:

- 20 patient records contain missing race values.
- 15 follow-up records contain missing completion values.
- Primary identifiers were validated for uniqueness.
- Foreign-key relationships were validated between patients, encounters, diagnoses, and follow-ups.

These scenarios are included to demonstrate data-quality assessment and should not be interpreted as characteristics of real healthcare data.
