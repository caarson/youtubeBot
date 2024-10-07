// Fill in information below to access proxy:
var host = "PROXY_ADDRESS"
var port = "PROXY PORT"
var username = "USERNAME HERE"
var password = "PASSWORD HERE"

//////////////////////////////
// Proxy Information
//////////////////////////////

var config = {
    mode: "fixed_servers",
    rules: {
      singleProxy: {
        scheme: "http",
        host: host
        port: parseInt(port)
      },
      bypassList: ["foobar.com"]
    }
  };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: username
            password: password
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls: ["<all_urls>"]},
        ['blocking']
);