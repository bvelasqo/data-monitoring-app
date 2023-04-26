# COVID-19 Data Monitoring Application

This application monitors and analyzes data on COVID-19 cases, deaths, and tests from various data sources. It uses a component called CovidDataService to download data in JSON format and then presents graphs and charts to the user.

## Third-Party Library Integration

To generate the graphs and charts, the application uses a third-party plotting and analytics library that is optimized for generating images from CSV data.

To integrate the third-party library without tightly coupling the application to it, an adapter class is used to transform the CSV data into a format that can be used by the plotting library.

## Repository Contents

- `covid_data_service.py`: The CovidDataService component for downloading COVID-19 data in CSV format.
- `csv_data_adapter.py`: The adapter class for transforming CSV data into a format compatible with the plotting library.
- `csv_plotter.py`: The plotting library integration component.
- `example.py`: An example usage of the CovidDataService, CSVDataAdapter, and CSVPlotter components.

## Usage

To use the application, simply run the `example.py` file. This will download the COVID-19 data in CSV format, transform it into a format compatible with the plotting library using the CSVDataAdapter, and generate graphs using the CSVPlotter.

## Requirements

- Python 3.x
- requests library
- Third-party plotting and analytics library (see CSVPlotter for details)
