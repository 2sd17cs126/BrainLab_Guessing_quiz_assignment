document.addEventListener('DOMContentLoaded', function() {
        function showPopup(text) {
            document.getElementById("popup-text").textContent = text;
            document.getElementById("popup").style.display = "block";
        }

        document.getElementById("close-popup").addEventListener("click", function () {
            document.getElementById("popup").style.display = "none";
            window.location.href = "/game";
        });
        function validateForm() {
            var guess = document.forms["guess-form"]["guess"].value;
            if (guess.trim() === "") {
                alert("Please enter a capital city.");
                
                
                
               
                return false; // Prevent form submission
            }
            
            return true; // Allow form submission
        }
        // JavaScript logic to display the popup based on correctness
        var correctValue = "{{ correct }}";  // This will be "True" or "False" based on Django template
        console.log(correctValue)
        if (correctValue === "True") {
            showPopup("Your answer is correct!");
        } else if (correctValue === "False") {
            showPopup("Sorry, the correct answer is: {{ country.capital }}");
        }
    });