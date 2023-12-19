//document.getElementById("checkPercentage").addEventListener("click", function() {
//  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
//    chrome.tabs.sendMessage(tabs[0].id, { action: "checkPercentage" });
//  });
//});
//
//chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//  if (request.action === "showPercentage") {
//    document.getElementById("result").innerText = request.percentage;
//  }
//});
document.getElementById("checkPercentage").addEventListener("click", function() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: "checkPercentage" });
  });
});

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "showPercentage") {
    const parsedPercentage = JSON.parse(request.percentage);
    document.getElementById("result").innerText = parsedPercentage;
  }
});

