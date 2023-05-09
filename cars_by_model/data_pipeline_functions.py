# Creating Functions to clean/ join tables for further Analysis.


# Defining a join_function that creates clean DataFrame on the model_analysis
import pandas as pd

def clean_join_model(a: list, b: list):

    
    
    def clean_model_fuel(a: str, b):
        #read the sheet
        regis_model_fuel_df = pd.read_excel(a, sheet_name = 'model_and_fuel_type')
        regis_model_fuel_df['Hersteller'] = regis_model_fuel_df['Hersteller'].fillna(method = 'ffill')

        # drop the first column
        regis_model_fuel_df = regis_model_fuel_df.drop(['Unnamed: 0'], axis = 1)

        # drop the rows with ZUSAMMEN
        regis_model_fuel_df = regis_model_fuel_df.drop(regis_model_fuel_df[regis_model_fuel_df['Hersteller'].str.contains('ZUSAMMEN')].index)

        # concentrate on only electric cars
        regis_model_fuel_df = regis_model_fuel_df[regis_model_fuel_df['Kraftstoffart'] == 'E']

        regis_model_fuel_df_copy = regis_model_fuel_df.copy()
        regis_model_fuel_df_copy.rename(columns={'Hersteller': 'manufacturer',
                                            'Handelsname': 'model',
                                            'Typ-Schl.-Nr.': 'tsn',
                                            'kW': 'power_kw',
                                            'Kraftstoffart': 'fuel_type',
                                            'Allrad': 'drive_type',
                                            'Aufbauart': 'body_type',
                                            'Insgesamt': 'total',
                                            'Wohnmobile': 'motorhomes',
                                            'private\nHalter': 'private_owners',
                                            'Halter\nbis 29 Jahre': 'owners_under_29_years',
                                            'Halter\nab 60 Jahre': 'owners_over_60_years',
                                            'weibliche\nHalter': 'female_owners'}, inplace=True)
        # check NaN
        list = ['model', 'new_registration_per_model']
        rows_with_nan = regis_model_fuel_df.loc[regis_model_fuel_df[list].isna().any(axis=1)]
        rows_with_nan
        
        regis_model_fuel_df = regis_model_fuel_df_copy
        # Getting rid of leading or trailing whitespaces
        regis_model_fuel_df = regis_model_fuel_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        # Variable with all columns to change
        cols_to_convert_fuel = ['total', 'motorhomes', 'private_owners',
            'owners_under_29_years', 'owners_over_60_years', 'female_owners']
        # Replace - with 0
        for col_fuel in cols_to_convert_fuel:
            regis_model_fuel_df[col_fuel] = regis_model_fuel_df[col_fuel].replace('-', '0').replace(',', '.').astype(int)

        # drop for duplicates
        regis_model_fuel_df = regis_model_fuel_df.drop_duplicates()
        # add new columns
        regis_model_fuel_df['business_owners'] = regis_model_fuel_df['new_registration_per_model'] - regis_model_fuel_df['private_owners']
        regis_model_fuel_df['owners_between_29_and_60_years'] = regis_model_fuel_df['new_registration_per_model'] - regis_model_fuel_df['owners_under_29_years'] - regis_model_fuel_df['owners_over_60_years']
        regis_model_fuel_df['male_owners'] = regis_model_fuel_df['new_registration_per_model'] - regis_model_fuel_df['female_owners']
        regis_model_fuel_df["year"] = b
        # drop columns
        regis_model_fuel_df = regis_model_fuel_df.drop(['power_kw', 'drive_type', 'body_type', 'motorhomes'], axis = 1)
        regis_model_fuel_df = regis_model_fuel_df.reset_index(drop=True)
        # concentrate on only electric cars
        regis_model_fuel_e_df = regis_model_fuel_df[regis_model_fuel_df['fuel_type'] == 'E']
        # final
        regis_model_fuel_e_df  = regis_model_fuel_e_df.reset_index(drop=True)
        regis_model_fuel_e_df.to_csv('regis_model_fuel_e_df_2019.csv', index=False)
        return regis_model_fuel_e_df
    
    def clean_model_state(a: str, b):
        # read excel
        regis_model_state_df = pd.read_excel(a, sheet_name = 'model_by_state')
        regis_model_state_df['Hersteller'] = regis_model_state_df['Hersteller'].fillna(method = 'ffill')

        # drop the first column
        regis_model_state_df = regis_model_state_df.drop(['Unnamed: 0'], axis = 1)

        # drop the rows with ZUSAMMEN 
        regis_model_state_df = regis_model_state_df.drop(regis_model_state_df[regis_model_state_df['Hersteller'].str.contains('ZUSAMMEN')].index)

        # rename
        regis_model_state_df.rename(columns={'Hersteller': 'manufacturer',
                                            'Handelsname': 'model',
                                            'Typ-Schl.-Nr.': 'tsn',
                                            'Baden-\nWürttemberg' : 'Baden-Württemberg',
                                            'Bayern': 'Bayern',
                                            'Berlin': 'Berlin',
                                            'Branden-\nburg': 'Brandenburg',
                                            'Bremen': 'Bremen',
                                            'Hamburg': 'Hamburg',
                                            'Hessen': 'Hessen',
                                            'Mecklenburg-\nVorpommern': 'Mecklenburg-Vorpommern',
                                            'Nieder-\nsachsen': 'Niedersachsen',
                                            'Nordrhein-\nWestfalen': 'Nordrhein-Westfalen',
                                            'Rheinland-\nPfalz': 'Rheinland-Pfalz',
                                            'Saarland': 'Saarland',
                                            'Sachsen': 'Sachsen',
                                            'Sachsen-\nAnhalt': 'Sachsen-Anhalt',
                                            'Schleswig-\nHolstein': 'Schleswig-Holstein',
                                            'Thüringen': 'Thüringen',
                                            'Sonstige': 'special',
                                            'Deutschland': 'new_registration_per_model'}, inplace=True)
        # Drop columns not needed in final DataFrame
        # Nan
        rows_with_nan = regis_model_state_df.loc[regis_model_state_df['new_registration_per_model'].isna()]
        rows_with_nan
        regis_model_state_df = regis_model_state_df.dropna(subset=['new_registration_per_model'])
        # Variable with all columns to change
        cols_to_convert = ['Baden-Württemberg', 'Bayern',
            'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
            'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen',
            'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt',
            'Schleswig-Holstein', 'Thüringen', 'special']
        # Getting rid of leading or trailing whitespaces
        regis_model_state_df = regis_model_state_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        # Replace - with 0
        for col1 in cols_to_convert:
                regis_model_state_df[col1] = regis_model_state_df[col1].replace('-', '0').replace(',', '.').astype(float).fillna(0).astype(int)
        # drop duplicates
        regis_model_state_df = regis_model_state_df.drop_duplicates()
        #  want to add fuel type but need to check (ues data from 1.1)
        regis_model_state_df = regis_model_state_df.reset_index(drop=True)
        regis_model_state_df["year"] = b
        regis_model_state_df['check'] = regis_model_fuel_df['new_registration_per_model']
        regis_model_state_df[regis_model_state_df.new_registration_per_model != regis_model_state_df.check]
        # if there is no results for last cell, then continue
        # add fuel type
        # Drop the 'check' column which was only used for comparison purposes
        regis_model_state_df = regis_model_state_df.drop(['check'], axis = 1)
        # Add the 'fuel_type' column to the state DataFrame by merging with the fuel DataFrame
        regis_model_state_df['fuel_type'] = regis_model_fuel_df['fuel_type']
        regis_model_state_df['model'] = regis_model_fuel_df['model']
        regis_model_state_df['tsn'] = regis_model_fuel_df['tsn']
        # put all states into one column
        id_cols = pd.concat([regis_model_state_df.iloc[:, :3], regis_model_state_df.iloc[:, 20:]], axis=1)
        # Reshape the DataFrame by melting the state columns into one column
        regis_model_state_df = pd.melt(regis_model_state_df, id_vars=id_cols, value_vars=regis_model_state_df.columns[3:20], var_name='federal_state', value_name='new_registration')
        # Drop the 'new_registration_per_model' column, which is redundant after melting the DataFrame
        regis_model_state_df = regis_model_state_df.drop(['new_registration_per_model'], axis = 1)
        # final
        regis_model_state_df = regis_model_state_df.reset_index(drop=True)
        regis_model_state_e_df = regis_model_state_df[regis_model_state_df.fuel_type == 'E']
        # final
        regis_model_state_e_df = regis_model_state_e_df.reset_index(drop=True)
        regis_model_state_e_df.to_csv('regis_model_state_e_df_2019.csv', index=False)
        regis_model_state_e_df["year"] = b
        
        return regis_model_state_e_df

    result = []

    for i in range(len(a)):
        model_fuel_df = clean_model_fuel(a[i], b[i])
        model_state_df = clean_model_state(a[i], b[i])
        joined_df = model_fuel_df.merge(model_state_df,how='inner',on=['model', 'tsn'])
        result.append(joined_df)

    return pd.concat(result)

# New wrapper function
def clean_join_model_default():
    a = ['model_17.xlsx', 'model_18.xlsx', 'model_19.xlsx', 'model_20.xlsx', 'model_21.xlsx']
    b = [2017, 2018, 2019, 2020, 2021]
    return clean_join_model(a, b)