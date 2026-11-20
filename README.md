# BBC News Headline Scraper

A lightweight Python command-line application that retrieves the BBC News homepage and prints the first five unique news headlines.

The project uses `requests` to fetch the page and `BeautifulSoup4` to extract headline elements. It provides a simple, dependency-minimal example of web scraping, HTML parsing, deduplication, and basic HTTP error handling.

## Features

- Fetches the latest headlines from the BBC News homepage
- Selects HTML elements marked as BBC news card headlines
- Removes duplicate headline text
- Prints a maximum of five unique headlines
- Uses a browser-style user agent
- Applies a 10-second request timeout
- Reports non-successful HTTP responses

## How It Works

1. Sends a GET request to `https://www.bbc.com/news`.
2. Adds a user-agent header to identify the client as a browser.
3. Checks the HTTP status code before processing the response.
4. Parses the returned HTML with BeautifulSoup.
5. Finds headline elements with the `h2` tag and `data-testid="card-headline"` attribute.
6. Removes empty and duplicate headline text.
7. Stops after collecting five unique headlines.
8. Prints each headline in a numbered list.

## Requirements

- Python 3.8 or newer
- `requests`
- `beautifulsoup4`

## Installation

Clone the repository:

```bash
git clone https://github.com/Karthickbalakrishnan/bbc-news-headline-scraper.git
cd bbc-news-headline-scraper
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the scraper from the project directory:

```bash
python headlines.py
```

Example output:

```text
1. Headline title
2. Headline title
3. Headline title
4. Headline title
5. Headline title
```

The actual output depends on the current BBC News homepage and may contain fewer than five headlines if the page structure or available content changes.

## Error Handling

The scraper exits with a printed message when the HTTP response status is not successful. For example:

```text
Failed to load page: 403
```

Network failures that occur before an HTTP response is received are not currently caught. Exceptions such as connection errors or request timeouts may terminate the script with a Python traceback.

## Project Structure

```text
bbc-news-headline-scraper/
├── headlines.py       # Main scraper script
├── README.md          # Project documentation
├── LICENSE            # MIT license
└── .gitignore         # Git exclusion rules
```

## Important Notes

- This project is intended for educational use and is not affiliated with or endorsed by BBC.
- BBC News may update its HTML structure or block automated traffic, in which case the scraper may stop finding headlines.
- The BBC website and scraped content remain subject to BBC's applicable terms and policies.
- The script is not a full RSS or news API client and should not be relied on for guaranteed real-time delivery.
- Use reasonable request frequency; avoid repeatedly or aggressively scraping the website.

## Potential Improvements

- Add structured exception handling for connection and timeout errors
- Move the scraper into reusable functions
- Support command-line options for headline count and BBC page URL
- Log informational and error messages consistently
- Add automated tests using mocked HTTP responses
- Detect additional or alternate BBC headline elements
- Add a `requirements.txt` file for reproducible dependency installation

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Submit a pull request with a clear description of the update.

Please keep changes focused and avoid introducing unnecessary dependencies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
