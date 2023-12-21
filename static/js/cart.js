function showSuccess() {
    var successMessageDiv = document.getElementById("success-message");
    var newSuccess = document.createElement("div");
    newSuccess.innerHTML = `<div class="rounded m-0 p-0 
    font-20 text-center text-white my-1 position-relative" style="background-color: #0a5230b7;
    cursor: pointer;" onclick="removeSuccess()"> اضافه شد <i class="bi bi-x-lg font-15 
    position-absolute" style="top: 5px; right: 10px;"></i></div>`

    successMessageDiv.appendChild(newSuccess)

    setTimeout(function() {
        successMessageDiv.removeChild(successMessageDiv.firstChild)
    }, 3000);
}

function removeSuccess() {
    var successMessageDiv = document.getElementById("success-message");
    successMessageDiv.removeChild(successMessageDiv.firstChild)
}

function addToCart(element){
    var itemId = element.getAttribute("item_id");
    var cart = JSON.parse(getCookie("cart")) || {};
    cart[itemId] = (cart[itemId] || 0) + 1;
    setCookie("cart", JSON.stringify(cart), 1);
}
function getCookie(name) {
    var cookieName = name + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookieArray = decodedCookie.split(';');
    
    for(var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i].trim();
        if (cookie.indexOf(cookieName) == 0) {
            return cookie.substring(cookieName.length, cookie.length);
        }
    }
    return null;
}
function setCookie(name, value, days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}
