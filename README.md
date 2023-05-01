# Ecar Project

## Introduction

In this project, we aim to analyze the trend of electric car sales in Germany from 2017 to 2021. We will use registration data of electric cars to explore the changes in the market over the years. 

## Data Source

## Data Source

The data used in this project comes from the following sources:

- [Bundesnetzagentur - Ladesäulenregister](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/Ladesaeulenkarte/start.html)
- [Kraftfahrt-Bundesamt - Neuzulassungen von Personenkraftwagen nach Segmenten und Modellreihen seit 1955 (xlsx)](https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2023_02.xlsx?__blob=publicationFile&v=6)
- [Kraftfahrt-Bundesamt - Fahrzeugzulassungen (Übersicht) (html)](https://www.kba.de/DE/Statistik/Produktkatalog/produkte/Fahrzeuge/fz6_b_uebersicht.html)

Select the dropdown to access the links:

<details>
<summary>Bundesnetzagentur - Ladesäulenregister</summary>
    
https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/Ladesaeulenkarte/start.html
    
</details>

<details>
<summary>Kraftfahrt-Bundesamt - Neuzulassungen von Personenkraftwagen nach Segmenten und Modellreihen seit 1955 (xlsx)</summary>

https://www.kba.de/SharedDocs/Downloads/DE/Statistik/Fahrzeuge/FZ28/fz28_2023_02.xlsx?__blob=publicationFile&v=6
    
</details>

<details>
<summary>Kraftfahrt-Bundesamt - Fahrzeugzulassungen (Übersicht) (html)</summary>

https://www.kba.de/DE/Statistik/Produktkatalog/produkte/Fahrzeuge/fz6_b_uebersicht.html
    
</details>


## Data Cleaning

We performed several data cleaning steps to prepare the data for analysis. 

- We filtered the data to only include electric cars.
- We dropped irrelevant columns such as "Unnamed: 0".
- We replaced missing values with appropriate values using forward fill method.
- We converted the data types of some columns from string to integer or float.
- We merged the data from the different excel files into a single dataframe.

## Data Analysis

We analyzed the data to understand the trends and patterns in electric car sales in Germany. 

- We created visualizations to explore the distribution of electric car sales across different manufacturers, models, and regions.
- We used statistical methods to identify significant changes in electric car sales over the years.
- We analyzed the relationship between the power and the number of new registrations of electric cars.

## Conclusion

Our analysis shows that the market for electric cars is growing rapidly in Germany. We observed a significant increase in the number of new registrations of electric cars over the years. We also found that certain manufacturers and models are more popular among buyers. Finally, we found that there is a positive relationship between the power and the number of new registrations of electric cars. 

Overall, our analysis provides valuable insights for car manufacturers, policy makers, and consumers who are interested in the electric car market in Germany.

