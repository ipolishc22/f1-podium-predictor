import fastf1
import pandas as pd

def extract_session_data(year: int, grand_prix_name: str, session_name: str, merge_weather=True):
    session = fastf1.get_session(year, grand_prix_name, session_name)
    session.load()

    # load the laps information into the dataframe
    laps_columns_to_keep = ["Driver", "Stint", "Compound", "TyreLife", "LapStartTime_s", 
                 "LapTime_s", "TrackStatus", "SpeedFL", "SpeedI1", "SpeedI2"]
    laps_temp = session.laps.copy()
    laps = laps_temp[laps_columns_to_keep]

    # load the weather data into the dataframe 
    weather_columns_to_keep = ["Time","TrackTemp"]
    weather_temp = session.weather_data.copy()
    weather = weather_temp[weather_columns_to_keep]
    
    # transforming laptime and lapstarttime to seconds instead of timedelta
    laps['LapStartTime_s'] = laps['LapStartTime'].dt.total_seconds()
    laps.drop(columns=["LapStartTime"], inplace=True)
    weather['Time_s'] = weather['Time'].dt.total_seconds()
    weather.drop(columns=["Time"], inplace=True)

    laps = laps.sort_values("LapStartTime_s")
    weather = weather.sort_values("Time_s")

    laps["Session"] = session_name.upper()

    merged = pd.merge_asof(
        laps,
        weather,
        left_on="LapStartTime_s",
        right_on="Time_s",
        direction="backward"
    )

    return merged


def clean_session_data(laps: pd.DataFrame):

    laps = laps.copy()

    clean_laps = laps[
    (laps["IsAccurate"] == True) &
    (laps["LapTime"].notna()) &
    (laps["SpeedFL"].notna()) 
    ]

    return clean_laps


def get_driver_laps(df, driver_code):
    return df[df['Driver'] == driver_code].reset_index(drop=True)