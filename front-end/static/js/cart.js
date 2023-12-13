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