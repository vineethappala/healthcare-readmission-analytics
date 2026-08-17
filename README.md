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
```

## Repository Structure

```text
healthcare-readmission-analytics/
│
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── documentation/
│   └── data_model.md
│
├── python/
│   ├── 00_generate_synthetic_data.py
│   ├── 01_data_profiling.py
│   ├── 02_run_sql_quality_checks.py
│   ├── 03_run_readmission_analysis.py
│   ├── 04_build_analytics_model.py
│   ├── 05_build_kpi_layer.py
│   └── 06_export_kpi_data.py
│
├── sql/
│   ├── 01_data_quality_checks.sql
│   ├── 02_readmission_analysis.sql
│   ├── 03_analytics_model.sql
│   └── 04_kpi_layer.sql
│
└── dashboard/
    └── README.md
