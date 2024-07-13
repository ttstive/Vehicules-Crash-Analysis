# Vehicle Crash Analysis Dashboard
<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python" width="50"/> <img src="https://pandas.pydata.org/static/img/pandas.svg" alt="Pandas" width="50"/> <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" alt="HTML" width="50"/>

This project is a comprehensive dashboard for analyzing vehicle crash data. It is built using Python, Streamlit, pandas, and Plotly. The dashboard provides insightful visualizations and metrics to help understand the patterns and factors associated with vehicle crashes.

## Features

- **Monthly Analysis**: Select a specific month for analysis to get detailed insights for that period.
- **Location Analysis**: Filter the data by location to focus on specific areas of interest.
- **Injury Type Distribution**: Visualize the distribution of different injury types using a pie chart.
- **Crash per Day**: A histogram showing the number of crashes per day, color-coded by injury type.
- **Collision Type vs. Primary Factor**: A detailed histogram showing the relationship between collision types and primary factors, categorized by injury type.
- **Total Accidents**: A prominently displayed metric showing the total number of accidents for the selected period and location.

## How to Run

### Install dependencies
Make sure you have the necessary libraries installed. You can install them using the following command:
```bash
pip install streamlit pandas plotly numpy openpyxl
```



##Run the application
###Save the code in a file named app.py and run the application using the following command:

```bash
Copy code
streamlit run app.py
Access the dashboard
Open a web browser and go to http://localhost:8501 to view the dashboard.
```

Preview
(![data_crash](https://github.com/user-attachments/assets/4da9b52f-d149-40b5-83d6-40ccdecf74ee)
)

## Project Structure

- `app.py`: Main application file containing the Streamlit code.
- `dados_limpos.xlsx`: The dataset containing cleaned vehicle crash data.

## Future Work

- Add more filters for deeper analysis (e.g., time of day, weather conditions).
- Include predictive analytics using machine learning models.
- Enhance the UI for better user experience.

## License

This project is licensed under the MIT License.

## Author

Estevão Lins
