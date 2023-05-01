# Ecar Project

## Introduction

This project is a Capstone-Project in a Data Analytics Bootcamp from neuefische GmbH. We aim to perform a general overview of the market regarding electric vehicles and the charging stations network, with the following hypotheses:

H1: The growth of electric vehicle sales is positively correlated with the expansion of charging infrastructure which differs from state to state and which makes some states even more attractive for EV-adoption.

H2: The target group for electric vehicles is primarily young people up to 29 years old and may vary by gender, as they are more likely to understand and embrace e-mobility concepts.

H3: Leading EV companies do not change over time and are not affected locally.

H4: Preferences for charging infrastructure plug types do not vary significantly across different states in Germany.

Our MVP is a Dashboard for the Management of the Company that will cover the following KPIs and additional dashboard features:

KPI1: number of sales of ecars
KPI2: number of competitors
KPI3: number of charging stations

DB-Feature1 and 2: Group of Interest broken down by age and gender
DB-Feature3: Top competitors with additional information on them
DB-Feature4: Top models of the competition
DB-Feature5: Map of Germany displaying the locations of the charging stations
DB-Feature6: Top connector types of charging stations

## Data Source

The data used in this project comes from the following sources:

- [Bundesnetzagentur - Ladesäulenregister](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/Ladesaeulenkarte/start.html)
- [Kraftfahrt-Bundesamt - Neuzulassungen von Personenkraftwagen (Umwelt)](https://www.kba.de/DE/Statistik/Fahrzeuge/Neuzulassungen/Umwelt/n_umwelt_node.html)
- [Kraftfahrt-Bundesamt - Fahrzeugzulassungen von Personenkraftwagen (Marke, Hersteller)](https://www.kba.de/DE/Statistik/Produktkatalog/produkte/Fahrzeuge/fz6_b_uebersicht.html)

Select the dropdown to access the links:

<details>
<summary>Bundesnetzagentur - Ladesäulenregister</summary>
    
https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/Ladesaeulenkarte/start.html
    
</details>

<details>
<summary>Kraftfahrt-Bundesamt - Neuzulassungen von Personenkraftwagen (Umwelt)</summary>

https://www.kba.de/DE/Statistik/Fahrzeuge/Neuzulassungen/Umwelt/n_umwelt_node.html
    
</details>

<details>
<summary>Kraftfahrt-Bundesamt - Fahrzeugzulassungen von Personenkraftwagen (Marke, Hersteller)</summary>

https://www.kba.de/DE/Statistik/Produktkatalog/produkte/Fahrzeuge/fz6_b_uebersicht.html
    
</details>

## Data Cleaning

We performed ETL (Extract, Transform, Load) to prepare the data for analysis using various tools and programming languages.

- We extracted the data from public data sources and imported them into Excel/Sheets and Jupyter Notebook using Python.
- We transformed the data by filtering the data, dropping irrelevant columns, replacing missing values with appropriate values using forward fill method, and converting the data types of some columns.
- We loaded the cleaned data into our PostgreSQL server using Dbeaver.
- We connected the cleaned DataFrames from PostgreSQL to Tableau for visualization.
- In Tableau we connected the Data Sets with their unique identifiers using the entity-relationship "Many-to-Many (n:n)"

Tools used:
- Python (in Jupyter Notebook)
- VSC
- PostgreSQL (in Dbeaver)
- Google Sheets/ Microsoft Excel
- Tableau

