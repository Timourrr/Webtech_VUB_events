document.querySelectorAll(".auth-card input:not([type=hidden])").forEach((input) => {
    const msg = document.createElement("small");
    msg.className = "field-error";
    input.after(msg);

    input.addEventListener("input", () => {
        msg.textContent = input.validity.valid ? "" : input.validationMessage;
    });
});

// Passwords must match (HTML5 has no attribute for this)
const p1 = document.getElementById("id_password1");
const p2 = document.getElementById("id_password2");

if (p1 && p2) {
    const checkMatch = () => {
        p2.setCustomValidity(p2.value && p1.value !== p2.value ? "Passwords do not match" : "");
        p2.dispatchEvent(new Event("input"));   // updates the message
    };
    p1.addEventListener("input", checkMatch);
    p2.addEventListener("input", checkMatch);
}