document.addEventListener("DOMContentLoaded", function() {
    let dropArea = document.getElementById("drop-area");

    dropArea.addEventListener("dragover", function(e) {
        e.preventDefault();
        dropArea.classList.add("highlight");
    });

    dropArea.addEventListener("dragleave", function() {
        dropArea.classList.remove("highlight");
    });

    dropArea.addEventListener("drop", function(e) {
        e.preventDefault();
        dropArea.classList.remove("highlight");

        let file = e.dataTransfer.files[0];
        document.getElementById("file-input").files = e.dataTransfer.files;
    });
});
