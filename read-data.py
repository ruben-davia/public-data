import pandas as pd
import requests
from io import StringIO
from davia import Davia

app = Davia()


@app.task
def read_csv_from_github() -> list[dict]:
    # Convert the GitHub web URL to a raw URL
    url = "https://raw.githubusercontent.com/ruben-davia/public-data/dd906dc35abc020a8a95b2403c837243d912a200/random_data.csv"

    try:
        # Get the raw content from GitHub
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Read the CSV content
        csv_content = StringIO(response.text)
        df = pd.read_csv(csv_content)

        # Get only the first 10 rows

        # Convert DataFrame to list of dictionaries
        result = df.to_dict(orient="records")

        # Ensure we return a list even if empty
        return result if result else []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    app.run()
