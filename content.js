chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "checkPercentage") {
    const url = window.location.href;
    fetch(`http://127.0.0.1:8000/laplace_smoothing_percentage/?url=${encodeURIComponent(url)}`)
      .then(response => response.text())
      .then(percentage => {
        chrome.runtime.sendMessage({ action: "showPercentage", percentage });
      })
      .catch(error => console.error(error));
  }
});
