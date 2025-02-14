document.getElementById("submit").addEventListener("click", function() {
    let fileInput = document.getElementById("full_ss");
    let file = fileInput.files[0];

    let formData = new FormData();
    formData.append("user_id", document.getElementById("user_id").value);
    formData.append("server_id", document.getElementById("server_id").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("login", document.getElementById("login").value);
    formData.append("password", document.getElementById("password").value);
    formData.append("jumlah", document.getElementById("jumlah").value);
    formData.append("pembayaran", document.getElementById("pembayaran").value);
    formData.append("whatsapp", document.getElementById("whatsapp").value);
    if (file) {
        formData.append("full_ss", file);
    }

    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(result => alert(result.message))
    .catch(error => console.error('Error:', error));
});
