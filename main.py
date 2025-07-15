import requests
import csv

API_KEY = "3b0c0372"  # 🔑 Replace this with your actual OMDb API key
API_URL = "http://www.omdbapi.com/"

def get_movie_titles():
    """Takes input from the user and returns a list of movie/series titles."""
    titles = input("Enter movie/series titles (comma-separated): ")
    return [title.strip() for title in titles.split(',') if title.strip()]

def fetch_movie_data(title):
    """Calls OMDb API and returns data for a given title."""
    params = {
        'apikey': API_KEY,
        't': title
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    if data.get('Response') == 'True':
        return {
            'Title': data.get('Title', 'N/A'),
            'Year': data.get('Year', 'N/A'),
            'Genre': data.get('Genre', 'N/A'),
            'Director': data.get('Director', 'N/A'),
            'IMDB Rating': data.get('imdbRating', 'N/A'),
            'Runtime': data.get('Runtime', 'N/A'),
            'Plot': data.get('Plot', 'N/A')
        }
    else:
        print(f"[!] '{title}' not found. Reason: {data.get('Error')}")
        return None

def save_to_csv(data_list, filename):
    """Saves a list of dictionaries to a CSV file."""
    if not data_list:
        print("[!] No valid data to save.")
        return

    fieldnames = data_list[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

    print(f"[✔] Data saved to '{filename}' successfully!")

def main():
    """Main driver function to glue everything together."""
    print("🎬 Welcome to the Movie & Series Info Fetcher!\n")
    titles = get_movie_titles()

    movie_data_list = []
    for title in titles:
        data = fetch_movie_data(title)
        if data:
            movie_data_list.append(data)
            print(f"{data['Title']} ({data['Year']})")  # Print title & year

    save_to_csv(movie_data_list, 'movie_data.csv')

if __name__ == "__main__":
    main()
