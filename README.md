## Steam Laplace Percentage: Chrome Extension

**Calculate the Laplace percentage of any Steam game to estimate your chance of enjoying it!**

This Chrome extension brings the classic Laplace's principle of indifference (also known as the Rule of Succession) to your Steam browsing experience. By analyzing a Steam game's positive and negative review count, it offers a simple, data-driven estimation of your personal enjoyment potential.

---

### Features

* **Laplace Percentage:** View the calculated Laplace percentage based on positive and negative reviews.
* **Review Sentiment:** Get a quick glimpse at the positive and negative review breakdown.
* **Easy Integration:** Seamlessly integrates into Steam game listing pages.
* **Lightweight and Efficient:** Minimal impact on browsing performance.
* **Backend Integration:** Uses a FastAPI backend to fetch and process review data.

---

### Installation

#### Chrome Extension
1. Download the code from this repository as a ZIP file.
2. Open Chrome and navigate to `chrome://extensions/`.
3. Enable "Developer mode" in the top right corner.
4. Click "Load unpacked" and select the unpacked ZIP file.
5. The extension will be installed and active on Steam game pages.

#### Backend (FastAPI)
1. Navigate to the `backend_fastapi` directory.
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn beautifulsoup4 requests
   ```
3. Start the backend server:
   ```bash
   uvicorn f_api:app --reload
   ```
   The backend will run at `http://127.0.0.1:8000` by default.

---

### How it Works

The extension calculates the Laplace percentage using the following formula:

```
Laplace Percentage = (Positive Reviews + 1) / (Total Reviews + 2) * 100
```

![Screenshot](./Screenshot%202023-12-20%20at%2012.59.57.png)

This formula reflects the principle of equal uncertainty, assuming no prior knowledge about your specific preferences. Higher percentages suggest a greater likelihood of enjoying the game based on the overall community's experience.

#### Technical Overview
- **Frontend:**
  - The Chrome extension injects a content script into Steam game pages.
  - When the user clicks the popup button, the extension sends the current page URL to the backend.
  - The popup displays the Laplace percentage result returned from the backend.
- **Backend:**
  - The FastAPI server receives the URL, scrapes the review counts using BeautifulSoup, and applies the Laplace formula.
  - The result is returned as a formatted string.

#### Usage Example
1. Open a Steam game page in Chrome.
2. Click the extension icon and then the "Check Laplace Score" button.
3. The Laplace percentage will be displayed in the popup.

---

### Code Structure

- `manifest.json` - Chrome extension manifest file.
- `popup.html`, `popup.js`, `styles.css` - Popup UI and logic.
- `content.js` - Content script injected into Steam pages.
- `backend_fastapi/f_api.py` - FastAPI backend for scraping and calculation.
- `icon.png`, `icon3.ico` - Extension icons.
- `Screenshot 2023-12-20 at 12.59.57.png` - Example screenshot.

---

### Disclaimer

Remember, this extension is just a tool created for learning purposes, and enjoyment is subjective. While the Laplace percentage offers an estimate, other factors like genre, gameplay style, and personal taste ultimately determine your experience.

---

### Contribute

We welcome contributions to improve the extension! Feel free to fork the repository, suggest features, or fix bugs.

---

### Credits

* Developed by Samuel Wallace
* Powered by Chrome Extensions APIs and FastAPI




