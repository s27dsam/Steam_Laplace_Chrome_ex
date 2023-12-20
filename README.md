## Steam Laplace Percentage: Chrome Extension

**Calculate the Laplace percentage of any Steam game to estimate your chance of enjoying it!**

This Chrome extension brings the classic Laplace's principle of indifference or known as the Rule of successionto to your Steam browsing experience. By analyzing a Steam game's positive and negative review count, it offers a simple, data-driven estimation of your personal enjoyment potential.

### Features

* **Laplace Percentage:** View the calculated Laplace percentage based on positive and negative reviews.
* **Review Sentiment:** Get a quick glimpse at the positive and negative review breakdown.
* **Easy Integration:** Seamlessly integrates into Steam game listing pages.
* **Lightweight and Efficient:** Minimal impact on browsing performance.

### Installation

1. Download the code from this repository as a ZIP file.
2. Open Chrome and navigate to `chrome://extensions/`.
3. Enable "Developer mode" in the top right corner.
4. Click "Load unpacked" and select the unpacked ZIP file.
5. The extension will be installed and active on Steam game pages.

### How it Works

The extension calculates the Laplace percentage using the following formula:

```
Laplace Percentage = (Positive Reviews + 1) / (Total Reviews + 2) * 100
```

![Alt Text](./Screenshot%202023-12-20%20at%2012.59.57.png)


This formula reflects the principle of equal uncertainty, assuming no prior knowledge about your specific preferences. Higher percentages suggest a greater likelihood of enjoying the game based on the overall community's experience.

### Disclaimer

Remember, this extension is just a tool i created for learning purposes, and enjoyment is subjective. While the Laplace percentage offers an estimate, other factors like genre, gameplay style, and personal taste ultimately determine your experience.

### Contribute

We welcome contributions to improve the extension! Feel free to fork the repository, suggest features, or fix bugs.

### Credits

* Developed by Samuel Wallace
* Powered by Chrome Extensions APIs




