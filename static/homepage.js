//Sarah Nasser
$(document).ready(function() {
    const popularShows = [
        {id: 1, title: "Attack on Titan", link: "/view/1", image: "https://images.weserv.nl/?url=https://static.wikia.nocookie.net/voiceacting/images/d/df/ShingekiNokyojin.jpg", preview: "Humanity is on the brink of extinction due to massive Titans, and after witnessing his mother's death, young Eren vows to eliminate them. Along with his friends, he joins the fight for humanity's survival."},
        {id: 6, title: "Fullmetal Alchemist: Brotherhood", link: "/view/6", image: "https://m.media-amazon.com/images/M/MV5BMzNiODA5NjYtYWExZS00OTc4LTg3N2ItYWYwYTUyYmM5MWViXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg", preview: "After a failed attempt to resurrect their mother using alchemy, brothers Edward and Alphonse Elric suffer devastating consequences. Determined to restore their bodies, they embark on a quest for the Philosopher's Stone, with Edward joining the military as a State Alchemist."},
        {id: 2, title: "One Piece", link: "/view/2", image: "https://m.media-amazon.com/images/M/MV5BMTNjNGU4NTUtYmVjMy00YjRiLTkxMWUtNzZkMDNiYjZhNmViXkEyXkFqcGc@._V1_.jpg", preview: "After the Pirate King, Gol D. Roger, reveals the location of his treasure, the One Piece, from his execution, many fail to claim it. Twenty-two years later, Monkey D. Luffy sets out on a dangerous journey to find it and become the next Pirate King."},
        {id: 7, title: "Haikyu!!", link: "/view/7", image: "https://m.media-amazon.com/images/M/MV5BYjYxMWFlYTAtYTk0YS00NTMxLWJjNTQtM2E0NjdhYTRhNzE4XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg", preview: "Hinata Shouyou, inspired by a volleyball player known as 'the Small Giant,' forms a team to pursue his passion. After a defeat by rival Kageyama, he enrolls in the same high school and must work with Kageyama to become champions."}
    ];

    const container = $("#popular-shows");
    let row = $(`<div class="row"></div>`);
    popularShows.forEach(item => {
        let col = $(`
            <div class="col-md-3 col-xs-12 d-flex flex-column align-items-center text-center">
                    <a href="${item.link}">
                        <div class="popularShowsImagesContainer">
                            <img src="${item.image}" alt="${item.title} image" class="popularShowsImages">
                        </div>
                    </a>
                    <p class="mt-2 fw-bold titleHomePageLink"><a href="${item.link}">${item.title}</a></p>
                    <p>${item.preview}</p>
            </div>
        `)
        row.append(col);
    });
    container.append(row);
});