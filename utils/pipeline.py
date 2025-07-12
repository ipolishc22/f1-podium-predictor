import fastf1
import pandas as pd

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



def clean_session_data(laps: pd.DataFrame):

    clean = laps.copy()

    if 'IsAccurate' in clean.columns:
        clean = clean[clean['IsAccurate'] == True]
    if 'SpeedFL' in clean.columns:
        clean = clean[clean['SpeedFL'].notna()]
    if 'LapTime_s' in clean.columns:
        clean = clean[clean['LapTime_s'].notna()]

    return clean.reset_index(drop=True)



def get_driver_laps(df, driver_code):
    return df[df['Driver'] == driver_code].reset_index(drop=True)


def clean_fp2_data(fp2_df: pd.DataFrame) -> pd.DataFrame:
    return clean_session_data(fp2_df)


def extract_fp2_features(df):

    fp2_features = df.groupby("Driver").agg({
        "LapTime_s": ["mean", "min", "count"]
    })

    fp2_features.columns = ["fp2_avg_lap", "fp2_best_lap", "fp2_total_laps"]
    fp2_features = fp2_features.reset_index()

    return fp2_features


def extract_quali_features(df_quali):
    # Remove laps with NaN times
    df_quali = df_quali[df_quali['LapTime_s'].notna()]
    
    # Group by driver and take min lap time (fastest)
    fastest_laps = df_quali.groupby('Driver')['LapTime_s'].min().reset_index()
    fastest_laps.rename(columns={'LapTime_s': 'FastestQualiLap'}, inplace=True)
    
    # Optional: Assign grid positions by rank
    fastest_laps['QualiPosition'] = fastest_laps['FastestQualiLap'].rank(method='min').astype(int)

    return fastest_laps


def assemble_race_dataset(df_fp2, df_quali, df_results):
    df_fp2_clean = clean_fp2_data(df_fp2)
    fp2_features = extract_fp2_features(df_fp2_clean)
    quali_features = extract_quali_features(df_quali)
    
    merged = fp2_features.merge(quali_features, on="Driver", how="inner")
    final = merged.merge(df_results, on="Driver", how="inner")
    
    return final



'''
def load_all_races(race_paths):
    race_dfs = []
    for fp2_path, quali_path, result_df in race_paths:
        df_fp2 = pd.read_csv(fp2_path)
        df_quali = pd.read_csv(quali_path)
        df_result = result_df  # might be passed from EDA manually
        race_df = assemble_race_dataset(df_fp2, df_quali, df_result)
        race_dfs.append(race_df)
    return pd.concat(race_dfs, ignore_index=True)
'''


def build_feature_row():
    return 

def append_to_master_dataset():
    return


def load_official_results():
    return 


def process_race(fp2_df, q_df, race_name, position_dict=None):
    return