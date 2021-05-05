function openAddForm() {
    closeRemoveForm();
    document.getElementById("addClass").style.display = "block";
}

function closeAddForm() {
    document.getElementById("addClass").style.display = "none";
}
function openRemoveForm() {
    closeAddForm();
    document.getElementById("removeClass").style.display = "block";
}

function closeRemoveForm() {
    document.getElementById("removeClass").style.display = "none";
}