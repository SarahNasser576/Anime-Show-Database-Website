//Sarah Nasser
$(document).ready(function () {
    $("input").on("keypress", function(event) {
        if (event.which === 13) {
            event.preventDefault();
            if ($(this).attr("id") === "character-input" || $(this).attr("id") === "tag-input") {
                let inputValue = $(this).val().trim();
                if (inputValue) {
                    let containerSelector = $(this).attr("id") === "character-input" ? 
                        "#characters-container" : "#tags-container";
                    let errorSelector = $(this).attr("id") === "character-input" ? 
                        "#characters-error" : "#tags-error";
                    
                    let tagExists = false;
                    $(containerSelector).find(".tag").each(function() {
                        if ($(this).text().replace(" ×", "").trim() === inputValue) {
                            tagExists = true;
                        }
                    });
    
                    if (!tagExists) {
                        let tagHtml = `<span class="tag">${inputValue} <span class="remove-tag">&times;</span></span>`;
                        $(containerSelector).append(tagHtml);
                        $(this).val("");
                        $(errorSelector).text("");
                    } else {
                        $(errorSelector).text("This item is already added!");
                    }
                }
            }
        }
    });
    
    $("#edit-form").on("submit", function(event) {
        event.preventDefault();
        $(".text-danger").text("");
    
        let characters = [];
        $("#characters-container .tag").each(function() {
            characters.push($(this).text().replace(" ×", "").trim());
        });
    
        let genres = [];
        $("input[name='genres']:checked").each(function() {
            genres.push($(this).val());
        });
    
        let tags = [];
        $("#tags-container .tag").each(function() {
            tags.push($(this).text().replace(" ×", "").trim());
        });
    
        let isValid = true;
        if ($("#title").val().trim() === "") {
            $("#title-error").text("Title is required.");
            isValid = false;
        }
        
        let startYear = $("#start_year").val().trim();
        if (!startYear || isNaN(startYear) || startYear.length !== 4 || parseInt(startYear) < 1963 || parseInt(startYear) > 2025) {
            $("#start-year-error").text("Start year must be between 1963 and 2025.");
            isValid = false;
        }
    
        let endYear = $("#end_year").val().trim();
        if (endYear) {
            if (isNaN(endYear) || endYear.length !== 4 || parseInt(endYear) < 1963 || parseInt(endYear) > 2025) {
                $("#end-year-error").text("End year must be between 1963 and 2025.");
                isValid = false;
            } else if (parseInt(endYear) <= parseInt(startYear)) {
                $("#end-year-error").text("End year must be greater than start year.");
                isValid = false;
            }
        }
        
        if ($("#image").val().trim() === "") {
            $("#image-error").text("Image URL is required.");
            isValid = false;
        }
        if ($("#summary").val().trim() === "") {
            $("#summary-error").text("Summary is required.");
            isValid = false;
        }
        if ($("#writer").val().trim() === "") {
            $("#writer-error").text("Writer is required.");
            isValid = false;
        }
        if (genres.length === 0) {
            $("#genres-error").text("At least one genre is required.");
            isValid = false;
        }
        if (characters.length === 0) {
            $("#characters-error").text("At least one character is required.");
            isValid = false;
        }
        if (tags.length === 0) {
            $("#tags-error").text("At least one tag is required.");
            isValid = false;
        }
        if ($("#age_rating").val().trim() === "") {
            $("#age-rating-error").text("Age rating is required.");
            isValid = false;
        }
        if ($("#number_episodes").val().trim() === "") {
            $("#episodes-error").text("Number of episodes is required.");
            isValid = false;
        }
        if ($("#average_rating").val().trim() === "") {
            $("#rating-error").text("Average rating is required.");
            isValid = false;
        }
        if ($("#preview").val().trim() === "") {
            $("#preview-error").text("Preview is required.");
            isValid = false;
        }
    
        if (!isValid) {
            console.log("Form validation failed");
            return;
        }
    
        let formData = {
            title: $("#title").val(),
            start_year: $("#start_year").val(),
            end_year: $("#end_year").val(),
            summary: $("#summary").val(),
            writer: $("#writer").val(),
            age_rating: $("#age_rating").val(),
            number_episodes: $("#number_episodes").val(),
            average_rating: $("#average_rating").val(),
            image: $("#image").val(),
            characters: characters,
            genres: genres,
            tags: tags,
            preview: $("#preview").val()
        };

        const pathParts = window.location.pathname.split('/');
        const itemId = pathParts[pathParts.length - 1];
        $.ajax({
            url: `/edit/${itemId}`,
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function(data) {
                if (data.message === "Success") {
                    window.location.href = data.link;
                } else {
                    alert("Error: " + data.error);
                }
            },
            error: function(error) {
                console.error("Error:", error);
            }
        });
    });

    $("#discard-btn").on("click", function() {
        if (confirm("Are you sure you want to discard changes?")) {
            const pathParts = window.location.pathname.split('/');
            const itemId = pathParts[pathParts.length - 1];
            window.location.href = `/view/${itemId}`;
        }
    });

    $(document).on('click', '.remove-tag', function() {
        $(this).closest('.tag').remove();
    });
});