//Sarah Nasser
$(document).ready(function() {
    function setupTagInput(inputSelector, containerSelector, errorSelector) {
        $(inputSelector).on("keypress", function(event) {
            if (event.which === 13) {
                event.preventDefault();
                let inputValue = $(this).val().trim();
                if (inputValue) {
                    let tagExists = $(containerSelector).find(`.tag:contains('${inputValue}')`).length > 0;
                    if (!tagExists) {
                        let tagHtml = `<span class="tag">${inputValue} <span class="remove-tag">&times;</span></span>`;
                        $(containerSelector).append(tagHtml);
                        $(this).val("");
                        $(errorSelector).text("");
                    } else {
                        alert("This tag is already added!");
                    }
                }
            }
        });

        $(containerSelector).on("click", ".remove-tag", function() {
            $(this).parent().remove();
        });
    }

    setupTagInput("#genre-input", "#genres-container", "#genres-error");
    setupTagInput("#character-input", "#characters-container", "#characters-error");
    setupTagInput("#tag-input", "#tags-container", "#tags-error");

    $("#add-form input").not("#genre-input, #character-input, #tag-input").on("keypress", function(event) {
        if (event.which === 13) {
            event.preventDefault();
        }
    });

    $("#add-form").on("submit", function(event) {
        event.preventDefault();
        $(".text-danger").text("");
        $("#success-message").hide();

        let isValid = true;

        let title = $("#title").val().trim();
        if (!title) {
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

        let summary = $("#summary").val().trim();
        if (!summary) {
            $("#summary-error").text("Summary is required.");
            isValid = false;
        }

        let writer = $("#writer").val().trim();
        if (!writer) {
            $("#writer-error").text("Writer name is required.");
            isValid = false;
        }

        let ageRating = $("#age_rating").val().trim();
        if (!ageRating) {
            $("#age-rating-error").text("Please select an age rating.");
            isValid = false;
        }

        let numberEpisodes = $("#number_episodes").val().trim();
        if (!numberEpisodes || isNaN(numberEpisodes) || parseInt(numberEpisodes) <= 0) {
            $("#episodes-error").text("Please enter a valid number of episodes.");
            isValid = false;
        }

        let averageRating = $("#average_rating").val().trim();
        if (!averageRating || isNaN(averageRating) || parseFloat(averageRating) < 0 || parseFloat(averageRating) > 10) {
            $("#rating-error").text("Please enter a valid rating between 0 and 10.");
            isValid = false;
        }

        let imageUrl = $("#image").val().trim();
        if (!imageUrl) {
            $("#image-error").text("Image URL is required.");
            isValid = false;
        }

        let genres = [];
        $("input[name='genres']:checked").each(function() {
            genres.push($(this).val());
        });
        if (genres.length === 0) {
            $("#genres-error").text("At least one genre is required.");
            isValid = false;
        }

        let characters = $("#characters-container .tag").map(function() { 
            return $(this).contents().first().text().trim(); 
        }).get();
        if (characters.length === 0) {
            $("#characters-error").text("At least one character is required.");
            isValid = false;
        }

        let tags = $("#tags-container .tag").map(function() { 
            return $(this).contents().first().text().trim(); 
        }).get();
        if (tags.length === 0) {
            $("#tags-error").text("At least one tag is required.");
            isValid = false;
        }

        let previewInput = $("#preview").val().trim();
        if (!previewInput) {
            $("#preview-error").text("Preview is required.");
            isValid = false;
        }

        if (!isValid) return;

        let formData = {
            title,
            start_year: parseInt(startYear),
            end_year: endYear ? parseInt(endYear) : null,
            summary,
            writer,
            genres,
            characters,
            tags,
            age_rating: ageRating,
            number_episodes: parseInt(numberEpisodes),
            average_rating: parseFloat(averageRating),
            image: imageUrl,
            preview: previewInput
        };

        $.ajax({
            type: "POST",
            url: "/add",
            contentType: "application/json",
            data: JSON.stringify(formData),
            success: function(response) {
                $("#success-message").show();
                $("#view-item-link").attr("href", response.link);

                $("#add-form")[0].reset();
                $(".tag").remove();
                $("#title").focus();
            },
            error: function(xhr) {
                alert(xhr.responseJSON.error);
            }
        });
    });
});