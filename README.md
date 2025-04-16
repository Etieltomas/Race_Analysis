# Race Analysis Tool

This project provides a **Race Analysis Tool** to analyze telemetry data for a specific driver's lap in a Formula 1 race. The tool visualizes speed and throttle data throughout a selected lap and highlights key circuit corners for a detailed performance breakdown.

## Features

- **Lap-Specific Analysis**: Select a specific lap number for detailed telemetry insights.
- **Dual-Axis Visualization**: Display speed and throttle on a single chart for easy comparison.
- **Corner Highlighting**: Annotate telemetry graphs with circuit corner markers.
- **Interactive Input**: Specify the year, race, and driver interactively for customized analysis.

## Technologies Used

- **FastF1**: Fetches and processes Formula 1 telemetry and event data.
- **Matplotlib**: Creates visualizations of speed and throttle data.
- **Pandas**: Manages and analyzes telemetry data.
- **Python**: Serves as the backend for telemetry processing and visualization.

## Usage

1. Clone the repository and ensure Python 3.x is installed.
2. Install dependencies using:
   ```bash
   pip install fastf1 matplotlib pandas numpy
3. Run the script:
   ```bash
   python3 main.py
4. Provide the required inputs:

- **Year**: Specify the race year (e.g., 2023).
- **Race**: Enter the name of the race (e.g., Monaco).
- **Driver**: Enter the driver's code (e.g., VER for Verstappen, HAM for Hamilton).
- **Lap Number**: Choose a lap number for analysis.

5. View the resulting graph displaying:

- **Speed** (in blue)
- **Throttle percentage** (in green)
- **Circuit corner markers** (in cyan)
