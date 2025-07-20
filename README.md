# create-spotify-playlist
📦 GitHub Repository Description 🎵 Automatically create a private Spotify playlist from Billboard Hot 100 songs of any date. Uses web scraping, the Spotify API, and Python automation.

🎧 Billboard 100 to Spotify Playlist Generator
This Python project lets you travel back in time and automatically create a Spotify playlist from the Billboard Hot 100 chart on any specific date. It combines web scraping with the Spotify Web API, allowing you to relive musical history in just a few seconds.


🚀 Features
Scrapes the Billboard Hot 100 chart for any given date

Uses the Spotify API to search for each song

Automatically creates a private playlist with matching tracks

Stores API credentials securely using .env

Skips songs that don’t exist on Spotify and notifies the user


🛠️ Technologies Used
spotipy: Python client for Spotify Web API

BeautifulSoup: For HTML scraping of Billboard charts

requests: For web requests

dotenv: For managing environment variables


📁 Project Structure

📦 billboard-to-spotify/
├── main.py         # Main script
├── .env            # Stores Spotify API keys (ignored by git)
├── token.txt       # Spotify OAuth token cache
├── song.txt        # Output of scraped Billboard songs


▶️ How to Use
1. Clone the repository
   git clone https://github.com/yourusername/billboard-to-spotify.git
cd billboard-to-spotify

2. Install dependencies
   pip install -r requirements.txt
   If requirements.txt doesn’t exist, just install manually:
   pip install spotipy beautifulsoup4 requests python-dotenv
   
3. Create your .env file

  Inside your project folder, create a .env file:
  CLIENT_ID=your_spotify_client_id
  CLIENT_SECRET=your_spotify_client_secret
  REDIRECT_URI=https://example.com/callback
  USERNAME=your_spotify_username
4. Run the script
  python main.py
  

🧪 Example
Which year you would like to go? Please write in YYYY-MM-DD format: 2010-07-01
...

✔️ Playlist created: Billboard 100 of 2010-07-01

✔️ Added 92 songs to your private Spotify playlist!

⚠️ Some songs were skipped if not found on Spotify



🔐 Keep Your Credentials Safe

Make sure your .env and token.txt are listed in .gitignore:
.env
token.txt
