//Sarah Nasser
$(document).ready(function() {
    $("#search-form").on("submit", function(event) {
        let query = $("#search-input").val().trim();

        if (!query) {
            event.preventDefault();
            $("#search-input").val("").focus();
        } else {
            query = query.replace(/[^a-zA-Z0-9 ]/g, "");
            $("#search-input").val(query);
        }
    });
});