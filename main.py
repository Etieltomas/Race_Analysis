import fastf1
from fastf1 import plotting
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plotting.setup_mpl(misc_mpl_mods=False, color_scheme='fastf1')

# Enable caching to speed up subsequent accesses
fastf1.Cache.enable_cache('cache')


def main(year, race, driver):
    session = fastf1.get_session(year, race +' Grand Prix', 'R')
    session.load()

    max_laps = session.laps['LapNumber'].max()
    lap_number = int(input(f"Enter the lap number you want to analyze (1-{max_laps}): "))

    while lap_number < 1 or lap_number > max_laps:
        lap_number = input(f"Invalid lap number! Please enter a valid lap number (1-{max_laps}): ")

    driver_lap = session.laps.pick_drivers(driver).pick_laps(lap_number).get_telemetry()

    corners = session.get_circuit_info().corners

    fig, ax1 = plt.subplots(1, 1, figsize=(12, 6))
    ax1.plot(driver_lap['SessionTime'], driver_lap['Speed'], label='Speed', color='blue')
    ax1.set_xlabel('Session Time')
    ax1.set_ylabel('Speed (km/h)')

    ax2 = ax1.twinx()
    ax2.plot(driver_lap['SessionTime'], driver_lap['Throttle'], label='Throttle', color='green')
    ax2.set_ylabel('Throttle (%)')
    
    corners_time = []
    for corner in corners[['Number', 'Distance']].itertuples():
        corner_number = corner.Number 
        corner_distance = corner.Distance  

        # Find the telemetry point closest to the corner's distance
        closest_point = driver_lap.iloc[(driver_lap['Distance'] - corner_distance).abs().idxmin()]
        corner_time = closest_point['SessionTime']

        corners_time.append([corner_number, corner_time])

    corners_time_dataframe = pd.DataFrame(corners_time, columns=['Corner', 'Time'])
    
    ax1.vlines(corners_time_dataframe['Time'], ymin=0, ymax=driver_lap['Speed'].max(), label='Corners', color='cyan')
    ax1.grid()
    ax1.set_title(f'{driver} Telemetry Analysis for the {lap_number} lap in {race} {year}')
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2)
    plt.tight_layout()
    plt.show()

def get_race_name(year):
    races = fastf1.get_event_schedule(year)["Country"].unique()
    race_name = input("Enter the name of the race: ").capitalize()
    while not (race_name in races):
        race_name = input("Race not found! Please, enter a valid race name: ")
    
    return race_name

def welcome():
    print("\n\n-----------------------------------------")
    print("Welcome to the Race Analysis Tool")
    print("This tool allows you to analyze the speed and throttle of the driver for any given lap of the race.")
    print("-----------------------------------------")
    print("Please enter the following information:")

    year = int(input("Year (e.g., 2023): "))
    race = get_race_name(year)
    driver = input("Driver (e.g., 'VER', 'HAM'): ")

    main(year, race, driver)

if __name__ == "__main__":
    welcome()
