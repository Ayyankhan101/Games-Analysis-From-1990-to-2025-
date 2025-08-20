# Games Analysis Dashboard

This project provides an interactive dashboard for exploring a dataset of the best video games of all time, based on Metacritic scores. The dashboard is built with Streamlit and allows for dynamic filtering and visualization of the data.

## Dataset

The project uses two CSV files:

*   `Best_Games_of_All_Time.csv`: The original dataset containing information about over 13,000 video games.
*   `Best_Games_Cleaned.csv`: A cleaned version of the dataset used by the dashboard and analysis notebook.

The data includes the following columns:

*   `Name`: The title of the game.
*   `Launch_date`: The release date of the game.
*   `Rating`: The ESRB rating of the game.
*   `Metascore`: The Metacritic score of the game.
*   `Details`: A brief description of the game.

The data cleaning process involved:
*   Converting `Launch_date` to a datetime format.
*   Extracting the `Year` from the `Launch_date`.
*   Converting `Metascore` to a numeric type.
*   Handling missing values.

## Features

The interactive dashboard (`dashboard.py`) offers the following features:

*   **KPIs:** Key performance indicators such as total number of games, average Metascore, and the highest score.
*   **Filtering:**
    *   Filter games by a range of Metascores.
    *   Filter games by a range of release years.
    *   Filter games by ESRB rating.
*   **Visualizations:**
    *   A density heatmap of Metascores vs. Year.
    *   A jittered strip plot of Metascores vs. Year, colored by ESRB rating.
    *   A scatter plot showing the top N games per year, with bubble size corresponding to the Metascore.
    *   A table of the top 10 highest-rated games based on the selected filters.
    *   A heatmap showing the count of games by decade and Metascore tier.
    *   A word cloud generated from the game descriptions.

## Technologies Used

The project is built with Python and the following libraries:

*   Streamlit
*   Pandas
*   NumPy
*   Plotly
*   Seaborn
*   Matplotlib
*   Joypy
*   WordCloud

## Installation

To run this project locally, follow these steps:

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/Games_Analysis.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd Games_Analysis
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To launch the interactive dashboard, run the following command in your terminal:

```bash
streamlit run dashboard.py
```

This will open the dashboard in your web browser.

## Analysis Summary

The `Analysis.ipynb` notebook contains a detailed analysis of the video game dataset. Key insights include:

*   **Metascore Distribution:** The distribution of Metascores is approximately normal, centered around a mean of 70.
*   **Top-Rated Games:** The top-rated games of all time include "The Legend of Zelda: Ocarina of Time," "SoulCalibur," and "Grand Theft Auto IV."
*   **Trends Over Time:** The analysis explores how the average Metascore and the number of games released have changed over the years.
*   **ESRB Ratings:** The distribution of games across different ESRB ratings is examined.
*   **Game Descriptions:** A word cloud is used to visualize the most common themes in game descriptions.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.
