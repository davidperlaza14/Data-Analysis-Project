# Data Analysis Project

This project is an interactive tool to analyze and visualize data. It uses `Dash` to create a web dashboard where you can see different charts based on a CSV file.

## Project Structure

- `data/`: Contains the dataset `dataset.csv`.
- `notebooks/`: Contains the Jupyter Notebook `analysis.ipynb` for exploratory analysis.
- `src/`: Contains scripts for data processing and visualization.
  - `data_processing.py`: Functions to load and clean data.
  - `visualization.py`: Functions to create charts.
  - `dashboard.py`: Defines the web application.
- `app.py`: Main script to run the application.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Usage

1. **Install dependencies**: Run `pip install -r requirements.txt`.
2. **Run exploratory analysis**: Open `notebooks/analysis.ipynb` in Jupyter Notebook and run the cells.
3. **Start the web app**: Run `python app.py` and open your browser at `http://127.0.0.1:8050/`.
4. **Explore data**: Use the dropdown menu to select different columns and see the updated charts.

## Dependencies

The required dependencies are in the `requirements.txt` file.

## Contribution

If you want to contribute, please fork the repository and send a pull request.
