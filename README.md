# Content-Scrapping-and-Summarizing-AI-Tool


A Python project to scrape articles from supported websites, summarize them using Google Gemini, and store the results in a local SQLite database. Includes a CLI for summary retrieval.

---

## Features

- Scrape articles from supported sites (Quotes to Scrape, The Hacker News)
- Summarize content using Google Gemini API
- Store articles and summaries in SQLite
- Retrieve summaries by article ID or list all summaries via CLI

---

## Setup

1. **Clone the repository and navigate to the project folder.**
   ```bash
   git clone https://github.com/hemangsengar/Content-Scrapping-and-Summarizing-Tool.git
   ```
   

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key:**
   - Create a `.env` file in the project root:
     ```
     API_KEY=your_gemini_api_key_here
     ```

---

## Usage

### Scrape and Summarize (Interactive CLI)

Run the main script and follow the prompts:
```bash
python main.py
```
You will be asked to select a website to scrape.

---

### Retrieve Summaries (Database CLI)

#### View all summaries:
```bash
python database.py
```
Choose option 1 in the menu.

#### View summary by ID:
```bash
python database.py
```
Choose option 2 in the menu and enter the article ID.

---

### (Optional) Direct CLI Commands

You can also add this to `database.py` for direct commands:
```python
if __name__ == "__main__":
    create_articles_table()
    cli_menu()
```
This is already present in your code.

---

## Project Structure

- `main.py` — Main script for scraping and summarizing
- `scrap.py` — Scraper logic for supported sites
- `Gemini.py` — Summarization using Google Gemini
- `database.py` — SQLite storage, retrieval functions, and CLI
- `requirements.txt` — Python dependencies

---

## Extending

- Add new sites to `SITE_CONFIGS` in `scrap.py` to support more sources.
- Integrate with Flask for a web interface if needed.

---

## License

MIT License

---

**Enjoy summarizing your favorite web content with AI!**
