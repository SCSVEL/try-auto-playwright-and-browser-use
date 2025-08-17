# try-auto-playwright-and-browser-use

This project demonstrates the use of Playwright for browser automation and testing, with both TypeScript and Python examples.

Trying auto-playwright lib with TS + browser-use lib with Python


![ScreenRecording](https://github.com/user-attachments/assets/43db7e8e-3550-44d1-bb9b-3611b59bb845)


## Project Structure

- `main.py` — Main Python script
- `package.json` — Node.js project configuration
- `playwright.config.ts` — Playwright configuration (TypeScript)
- `tests/` — Contains test files
  - `test.autoplaywright.spec.ts` — Playwright test (TypeScript)
  - `test.broweruse.spec.py` — Playwright/browser test (Python)
- `types/auto-playwright.d.ts` — TypeScript type definitions
- `test-results/` — Test output and reports

## Getting Started

### Prerequisites
- Node.js (for Playwright and TypeScript tests)
- Python 3.x (for Python tests)

### Install Dependencies

#### Node.js
```sh
npm install browser-use
npm install playwright
npx playwright install chromium
```

#### Python
Set up a virtual environment and install dependencies as needed.

### Running Tests

#### TypeScript/Playwright
```sh
npx playwright test
```

#### Python
Run your Python test files as usual, e.g.:
```sh
python -m unittest tests/test.broweruse.spec.py
```

## License
MIT
