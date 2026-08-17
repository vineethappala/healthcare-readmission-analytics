# Healthcare Readmission Analytics

## Project Overview

This project demonstrates an end-to-end healthcare data analytics
workflow using synthetic patient, encounter, diagnosis, and follow-up
data.

The objective is to analyze 30-day hospital readmission patterns and
produce reusable healthcare KPIs for reporting and dashboarding.

## Business Objective

Healthcare organizations monitor readmissions because they can indicate
opportunities to improve discharge planning, follow-up coordination,
and patient care processes.

This project answers questions such as:

- What is the overall 30-day readmission rate?
- Which departments have higher observed readmission rates?
- How do readmission rates vary by diagnosis category?
- How do readmission rates vary by insurance type?
- How does documented follow-up status relate to readmission?
- How does readmission change over time?
- How does length of stay vary across readmission groups?

## Dataset

The project uses synthetic healthcare data generated with Python.

Dataset size:

- 2,500 patients
- 5,000 encounters
- 12 diagnosis codes
- 2,226 follow-up records
- 2024–2025 encounter period

No real patient information is used.

## Technology Stack

- Python
- Pandas
- DuckDB
- SQL
- CSV
- GitHub
- Power BI

## Project Architecture

```text
Synthetic Data
      |
      v
Data Profiling
      |
      v
Data Quality Validation
      |
      v
Analytics Data Model
      |
      v
KPI Layer
      |
      v
Processed Analytics Data
      |
      v
Power BI Dashboard
