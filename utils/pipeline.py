import fastf1
import pandas as pd


# extracts the nexessary data from the session and returns it as a pandas dataframe 
def extract_session_data(year: int, grand_prix_name: str, session_name: str, merge_weather=True) -> pd.DataFrame:

    session = fastf1.get_session(year, grand_prix_name, session_name)
    session.load()

    laps = session.laps.copy()

    for col in ['Sector1Time', 'Sector2Time', 'Sector3Time']:
        if col in laps.columns:
            laps[col + '_s'] = laps[col].dt.total_seconds()

    laps.drop(columns=['Sector1Time', 'Sector2Time', 'Sector3Time'], inplace=True)

    if 'LapStartTime' in laps.columns:
        laps['LapStartTime_s'] = laps['LapStartTime'].dt.total_seconds()

    if 'LapTime' in laps.columns:
        laps['LapTime_s'] = laps['LapTime'].dt.total_seconds()
        laps.drop(columns=['LapTime'], inplace=True)

    if merge_weather:
        weather = session.weather_data.copy()
        weather['Time_s'] = weather['Time'].dt.total_seconds()
        weather.drop(columns=['Time'], inplace=True)
        laps = laps.merge(weather, left_on='LapStartTime_s', right_on='Time_s', how='left')
        laps.drop(columns=['Time_s'], inplace=True)

    return laps



# cleans the session data by removing inaccurate lines and NA values
def clean_session_data(laps: pd.DataFrame):

    clean = laps.copy()

    if 'IsAccurate' in clean.columns:
        clean = clean[clean['IsAccurate'] == True]
    if 'SpeedFL' in clean.columns:
        clean = clean[clean['SpeedFL'].notna()]
    if 'LapTime_s' in clean.columns:
        clean = clean[clean['LapTime_s'].notna()]

    return clean.reset_index(drop=True)


# returns the data fro a specific driver based on the driver code 
def get_driver_laps(df, driver_code):
    return df[df['Driver'] == driver_code].reset_index(drop=True)


# computes the FP2 features that are not present in the dataset initially
# like average lap time in FP2, best lap time in FP2, and total laps done in FP2
def extract_fp2_features(df):

    fp2_features = df.groupby("Driver").agg({
        "LapTime_s": ["mean", "min", "count"]
    })

    fp2_features.columns = ["fp2_avg_lap", "fp2_best_lap", "fp2_total_laps"]
    fp2_features = fp2_features.reset_index()

    return fp2_features



# extract necessary Quali features, like fastest lap in qualifying, and 
# qualifying position
def extract_quali_features(df_quali):
    df_quali = df_quali[df_quali['LapTime_s'].notna()]
    
    fastest_laps = df_quali.groupby('Driver')['LapTime_s'].min().reset_index()
    fastest_laps.rename(columns={'LapTime_s': 'FastestQualiLap'}, inplace=True)
    
    fastest_laps['QualiPosition'] = fastest_laps['FastestQualiLap'].rank(method='min').astype(int)

    return fastest_laps



# combines the fp2 features, quali features, and the final result dictionary 
# to create the dataframe with all the necessary data for modeling
def assemble_race_dataset(fp2_features, quali_features, race_results_dict):
    combined_df = fp2_features.merge(quali_features, on="Driver", how="inner")

    results_df = pd.DataFrame.from_dict(race_results_dict, orient='index').reset_index()
    results_df.columns = ['Driver', 'RacePosition', 'DNF']

    final_df = combined_df.merge(results_df, on="Driver", how="inner")

    return final_df



# combines the race dataframe to the master dataframe 
# which contains all the previously extracted data
def append_to_master_dataset(master_df, race_df):
    return