# Sarah Nasser
from flask import Flask, request, jsonify, render_template, redirect, url_for, json
import urllib.parse
import re

app = Flask(__name__)

items = [
    {"id": 1, 
     "title": "Attack on Titan", 
     "start_year": 2013,
     "end_year": 2023,
     "summary": "Giant, unintelligent Titans have nearly wiped out humanity. The last survivors live within three massive walls, and no one has seen a titan in over a century until one day, a colossal Titan shatters the outermost wall. Ten-year-old Eren and his friend Mikasa watch in horror as his mother is devoured. Eren vows to eradicate the Titans and take revenge for mankind.",
     "genres": ["Action", "Adventure", "Drama", "Fantasy", "Horror"], 
     "characters": ["Eren Yeager", "Mikasa Ackerman", "Armin Arlert", "Annie Leonhart", "Jean Kirschtein", "Reiner Braun", "Levi Ackerman", "Erwin Smith", "Hange Zoe"],
     "writer": "Hajime Isayama", 
	 "average_rating": 9.1, 
	 "age_rating": "TV-MA", 
	 "number_episodes": 98,
	 "tags": ["Giant", "Man eating monster", "Titan", "Army", "Battle tactic", "Transformation", "Special ability", "Tragedy", "Gore"], 
	 "image": "https://images.weserv.nl/?url=https://static.wikia.nocookie.net/voiceacting/images/d/df/ShingekiNokyojin.jpg",
     "preview": "Humanity is on the brink of extinction due to massive Titans, and after witnessing his mother's death, young Eren vows to eliminate them. Along with his friends, he joins the fight for humanity's survival.",
     "link": "/view/1"},
    {"id": 2,
     "title": "One Piece",
     "start_year": 1999,
     "end_year": None,
     "summary": "Gol D. Roger, the Pirate King, obtained wealth, fame, and power before being captured. When he was about to get executed, he revealed that his treasure, the One Piece, was hidden in the Grand Line. Many set out to find it, but the Grand Line was too dangerous, and no one succeeded. Twenty-two years later, Monkey D. Luffy vowed to become a pirate, find the One Piece, and become the next Pirate King.",
     "genres": ["Action", "Adventure", "Comedy", "Drama", "Fantasy"], 
     "characters": ["Monkey D. Luffy", "Roronoa Zoro", "Nami", "Usopp", "Vinsmoke Sanji", "Tony Tony Chopper", "Nico Robin", "Brook", "Franky", "Jinbe"],
     "writer": "Eiichiro Oda", 
	 "average_rating": 9.0, 
	 "age_rating": "TV-14", 
	 "number_episodes": 1137,
	 "tags": ["Pirate", "Monkey D. Luffy character", "Quest", "Treasure", "Straw hat", "Pirate crew", "Devil fruits"], 
	 "image": "https://m.media-amazon.com/images/M/MV5BMTNjNGU4NTUtYmVjMy00YjRiLTkxMWUtNzZkMDNiYjZhNmViXkEyXkFqcGc@._V1_.jpg",
     "preview": "After the Pirate King, Gol D. Roger, reveals the location of his treasure, the One Piece, from his execution, many fail to claim it. Twenty-two years later, Monkey D. Luffy sets out on a dangerous journey to find it and become the next Pirate King.",
     "link": "/view/2"},
    {"id": 3,
     "title": "Jujutsu Kaisen",
     "start_year": 2020,
     "end_year": None,
     "summary": "Yuji Itadori, a kind-hearted teenager, joins his school’s Occult Club for fun but discovers that its members are real sorcerers who can manipulate the energy between beings for their own use. When a cursed talisman, Sukuna’s finger, is targeted by cursed beings, Yuji eats it to protect his friends and becomes Sukuna’s host. However, Yuji discovers he can control Sukuna’s power without interference. He enrolls in Tokyo Metropolitan Magic Technical College to consume all of Sukuna’s fingers, enable a full exorcism, and rid himself of Sukuna.",
     "genres": ["Action", "Adventure", "Fantasy", "Thriller"],
     "characters": ["Yuji Itadori", "Satoru Gojo", "Megumi Fushiguro", "Yuta Okkotsu", "Toge Inumaki", "Nobara Kugisaki", "Aoi Todo"],
     "writer": "Gege Akutami", 
	 "average_rating": 8.5, 
	 "age_rating": "TV-MA", 
	 "number_episodes": 48,
	 "tags": ["Martial arts", "Exorcism", "Supernatural thriller", "Violence", "Curse", "Dark fantasy", "Possession", "Demon", "Power", "Sorcery"], 
	 "image": "https://m.media-amazon.com/images/M/MV5BNmI1MmYxNWQtY2E5NC00ZTlmLWIzZGEtNzM1YmE3NDA5NzhjXkEyXkFqcGc@._V1_.jpg",
     "preview": "Yuji Itadori, a kind-hearted teen, unknowingly becomes the host of a powerful curse, Sukuna, after swallowing a cursed talisman. To rid himself of Sukuna, he joins a magic school and sets out to consume all of Sukuna's fingers.",
     "link": "/view/3"},
    {"id": 4,
     "title": "The Promised Neverland",
     "start_year": 2019,
     "end_year": 2021,
     "summary": "At Grace Field House, orphans live happily under the care of a kind ‘Mama,’ and they are all adopted by age 12. Their days include rigorous tests, followed by outdoor play, with only one rule: never leave the orphanage. One day, top-scoring orphans Emma and Norman break this rule and uncover the harrowing secret behind their existence. Using their intelligence, the children must work together to change their predetermined fate.",
     "genres": ["Action", "Adventure", "Drama", "Fantasy", "Horror", "Mystery", "Sci-Fi", "Thriller"],
     "characters": ["Emma", "Norman", "Conny", "Mujika"],
     "writer": "Kaiu Shirai",
     "average_rating": 8.1, 
     "age_rating": "TV-14",
     "number_episodes": 24,
     "tags": ["Dystopia", "Orphanage", "Survival", "Demon", "Evil", "Freedom", "Hope", "Demon society", "Forest", "Dark secret", "Lie", "Sibling relationship", "Friendship", "Betrayal"],
     "image": "https://m.media-amazon.com/images/M/MV5BMGQ4ZGJhZTUtZDQ5Mi00NTI1LWEyYjItMzIxM2VlNmY4MDEyXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
     "preview": "At Grace Field House, orphans live a seemingly perfect life until two of them, Emma and Norman, uncover a terrifying secret about their existence. Together with their friends, they must outsmart their captors and escape their grim fate.",
     "link": "/view/4"},
    {"id": 5,
     "title": "Detective Conan",
     "start_year": 1996,
     "end_year": None,
     "summary": "Japanese high school student Kudo Shinichi is renowned as the avior of the Japanese police. One day, while out with his girlfriend Mulilan, he witnesses an illegal transaction but is attached from behind and forced to take an experimental drug. Instead of killing him, the drug shrinks him into a primary school student. To investigate the man and his accomplices, Kudo goes by the pseudonym Edogawa Conan.",
     "genres": ["Action", "Comedy", "Crime", "Drama", "Mystery", "Romance", "Sci-Fi", "Thriller"],
     "characters": ["Edogawa Conan", "Ai Haibara", "Richard Moore", "Ran Mori", "Heiji Hattori", "Shuichi Akai"],
     "writer": "Gosho Aoyama",
     "average_rating": 8.5,
     "age_rating": "TV-14",
     "number_episodes": 1158,
     "tags": ["Child protagonist", "Detective as protagonist", "Mystery thriller", "Detective fiction", "Child detective", "Turned into a child", "Detective", "Secret", "Mysterious killer", "Group of friends", "Schoolboy", "Criminal investigation", "Secret identity", "Adult as child", "Sir Arthur Conan Doyle character"],
     "image": "https://m.media-amazon.com/images/M/MV5BNGNjMjVmODYtMGMzZi00MWUyLTk1ZDQtYzI2ZTk2MmYzYTZiXkEyXkFqcGc@._V1_.jpg",
     "preview": "After being shrunk into a child by a mysterious drug, high school detective Kudo Shinichi adopts the alias Edogawa Conan. He continues to solve crimes while searching for the criminals responsible for his transformation.",
     "link": "/view/5"},
    {"id": 6,
     "title": "Fullmetal Alchemist: Brotherhood",
     "start_year": 2009,
     "end_year": 2010,
     "summary": "Two brothers lose their mother to an incurable disease and try to resurrect her using alchemy, violating a taboo. The process fails, costing Edward Elric his left leg and Alphonse Elric his entire body. To save his body, Edward sacrifices his right arm to bind Alphonse’s soul to a suit of armor. With the help of a family friend, Edward receives automail prosthetics and vows to find the Philosopher’s Stone to restore their bodies. To achieve this goal, he becomes a State Alchemist, someone who uses their alchemy for the military.",
     "genres": ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Sci-Fi"],
     "characters": ["Edward Elric", "Alphonse Elric", "Roy Mustang", "Winry Rockbell", "Envy", "Maes Hughes"],
     "writer": "Hiromu Arakawa",
     "average_rating": 9.1,
     "age_rating": "TV-14",
     "number_episodes": 68,
     "tags": ["Alchemy", "Loss of limb", "Genocide", "Brother brother relationship", "Armor", "Military", "Steampunk", "Automail"],
     "image": "https://m.media-amazon.com/images/M/MV5BMzNiODA5NjYtYWExZS00OTc4LTg3N2ItYWYwYTUyYmM5MWViXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
     "preview": "After a failed attempt to resurrect their mother using alchemy, brothers Edward and Alphonse Elric suffer devastating consequences. Determined to restore their bodies, they embark on a quest for the Philosopher's Stone, with Edward joining the military as a State Alchemist.",
     "link": "/view/6"},
    {"id": 7,
     "title": "Haikyu!!",
     "start_year": 2014,
     "end_year": 2020,
     "summary": "Hinata Shouyou, a short middle schooler, falls in love with volleyball after watching a national championship match. Inspired by a star player known as “the Small Giant,” he forms a volleyball club, and in his final year, he finally assembles a team but faces a crushing defeat against championship favorite Kageyama. Determined to surpass Kageyama, Hinata enrolls in a high school he watched in the national championship and finds that Kageyama is also in the same school. The volleyball team must learn to work together if they want to become champions.",
     "genres": ["Comedy", "Drama", "Sport"],
     "characters": ["Hinata Shouyou", "Tobio Kageyama", "Yu Nishinoya", "Koshi Sugawara", "Daichi Sawamura"],
     "writer": "Haruichi Furudate",
     "average_rating": 8.7,
     "age_rating": "TV-14",
     "number_episodes": 89,
     "tags": ["Volleyball", "School", "Teen comedy", "Teen sport", "High school"],
     "image": "https://m.media-amazon.com/images/M/MV5BYjYxMWFlYTAtYTk0YS00NTMxLWJjNTQtM2E0NjdhYTRhNzE4XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
     "preview": "Hinata Shouyou, inspired by a volleyball player known as 'the Small Giant,' forms a team to pursue his passion. After a defeat by rival Kageyama, he enrolls in the same high school and must work with Kageyama to become champions.",
     "link": "/view/7"},
    {"id": 8,
     "title": "Your Lie in April",
     "start_year": 2014,
     "end_year": 2015,
     "summary": "Kousei Arima, a piano prodigy, plays with flawless precision under his strict mother’s guidance. After her sudden death, he develops a trauma that renders him unable to hear the piano and stops performing. Now living a quiet life with his friends Tsubaki Sawabe and Ryouta Watari, he still clings to music. Everything changes when he meets the eccentric violinist Kaori Miyazono, who makes him her accompanist. Through her influence and a small lie, Kaori brings color back into Kousei’s world.",
     "genres": ["Comedy", "Drama", "Music", "Romance"],
     "characters": ["Kousei Arima", "Kaori Miyazono", "Ryota Watari", "Tsubaki Sawabe", "Saki Arima"],
     "writer": "Naoshi Arakawa",
     "average_rating": 8.5,
     "age_rating": "TV-PG",
     "number_episodes": 24,
     "tags": ["Pianist", "Child Prodigy", "Death of mother", "Violinist", "Musical composition", "Metronome", "Teen romance"],
     "image": "https://m.media-amazon.com/images/M/MV5BZGMyYmFmNzgtMWQ4NS00MWE2LTg4YmEtZGY1MTBiODE0YmE5XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
     "preview": "Kousei Arima, a former piano prodigy, loses his ability to hear music after his mother's death, abandoning his passion. His world is reignited when eccentric violinist Kaori Miyazono convinces him to accompany her, helping him rediscover the joy of music.",
     "link": "/view/8"},
    {"id": 9,
     "title": "Komi Can't Communicate",
     "start_year": 2021,
     "end_year": 2022,
     "summary": "Admired for her beauty and graceful demeano, Shouko Komi struggles with extreme social anxiety and communication problems. Her attractiveness and silent nature makes her highly popular while preventing people from truly knowing her. She first communicates with Tadano over a blackboard and uses a notebook to express herself. Though she can speak on the phone, she dreams to overcome her struggles and make 100 friends.",
     "genres": ["Comedy", "Drama", "Romance"],
     "characters": ["Komi Shouko", "Osana Najimi", "Tadano Hitohito"],
     "writer": "Tomohito Oda",
     "average_rating": 7.7,
     "age_rating": "TV-14",
     "number_episodes": 24,
     "tags": ["Coming of age", "High school", "Love", "Friendship", "Teenage boy teenage girl relationship", "Social anxiety", "Female protagonist", "Shy girl"],
     "image": "https://m.media-amazon.com/images/M/MV5BZGMzZDY0MDUtYzY5OS00NmI0LTlhZmUtZGM2NjVjNjdiNThlXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
     "preview": "Shouko Komi, admired for her beauty but struggling with extreme social anxiety, dreams of making 100 friends despite her communication challenges. With the help of her classmate Tadano, she begins her journey to overcome her fears and connect with others.",
     "link": "/view/9"},
    {"id": 10,
     "title": "Snow White with the Red Hair", 
     "start_year": 2015,
     "end_year": 2016,
     "summary": "Shirayuki, a red-haired girl from Tanbarun, is an apothecary until Prince Raji demands she become his concubine. Unwilling to lose her freedom, she cuts her hair and flees into the forest, where she is rescued by Zen Wistalia, the second prince of the neighboring country Clarines, and his two aides. Hoping to repay their kindness, she dreams to become a court herbalist in Clarines. As Shirayuki adapts to palace life and Zen vows to prove himself as a worthy prince, they grow closer while navigating dangerous enemies.",
     "genres": ["Drama", "Fantasy", "Romance"],
     "characters": ["Shirayuki", "Zen Wistalia", "Kiki Seiran", "Mitsuhide Lowen", "Raji Shenazard"],
     "writer": "Sorata Akidzuki",
     "average_rating": 7.6,
     "age_rating": "TV-14",
     "number_episodes": 25,
     "tags": ["Red haired teenage girl", "Female protagonist", "Medicine woman", "Female pharmacist", "Fantasy romance", "Teen fantasy", "Royalty", "Prince", "Fictional kingdom", "Snow White", "Fairy tale"],
     "image": "https://m.media-amazon.com/images/M/MV5BNmM5NzM4ZDgtNGZhOC00YzljLWE0ZTEtZTNjNjg0MjFjYzk3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
     "preview": "Shirayuki, a red-haired apothecary, flees her country to escape an unwanted marriage proposal and finds refuge with Prince Zen of Clarines. As she adapts to life at the palace, she dreams of becoming a court herbalist while growing closer to Zen and facing various dangers together.",
     "link": "/view/10"},
    {"id": 11,
     "title": "Bleach",
     "start_year": 2004,
     "end_year": 2023,
     "summary": "High school student Kurosaki Ichigo has the rare ability to see ghosts, a power he’s had since childhood. His life changes when he and his sisters are attacked by a an evil, tormented spirit known as a Hollow, only to be saved by a Shinigami (Death God) named Kuchiki Rukia. Rukia gets injured during the battle and transfers her powers to Ichigo. Ichigo’s training and duty as a Shinigami begins, and he must maintain the balance between the world of the living and the world of the dead.",
     "genres": ["Action", "Adventure", "Fantasy"],
     "characters": ["Ichigo Kurosaki", "Rukia Kuchiki", "Sosuke Aizen", "Byakuya Kuchiki", "Orihime Inoue"],
     "writer": "Tite Kubo",
     "average_rating": 8.2,
     "age_rating": "TV-14",
     "number_episodes": 386,
     "tags": ["Supernatural fantasy", "Afterlife", "Seeing things other humans can't", "Ghosts", "Soul reaper", "Sword fighting", "Martial arts"],
     "image": "https://m.media-amazon.com/images/M/MV5BOWQwOWY5NTUtMjAyZi00YjQzLTkwODgtNmQwZjU1MGIzZDhjXkEyXkFqcGc@._V1_.jpg",
     "preview": "Kurosaki Ichigo, a high school student with the ability to see ghosts, gains the powers of a Shinigami after saving his family from an evil spirit. Now tasked with maintaining the balance between the living and the dead, Ichigo embarks on a journey of training and battle.",
     "link": "/view/11"},
    {"id": 12,
     "title": "Hunter x Hunter",
     "start_year": 2011,
     "end_year": 2014,
     "summary": "Gon Freecss, a young boy from Whale Island, learns that his father, whom he thought was dead, is alive and a top 'Hunter.' Inspired to find him, Gon decides to become a Hunter and leaves the island. To do so, he must pass the rigorous Hunter Examination, where he befriends Kurapika, Leorio, and Killua. Together, they face the challenges of the exam, with Gon aiming to become the best Hunter in the world and eventually reunite with his father.",
     "genres": ["Action", "Adventure", "Comedy", "Fantasy"],
     "characters": ["Gon Freecss", "Killua Zoldyck", "Kurapika", "Leorio Paradinight", "Hisoka", "Chrollo Lucilfer"],
     "writer": "Yoshihiro Togashi",
     "average_rating": 9.0,
     "age_rating": "TV-14",
     "number_episodes": 148,
     "tags": ["Friendship", "Training", "Fight", "Anti hero", "Child fights an adult", "Quest", "Supernatural fantasy", "Tournament", "Superpower"],
     "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFRUWGRcaGBcYGRsaHxgaHhsYGh8ZGxgYHyggGB0lGx0aITEhJyorLi4uGB8zODMtNygtLisBCgoKDg0OGxAQGy0lICYtLS0tLS0tLS0vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAQwAvAMBEQACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAAEBQIDBgcBAAj/xABIEAACAQIEAwUFBAcFBgYDAAABAhEAAwQSITEFQVEGEyJhcQcygZGhQlKxwRQjYnKS0fAkgrLC4RU0c6Li8RYzNVNjsxdDVP/EABoBAAIDAQEAAAAAAAAAAAAAAAECAAMEBQb/xAA/EQACAQIEAgcGAwYGAgMAAAAAAQIDEQQSITFBUQUTImFxgbEykaHB0fAUUuEjM0KisvEkU2JyktIVNEPC4v/aAAwDAQACEQMRAD8A8S1MgbfaPy0Fc+9jotl5gCBoByoIBK3pyqEPMXfVFzGildkF1zH3InJAjpr+OlWKCCW4bFK+gOo69ajjYgWUpQHyIKBADF4wI2UKWj3o5Ac/nTqNyXGVhiwkc9qVkJMxFAh9bBNRkLkU8qACTJ5VCIkZqEEfF+KpBUEHYGNdzEgzEfP4VbCL3BmQtS16inuOydkMjZgdRQbT0Jc0fCsQLggiHA1H5iqpKwrDWtetKAou4Y8udQKYMbJHKhca6JkSIZalwERYXkxHlNQlwVMoEAD0qahLFVegqEI33CqTGwmmSALrJa7ldiANCFA+OpNWO0dApNhjAeVJccBv2bZG0N1AP5VYmwONys2XHuP6AifgdaN0DKzzPiBr4ZOmX8/Kh2QO4XhbBAMgFm949fL0oNhUSXBZyMCPddgJ3jf86E9xRuQI19PnpSEIWsDqpzNpOk7zG8+n1NHMS5bawxHvHn+UfjrUbJcuNjdifDA09N/nQuK5GH7T8XMSRInwAgaQTzBny0J+IrXCFtTLUqN6Cbs/w7F466UsZQBqxY+FR15sef8AMTTTnGC1FhByehusX2bu4cAuyXAB4mQ7HqynVR57elZusUtjatFqDdwDyoXIAPxDu7mW2pZh7xBiPKefpVig2rtgu27JGh4Rj7t1MxQRmM66wNIAEa7nXrVUopO1xktNRqihhoN+Wx+VILsUtZ6igG4NeYDcfjRCihUU6/zqWYRVfxhQajxbKPvHy/lTqNw3Bl71IfNnJOqzpJ+6TsAfpTaPQlmtS/ubjjx3CJ5KIA8tdTUulsTKwiyioAoEAbUr11GiraELjzoBHnRSGsSw9r51GwhgtDTSluKVmx0kGPhvNG5LE0sn+taFwE+GYeO803ufktGRWwm9Z92ObD6a/lSkTLwT0NAGhbYQ86hGBdprZ7g+IKJEyYnyGmp+I61ZS9oqqPQ5Dxe8WutPLTedPWBNbTIbH2MYiMcySfHbaBrqRB2HlzP1nTPiF2S+g+0dQxgTvraKoe2gYslskkPMjMoBBB194jeZrKpJJ33NLTurbGMx/DcRZwz3LmW2wIVQRuS0CIJB8Osz+FXRyuSsKs1tTMYpBatgAmSyyQdW111PPzq5dpjSWSOgfwi9fUt3ACuRJtscyOACfeOqt8QKWaj/ABEyyiG8TbELbGJMKMo0UnUb68h6+cUscreUaW1yGE4rcVQQzQY0OoM+tRwVwWTG/DuLd6wQgKx26H+RquULLQFrBpSNNqqIZhLYuHOxkSco6Dr61c3l0LErlrMRpy6/z+NBDtFyvI2qEJ93m3qXsGxJbGk+X+tS5C4Wj0/OgC5datayQaBGT7qagC9UoCsjwq2fGrEZs5JHrsfSmkVyCnXxL8T+X50ALYjheJWmA3BYgCQee2oka+tFomVjW0opRSnivDhetMkweWsCeU6HSmjLK7iyV0cW7ScFfDXwL4YKxBZhBkT4ihGh0209a2xkpLQzNWepvMF2dtWcuKwiKSBOXvGNu9bjxWy7MSrHTKRoTAIg1lc3LsyNSglrA6ZgHQ21NsBVjQCAB5QNKztWL07gvaLh36Rh7lqAcymJ5MASpERqGg0YSyyuCSujFcP7OhGLXHw9xRprc2gyZESpkAREjWr3UvoiOSZosHwO3cVgj5VJ0AQRzWDIDOAQROhOvrVblbcCkwbtBwe/3LotsXcylfCeRESVMH4DNRi1e4bq2oBY7P2FgjNlj3ZkbfP61HNiuXIzFu4q3AwDZQ0666T1PlVlroY0wu5gGEwQCKq2FRlMNiliJiNqslFl0WraBa3VJ3oWGuEWQOtAgQi1CBNoCB8aGoGi9BNC4LHhtLGTSIiPL0qXYbE/CNTAg68tYipqCx9bxEyR7vLbX+tvhUsRwPWtsWDghCNJAmR0M+dRS01K3Evw17NcyN7wHhI2YE/iI2qNaCtWQtsWgUyyQVY7aFSDIGvTzovct4Dzg+ILWgWILCQT5gkajkY/Gg9yiSsxgrUopRxJLbJkuqtwMQoRgDmJMAANpMmmje+gNLal/COC2bFjuVsLaJzHIQPfadm1DRoJBOwqVFNPtFlKUbdkWYm5cw2YqxCkZhoCDpPMb8qXcusnqLX7Q4orHeweoRPpppT5UV6mZw+HvI7Fb7gPJb7TGd5ZpkGZ1Bq5zi1sMk1s9B1wDtHew0Wntd9bBhHUwy6AAEMYIGuxG9JKEZa7CNSTNzh8ddDKCudTJJCszKug1CCCddwB6HekUG9hM6WjA8WVNxwNATIEEbqpJg6+8T8TQcWtwXT2OfYu2FYgciR9atRaPOCtNlfj+Jqqe4rMTYtjLLeegHTflNaJbjR21CbdoD4c6UcNt29NDzP0oDJl73FRczEadRqd9IoJNuyC52QGOOkgBUVImdJM/Greq5iqpdg74pz9tv4iKKihxjwzihBVXggmC8kHynX0pJQ5BQ8usJiWOk6a6THWqkPsU/ouVtC2p66aSZ30/wC1G+hLhanzpGhGD23zXlGfYzE7wv8A1H5U1rRKpF+OwLlxct7zDgmAwiJPmNOVBNW1FUrBHC8A6MzMwYtA0BGkk6yep+QFRu4JSPeNcctYUeMksR4UXc+e+g8z9aso0J1X2TPVrQprtHMeI8UuXXzs7SNR4j4SOYPXz/CuvRw0aa5nOrYiVR8kdD7Ie0tWAsY+OQF8iQf+KOX723WN6Sph+MfcSFXhIedv8ZZsWrCalL1wSFba2IJddDESsQQPhWSNCMnexfPFukknxZynCdpl2uowPMoxI+ROnzNPLBSteDuWxx0b2krDzheIt3wWts2hggyCDHrWWpTlTdpGmFZTV4hf6Ifvfj/Oq7luYT9tuJ4gGzdW69t/1izbZkMeAjVSOeat+AUW5Jo5+ObVmiXYztJir2Kt2r2IuXFy3AA7ZoOXNudfsj5VbjqMFSzJcSjCVZOdmMOJYc97c1+03PzNcxSR1Uw7gttu7InZjz8h5UsrNkuhDw9wygjTyp5bllN3QfbQUhYXhKgRHxwBrkH7I+ROs+u1X09iuaT3E+EuXG0C6k+9psPjVrsjPGc5LT3m07N9krl1c+IY20aMmWMzSAwJUyIImBIOnoDkr4qFO9t1w8N/UKqzTtv3nQMBwLC21/VWkII96MzfBmk78vx2rkT6RnOXZeXudrPz4eneiOLa7TuW3MAl1MpA3JzKACD98euzDnrzEkQxs0+1fTg+K+q4c0CKcdYmT4tba1dKTpuJ5eUiJ12PQrzkV06VSNSOaJqpTzLXcBOKE6gf9jH41bYs0Z8mKQqZEiTp6GPyoWdxJLiNuD4kPaRi0yOvrv50JKzsZ5LXQTdse0F3D92lnKM4cl4zEQQIAOnPcg1qwlCNVvNwMeKqyp2txOe4nEs7F3Ysx1JJkmuvGCirR0RzZScndg5enQrK3apsRGk7K4xcQyYLE3CFIIw9zQ9y+pC6/YY6RO8RyjNWil24+ZakqkckvIz/ABXANadlYEEMQQeTA6iracropT1cXuhj2W4sLTd1lJNxlgiNOX8vrWPF0XPtp7I34Wqodl8WbM3K5h0jN9tDNu2f2j+Brf0f7b8DFjvYXiKOymKFvF2XMwGI081ZfzrZjFehJfe5iw371Gvv3iWYnmSa4yR2wjAYmFOvP8hQaAwW5w0Wzmtg5VOq+XVR+VMpX0ZErO6DEt9Dv+FI0XKVwhbXU1CNmQ4oty7eYJIEwzchy+O1aoWjEzSzTlZbDjgPD5uWrPIsAT5AZj9AarnJJOTHfZhZHVTbB72fd8J+AET6gAH4CvJzqylJS738QJWRUbyo8FgrHqdH02nzGoO+2/ipbNr70Cj6zxNBcCnZ5AJ+8NCrfdcfJhsdKMoScb8vv3ehFuB9psLmtC5EtbJB6lZif81bOjquWpk4P1Hg8sk/IxzspysoGjQRp9o6zGxnWefxruGjTdErWHhQDoY19Tr+dS5FtYs4C8Z7f3Dp6N4o+E0JrUz20M/7R2JFubZyqT+sBO7EzbIG2ymflzrZgmk3r5GHGRemnmY/NXWRyyJNEBEmoAirlSGUwwIII5Eagj40LX3GTtsa7tbikxRXEJob9pGcfdurNtlGm0oD5hgedZoLLdchKzUaqlzMaRWlFjNLwvtIFRUuKfCAAw1kARqOtc6tg5Zrw4m+ji42tMu7aXrZt2O7cPnAcx9mVEBvPxfSpgYNTlfwJjJpwVjOcPaLts/tr+IrdXV6cvAxUXapHxNtiNRXER3iOHttGnWiyPUcl9YjQ1UAFtcMI8KXWVNYBCmB0B3j50+cFgscPBIzXXIHIFV+ZUTQzksHpgbUQAF0PTqDPmZE0MzCLP8AdsUjN7syD5EZT8pIoVVnpSS3sySV0OMV2hckPYhiEd8h3IUO8CNzAIjmUI0nXk0MFnbhLR/f35lcpW1J4XAXMS9o5GFt1HduMrBRP3vduKpLQOYJjStmHwjhJxl9/wB+IrnpdAGC4ffSxde5Oe20XkaNSHCoyZfd8JO+vh3giLMXhqajmjoxac29x9xfjai2QW0IcE9JbIJ6aDNXJwVFusny+hoW6ENy2t1AQ081YcjyNdzVM1aSQKcV3SG422sKfvSRE89efSja7sDZXPezV8d295jJeSvVsuhPpmIFGotbGZSuYjtVxjvruUNKoTsTBaTJA2ge6D5HrXRwlHKsz3ZzcZWzyyx2Qkz1uMJFbsnShGV3oM42WpMmnEImpYlwrh+IynKdj9D1/ryqua4iVYZlofYrCku+USAMxjoaXrIxtf7+7ltGEqkLrgBkVcK1bciTHzpGrO4yd1Yuw3vrv7y7eo2o1fYfgw0vbXijot3hxiVbQ7BhlPx3rg5jvXDeFKotiIbUyfPaKSd7kuitXkE766EfhRsQ9tI/MiP6mm0IG2wYHXTQf1rShQWq6TFAgtxXcwyu8sZPWDH7I0H8qZXGAOz90Wb9q4xzKhEjfTYx1IGseVFxV78RJwTWh1XgjW+6UWGV7cmCCIAJJy6cxtBig3fUoWisKe2mPRbfdAy7OhcLyE5hmPLMQABufSSKsR+6dwrczfCLeZnuGCuUBT5BnDHz92fQ1Rh6WSN3uy+HMr4vw5EXvbZKMGUkpsQdD4D4Toa1xlwY+UzXGcHefIjOhtxmLrMsrajSNDH+KrYSitSuSlLjoLOMcQNq3Cble6WPsDQx6wfm00cPHrKjb23OX+JblJx5WRn7mCIK2wPFGZjyE8j0AH41shXWtR7bIzcCV22gsuU8ZEAty5Ex5RzqrrpzqJS0XIeMHfyFFp4M1sjKzI1dBoaa0p3KGj6iA8NSwbjbgmIJuQeaEesGfwmsGKjZG7AWU2lxDr3DLZmRz8JGhA8+p/lWeFaUfZNs8NCftAL9nr2XOi51mNN/4efwmtccZB6S0MFTBTj7Op5wPhTvfVWUqFIds4I8II0g7zt86OJrxVN2d76C4ejJ1FdWsb3GK+VlUKBoFAkQukzpAO8RXIVjrC+7auzouTQaB42Efd6QPhRuhbMrscMXZbjqOmb+c1M5Z1YXgsabR7u6CxEQ+4IJ0LEe75z6ii431Qt7aM0VoeW/lVYQskKhZtAATt5TUBx0OfYu9kRmG42nzjrV6Vx5NqNwHhlrUOWKgamCfGZnZTA1ircspyyRV2ynSMc70S3G/wCl3bKh8Pd7hWBX3gsxO8A/PlpVMqbjUcJXzLe2v33GunSjOkqtlladrtrbnptz5AKC8XKPdJW286FiGYiS0tudd966eFwFGvTU3ez5/wBvmcrH4udGo6KUVblf5vvNxwHHqtsI6ssFjnglYJnWB4d/T0rJjcLGE26co25X1Rdhq9Wcf2kJeOXR+4F4q3dM9iZRwGtnffXQ+o26QRWFczXGqr5XuZq5fyIwY+7PyWZH0/5qN+Bzp1mqc6a3vZeDZk7OLlXuNqyvnA/aYZR8BE/CtDVuytmrGWUNUkVcWxslkU6E+I/eO0eg2qU4aXY1OHFjTsoAFZm28X+UfHnpS1H2jTQaVRzlsl6gfEuClgbtlBlk+AamNNuo8quo1/zCdU6kXOK0vsJrblTBn+Vb4TMk4F6uDtVyknsVOLRKmFCuFEi8h8z+BrLivYNeDdqi++BrcRZy6MCrDkdD8jrXNOzdPUZcDvqLcHSWMTz0HWqqidwIPzAKNeX8qQDKnbeoQoYr1j40SAdi7HP6UzRcMbTBkK9Qfrz9aXZgcdAvgeJJLW3nMmUzvodvjoZ9KMuZU+Qv7Q4l1um3lJVlzZp5yfDE/jTw1VyGYxOINyQBC7knqOXnrFWpWA257bEsBbYICZgmRv0nn6j510ujUnXb5J+qMOMk1Qtza9GHMuVAOb+I+gMAem5rZRSq4qc7aQ0XjxfjwKq7dHB06fGfaf8AtXsrwe/ia72ccFS/cZnHgQSeXoJG0mTp93zrD0nUzVeqWyWq72X4NOjh+tXtSdk+UVy5Xfob3tHwKxewd62iIhyMUdAAUdQSrBl1BB8+vWsMLRaYHOTd23c412fxN3FYK5cutnNh1ymNcpEvJH90/wB3zoY6lGnUtELU61Ft7p6MzPF+JTmAM5xBnQqwbWfUEjzquENbszazlmlv66CEtV5YRNQIfZxPgW0p0OrnylifoTVbjq2I76s12A4hhXVF7xrDZZPeAQT5RtJ11Pw6L1c1eyvbkbqFemoqF7eIk7TshfIGS4ynVl/DNz+EitWGhLe2hRjKsHonr98RGtsDWtqilqc9yb0H/YzhdjF4kYe9eNrOpyOIPjEEKQeRXNzGoFSpNpXiNSp5nZnWeHeyW3ZJHfm4rgTKhWR1Jy3EYEgwCylTuGOsgViq1XUVmaqUOrd0avG9lrd6xYt3YNyyioLoGp8GQ/A7xOhANVWLMz1FXafsGl+0DZIt3VRAF+w+RcoBjVdBlzDlyoOOtx41GtDn3argd7C3BaUu6G33i6GVQZmKvHNYOvQDbalcUWRqXQrTjDaZhtofMfkaR00WZg65j7Y+1Hz/AJVXkYbgVpZO/OmZch1gbRE1W2MCDjS28RcCwz5FGm0gsddddDMelWKDcSjMnJoS37Vy9cYudRJkjQyRHrp+FWpqK0FcW3Ynh+Dlrip47rMQFUczppC78/ID0qZr7DOCSvJ6Gq7YcG/RbeEtFpuEXGdQScpYoAqjaNI0iSp610+jINTc3slr5/2OVjauaOW2708r/UT4/h15TDW2GVFnTYRzG41mQdRzAq/BYilBSzS1lKT9+xMdGVSUcuqjCMfctfizbezvAZrGbMBneIZwAQpMQg8RaWbmBt8ebinevN9/yRozXo048l8W2aztfj1w/D8S6kSlm4qgR72QgCBt19AaqgrySEOX+zm0qcPZm91nuE+gVVP4Gh0g717eBtwS/ZeZl+z3AEv8TFi4pa2QzkdVA2MDntMrBIMyADU5Whcz9VlqOB1FeymCuhkazbJKwWVtSDAkkQc0qpzc2Wd5qh1JrUvjTg9AbFdh8Af1aYdFIGhJmDGUMUmbgGp8RiZMMZoKrLe4XSjskcXbC91iLqZC3dllgyToecqpJ0+6OZ2Fa32kkYKieyAGvZiSTqda6FNxirIyyize+z/s1axFlzeSRduBUOzKttWZmRuUuyKeuUis+Lrum1l3NWGoqaebYT9s+zf6FiBbD5kcZkJiYmIYDmDz5/MC/C4jro3a1RTiKHVSstmdI9mnAgLaMMdbuo29nuFe35rnY5p/h9Krq77F9ODUd7nVbaBQANht/RqgclUIfVCCPjpXuL9woXuC1dtBVBYsW2CqNSSY9NaBFucAxNp7eZWVldZlXBBBjYgiRSmlvS6Fq3nfUOq+Wn5kUdCu7etzWW9TPM7VnNtxhYcyAzaDcaAcviPQ9aXyJ5mY4pgX79u5tyEYeIRAmDlMbf8AatEZLLqZpRee8R7gsHcuMFRSTpJ1hZ5sY0G/yMTVZfKSjudC7MdlHtZiLsOVGZ1AUrIDC2rMGgZSpY5Z1AHlYlYxVarn4DleFyRcbCgYhYXvgyOcswSju2cHKWgHYsfWnzO1uBVZXL7F0IGD/qyCx8WnhzQCDsQFKjy0FZ5p3L4NWKbOX9ISQMz6FdtVBMn70EaE75vIVIPWwJp2uY/2z8QCYUgMQb9wW1AjUW57xzz/APj/ALx8o3YWGap4amabtEV9gLYOAtggEMbs+mdhWXGv9vLy9EdPB/uV5+oXwrgdu3iluDV2W7btkn3ZXNOg97znY7a1mc3awZxzSv5DzhmCvpi8TevMWtuwSwFAhUzudgdPCUBJAMIBrlFCpUctPcV0oZdSOHwuKOOvMxjDZUyLrrczWTn1MSFFwaRpIMyKManYcWgSp9tSRl8Bwe3bu3r+rG+7upgLC5jAGXToZ0n1mY53SLKVLLJt7s5z2xxi3MU4UAKhyCANSPeJjc5pE+QrpYeFoK/E5+Kneo7bLQd9jO2P6Lbu97NwqltLCABRo1wkEgQNWBLHxGOcUtfCupJW8wUcQoRdzOcV4ncxN1r11szt8gOSqOSjp+etbqdONOKjEyTqSqNtnWfZlfVMGr2kVXlgx0JYiSXYnlAaNIGWOU1mqys3mNtK2RWNfg+PaZ7rEwYA6kkgQvI6GZmMrbR4qN9RmncutdqFdgMrEOJWRAYGTpPLKCxZogaxJgC4LMbJdOWQzH+6x+AOn1E9elQBWMwRgRnnUgkKZJEJI0zEEfQUSHEO05wxvFsNnCmcyOGlG5gFtSPI7fgjtwNUbpamaxGBVmmIopiSppserxdR4YbPzXKSfl0qjIaetXINwVi9eOdSbQiBI1P93kPlQuogd3rsaTh2GFi0SSW3ZieZ/rSkbuyCrhvFe6xa4hhOpzKNZBBWBPkfpVnCwzjmVjX8O7aWrBOZy1swdmzAgBY23yhR0MbiaeM9NTLLDzvaKNtwzilnEIHs3FuL5HUeTDdT5GnTTKZwlB5ZKzLMdhRcQqfhz5EHToQSD5E1GrgTsZ27wk2rqN3qgKpaTpkUKQzmdABP0UbSaRQtK47qXjlOJe0HtCuMxU2v93sr3VnzUbvrr4j9AtdnDUskdd2Y6krsddmeK93hLKquYg3OZEeNjy9etcrGQvXl5eiOxgv3K8/UP/8AEzhkuQAEIJUEwwA2P1g8prN1a2NEopjnEcUsY0o9tmFxFYNbNw22A0Ob3lDAa+LlPKapWmiZIZYN9Yj2/wBqrFmyMOl1r1zLla5mLQTuc7e+ROkaabiio5ncrytkMPi1dAUOm0QBl3OWB6/WaLVtB4qxxLFk97cncO/+I12KO3kjhV934s8FaEZmHcK4XfxD93YtPdeJIUbDqSdFHqak5KKGhByehuOyl+9w/wDU38K1tr11Abl0EIBBXcDxgZjIEaTrtFU4dbdp7LzNVK8FZo6Viuzy3sI0D9Y6AiDGVszMQp1j3sv90HesMWsyvsaJptO24HwvsY1jDIqsDcCgP72V8pGRmVjqwXMTtJgbUZyWa62FhF21COEdoS90oB+pIRrbk721zS3ViXBLHT3SNZWZuAo7XdpVtLdsudblpojSGa3cgyNiHQKD1qXGhFs5DfvM7M7HMzEsx6kmSdPOlNHgetYYcv62oZkSzHcsSCInmQf6nn86S6Lbof4K6QASo+f/AE1S0Bg/HuJHKtuBqZOvTbl1/CmhHiFIRvf12/71ZYdBGHuIfFcgAHQEbnmY6AH60vVVKl1BXtqzZQqUqVp1ZJX0V+fEXcRbNezWS1rLp3iEqSeeXKRptrXW6Lwl6TlNb8+RyOm8WpVlCD9n1f0+ofgeMcQzKq4+9Ak+JyfLUmZ1I3qzpDD06NK8Vq2kjJ0d+2q9v2Um34L9TVe0q4W4TnS8SxuWUxDE63VAaF00y5mDwIHvedZMLbrFclT2TjaiuqZRjw5S7WrZJyF9RMTz5a7KfnXIx7yyk+5GrrJQw91wubL9EtkbaEdTz+NcXrZ33Oc8ZiL6zYovcEtoTlJg6wddRJ/KhOq5WTO50Hd06km9Fb0b+QRguAqhkuzH4fnNWde1skjjRx9ZSz3v46jbA3hZkSSpIk8xOg286Majm9To4PpGdWooTS14ow3avhQt3Wuh0IuuxCLuNASTy94murhZ37PJBxlLK83NgXAeE3MVft2LQ8TnfkqjUu3kBr9OdbHKyuYYwzOx+k+zHZ+zgrC2bK+bufeuNzZj+WwGgqnfVm2KSVkG8T4dbxFp7N1QyOII/MdCDqDUvZ3QWrnO/Zf2zY5sJiSTkYhL4ByEjQq7bKSfECTrmPlNNWlbtLjw5DQnfRmq4p2swaKyPi0O4Pdy7RzU5JCmJEyPQVQWWbOPcU7Rs917lhSiZlCCAqqlsyinqB7xGxaTrTat3YUko6IU8Qx1/FOrXM7lUVCyhtQsxIH2jzJid4qNpAUG9AwoUEFRcUjTuzJVujdfU6elV3uX5baBX+0SdrTjyIjWky94+buJpwhAc1ssh6qxqZ3xB1K4EsXmsgMl9y52DHMI6xTR7W6FlBx2Yp/2reBm6M3Vhv61blXArVScfaGdvFKVzzI5Uii27Lc0Z0o5uBHEqWgHQaababyemYyY6EfDr9H0W4OL2vr/AKny8Fx5vuOd0jWSlGS3ssq2svzP/VJ6rkrX1seiu0cYfdlMHnuA7c9p0WP8xX+E15/pSrnrKmv4Vfzf6HbwcOqwkqj3m7Lwjv8AHQ89snZ4YdsPdFwEOGTIEywV8ReQSJOaD6Chgnq1Yy1trnO1FdIoHvZyyD4ipJXvCCPskLbEjqYY1wulW1O1+C9WWVm1hVr/ABNfCJo8Hc8CZiMzCfnJHppXGluYXSlLNKKbS3fBEL2rfIf1/FVb9pHo+i1l6Nqy/wB3wjYKmnPLAbXc0jWcw+jBR6AkfjVsFaSNuEuq8LfdzNduW/WW16KT8zH+Wutglo2dTpB6xR0v2O9nRYwxxVwDPfEifs2RqP4ve9MvStEndlNOOVG/4W5Nm0W94ohM7zlG/nSx2LAHtTeu9w1uwR391WW3qBBgy0nmBoP2mWdJNG6ukyMX9i+ydnBWUtaPdAzXDyzGNh0EACdYWmlPMwJWRgPbSyDE21tgK7Wy10jTOWOVAfPwtJ3iJ5Vnmlcui5ZWuBgCVB0VnVdBroCN4HrSWD4bGi4NhC6FA7LAGZCBPU676z9RVE5WZpgnaxBeGC6SWTJ3Zy5APiDmnb5VM1iRgnqwj9BUfYb5f61MxZZLgeXcXkUk+g8zUUbuxJSUVcTXcQzHMxkmr0rKxlcne7JqmnrQbHUboL4VgQil21APhUmRPT5an5c63QoyTVJe3JXb/LH6v75maEoqMq8tYRdkvzz4eS3YQTrJ1J3ru04RpxUIqyRxqlSVSTnN3b3LLFouwUc+fQcz8qpxeIVCk5vy8eBfg8LLE1o0lx37lxZ0PsvgQuTSMxX4LOg/P4+VeXjd3lLd6s7GMrRnNRh7MdEee3XCFsHZuD/9d4A+jow/xBa24N/tLdxgq+ycTrqmY0/ZgEWbj+Zj4KPz/CvOdKNOul3IrqycnCn3+unyHNnKPtAnrNcsfFPET0cHGK2jZpL6vm3qyl2BaeUzPxXX6VW/aPRYSlNdFONndxm7cd/oE3LU67HkasPL4fFOknFpSi94vZ/R8mge2W7tifeBc6dQxP5U6dpIbNTjiIuF8t1vvbvFPGuFnE8Qw1j/AN0KCR90M7MR/cBNdfCu0GdjGRvUj4Hc8Vh5sm2gAEBY2GTQMoPLwSB8KvewgN2a7UYXHLmw9wEgSyHR19V6eYkedNZrcCaDcWyrcDsNEt3GJ6RlAjzhnpHuQvwVnKoB946serHUn57eQFFLQh+eOJ8Q77FXbt9j3gdkC7hVXwgfTU9aqqxaenFF2HnCzcuDFFtpEHcE/KfrSoKkmjS9lr5BJYakwD6Rp8orNVRfSfMdYrh5abiXCjEaxsfUf6UidtGM073QJ/4et/aZieZJ/nRzsXIuJl+IXizkcgdPzrTBWRVUbbK0WmZEhtgMIYXmz+4Oi/ePrr8AetXYZRWatU9mHxlwX3xsGtGby0aft1Nu6PF+fonzCcSwnKvuroPPq3xP5V18DSkoOrU9qer+SOZ0jWjKao0vYhou98X5soWtyOexz2ewuZhP2yQP3V336nT0Fed6TrdbW6tbR9f0+p6DBQ/D4R1f4qmi7ord+f0Oj8CtfrU9Z+WtYzMZb27cScDD4YCEbNdJncr4QsbwMxOu8joa3YGKcnLkU1npY5LbtliFG7EAep0rfVmoQcnwVzObY4Q20C2gCAIKke91M9a8fKo5ycpPVmVVHmzceD5CSxYxDszqXRTmKjMeWwgnrpMVdKNJJLS+nA6z6RrUkkqjvpfW/qXjAYgMrlmzBDJ7y3ocpbJ3eWSZAHnoelWKnQcLaWL49JVcyqZ9bd3oDXsbiLYzNb0iSSg033KxFVRw9OT0fxGj0pUqO0lB+KG3DRdZVc/a8QWYAnXXm2+1VTSi2ji4qcZVZNRS7l8jXdiuGq1/vzvYRrS9PEVPzCAfxmung7uOY6sKvW04ye9tTW9qMcbOCxFwbi2wX95vCv1IralmaXMjdkcH4VgWuX7SWme3cd1RXtkqy5iFJBG0DX0FdCuo5G2UR3Or+03jQwllLNhsl+6VOf3itu2wMnNMy8CDv4ulYKNJTnlZbN2Rz2/7QeJrl/tcx/8AFa19fBV88PGLsUyqtK5lUus9wsZLOWLbakyTVGJhaKfkHCzbm1zJ3bni8QywVkeRn+W9ZDZLfUdcA4hatuynMSYjTNrzyx5R8qpqxbRdSkk7GiPGrYA1ZpBOg90bSRuKpyMtzIKGOVtQykdaWzDdHPO8reZLhmCt52jlufStGFodbUSey1ZViK/Vwdt+BobXhQtzPgXyAEEj0ECtc6MZ144ePsxvOXi3ovvh4EpVpUsNLFS9qSUIdySs398fEEauuzio9VDoBuYA9ToKSrUVKm5vgiylTdWooLdu3vNrwfChQhG2bKP3Qrr/AIp+deRp3fae71PQ4+S6zq47RSS8jcdnLPiLfdEfE/6A05hOd+3fDRewtz71u4n8LKw/xn5V0MC/aXgUVlsznvAwO/QmIEnX00jqZip0nUy4drnoJToTr3hC17cXb1NjcxAjQ+I6AHTU6c+VeYjqZqmDr0X+1g0vDT37E0tkDSNgPQDlRbuZ27lQcj3gZzctfs+QFG3INr7fepcRPLyI6igDYGwDgW1UnVRlI5gjTUCjUazNmtYSviJt0oN31vbT37Gt7BY1WN62pnKVY6jSRljT92ungJPK1Y30sPKhDLNq/JO9vG2gH7XuIMtuxYBhbhZ388mXKPSWn1UV1sNG878gVHoZL2fWc/EcMJiGLeuVGaPjEfGtGJf7NiQ9oYe1e5PEGE+7btj00LfmKqwkFrLyGqS4HO8Xelyp5VJTvUaZnqrQ8svDA9DQqRzRaEpTyTUg/wDR2Lk3BI5GNfLT0rlHWs27sHtWHBXopmZjT8fjReqFV00avDcFAX/zG1AIjTWPqPWszma1EnY4dlnxtqZ0AA5cqjmTIZFk5VrMhoeEYfLbBjxNr/If11rvYKmqVHPLjq/A5WIk6tXLHwXiH4s65eSDL8eZ+c/Kk6Pg3B1pbzd/Lgaek5pVFQj7NNZfP+J+/wBAVtwPU/Af6kVue6Ocg/h1vxgxOUFo6wIA+ZFczpeploZF/E0vmdXoWCeIdR7QTfyNzYs5bYH3Mp/hIJP0NcVKxZKTk7vibXgNuLU9SfppUFMF7d7f9mwzcxfK/O25/wAorZgn+0fgVVfZOSnBEW1eD4pO2y6QT66/AVTjMSp1Miei9SYjB1I4eM8rd3fbZcL+Ib2fuE3lGYx4jE6HQ8v62rn14pRvYwdfVdNwcnbld23XA1VwsPdUH4x+VYzOrAiXHLmbRAGvvDnA66+6fnTNK25Y0lHRhoPlH9eVIVGU7QZu/ZQSQwU5QT0A2+FbKOXJmZqjOtOCpQba5K/Pkab2Xpdt4oyhyXEIb9mPEGI5DQjX71acPWi52jr38EdKhga9CLnVWW+ye78j72rYsPi7agghLQ1BnVmckfILXbwq0b+/vUWpuU+yy1m4jbP3UuN/y5f81HFewvH6gp7k/apZy8Rcz76Wm9NMkH+GfjUwnsPxJU3Oe8VtCVYbtIPwjWss5N1pIlSKUIvxKhWkwjfBX8yiZJAiegG30rl1oZZtHYw9TPBBWFw7XGCosjm06DzqlvKi1auyNPZMkrBEaCZ1HWszRouXHBeVAlznWAwztdUcidfTc/SunQp9ZUUeZzKsnCDkbXD6NPJQW+Q0+sV2ukG+pyR3k1H3/oZujEuv6yW0E5PyWnxsDVrjFRSitkYZScm5PdlVnW437IUfPU/lQXtMj0iHXMT3Nk3efeWh8FYOR8hXD6UbniIQXBX83/ZHc6OShgqlTm0vJa/NnRVtZlI+8CPmIrnlRrOAXM2GtN95Z+ZJqEMj7XsIt3D2LZMfrwx/dW3cDH/mA/vCj1zparfY0YXDfiKii9t34L7sZLsbw+3ir93ODlVAFCkrGsDbyB+Zpsfho0aFOLSu7t/Ato46dbEznBtRVkl3cNAbtJwT9CvLccm5ZfNkbIJttIOQkanwzB5wfjzlBSjamrPjr9SjpFVq0Ulrr3Ly7yQsfs3Plcqmz+7HJeCxP5PQFd1Vtc8GFBlt5OkTPOnVOdhvwWIy+z6BBQbeMHpLT8jrVdnyKHh697ZH7v0PuA8KGLxWVHZbaKrXTrLa6KC2uo09AauyJRvNeB2+jpYilBwd0r3NlxG5YwCaWyVuCAij3nEnU7CQdSfu8624KV7xLMTupHLe015rl9rptrbV8uVU1UQoETA10nYV3MM7Ryvcwz3uNvZjiu74hb0JzpcTT93PMc/cqYv2L95Ke4x9qvDyL64kSVuhgdtBb7tQ3WDP0nnVWFrKPZY0431RzbH4kMMmUAqTDdNeVVTpPrXO/EWddOCp5dgQOOtXqaMjgx3wDCsxIA94gD6/z+lYMZNZl3HRwMGotvibvC4dbaBQNvqeprmOV2dFKxK5BHMGaiIyvPUAY/s1hCzORqUWY56mJ+A/GuvhK8aVaLnondXMNXDTrUZKGrVnbnqPUHgc9Sqj/EfwFdOu8+Lpw5Jy+S+Jkw66vBVp/mcYr1fwKAtdA5pHhGDuurOtm64ZyZS27DlpKiJrn/jqUZNO+/I6n/i6soxeaC0T1kk9dSPaN/7KqEEMLrZgwIIIEQQdQdRXLdRVcbmW2lvI6VWg8N0fGnKzd29Hda3N52L4gL+EttMsoyP+8sCfiIPxqmtDJUaMEHeKZuuzZiyU+47j4Mc4+WaPhVQxzf2kcUL33UHRP1S/DVz/ABeE/uCrsFS67Eq+0dfobZz/AA+Acl7U3ZeHH5/AQ9lu0IwbXCUzC4FEztlLco1mfpzrodK4WVaClF+zf7+By8DWjTk0+Ng3t9xtb1kLaLZSc75hGv2Rr011H7O8VwaEddTrTWh0SxgbRCnu11AO3WsrLczOYccgIGjZ5+GprXDewH7J0r/Ytk7Bh/erIPnZkOz+NFh3V9LZA8QUk5lGk5SCVgn4x51dJXRXa6uU9o+0C4kIiKcqHNmY6t4Y92NN5rfg8PKDcpGSvUUkkhMbYYQQCDyNdAzkMFhFt3O8QFGWMrBmBBgyQZ6GKjbkrSegLWDeLPcxCPnuF3ZCoZo0EGBoBAk0qgktAu7OYOhDEMCGBIIPWmiuJjk3fUP4XhM5kjwj6npVOIrZVlW5pwmHzvNLZG74Hgwq94REiFEbDrXJqSu7HXQWXkwuw0PyH5Ulhi5rcgTREuVNb/aiiS5ksNw28ri5bbuiD6+vh2IPSavck1Z6lUM8JZoOzNM9s3U8IUODmZRpmMRmHkauwWKWHrZp3atbwW5rxmG/G4e1Kyknma2u7W+/iLb6FQZBBAO4PSvRxxVGcbqa955aeExEJZZQfuZ1L2N/+nD/AIjz8lrztR3m2ubO5jFZwT3yR9DkvbS4zY7EKxlRevGI55iJn0VflS03llmW50HFVXRpz1WT6/RHR27FfoGEvXrWJueFTcyBUCkwN5BPTYimqSc3dsxYapTqTjT6uKu0tM3HzGXZHh17EWDe/TL9vNcuDKgtx4WKD3kJ2FVpXLMROnRnkVOL0WrvxSfPvOWcZuN3txWYsUuXFzHdjnMsY5k610MHF08PKot5SS8rpfNhxeSri6VFrsqDlbhfK38ka3tV2ATB4Y4lbz3CjW/CyqAczKNx0mazVcRUlFxcn8PoJg1Rq1lHqorfVZr6Jvi36F3ZvsGmOwiX3xFxc+aVyqQMrsu+/KfjWaMeJficTClUlT6tNLnf6h/EHvYZxgzeYkthxauwoY23IttyjMreWxFUSppSL6ChUh1qjsnda2uldd+qFfbvsgMJhhcGIuXJdUysFA2JnwieVXZUncrwlaGIn1bglpwv9TVcD7P3L2Hs3f07EDvLaNAFqBKgwJSdKVUYtXKq2LjTqSgqadm1x4eZS3s2U74y9r+yn8qbqkV/j4/5cf5vqYrtN2bGDxVjDrdZxdCSxABXM+TQDTTetKqS2uXUIUa1KdR00svDWz0b117jYf8A4vT/APru/wAKfyodZLmZPxNP/Kj/ADf9ijHezVUtO36VdOVWaMqawCY251OslzJ+Jp/5Uf5vqIewvZ/9PW4zX3t92UjKFM5lnXMKPWz5mzGwpYaSioJ3vvfm1wY4xfscsOxY4hyx3JRdT10ih1kuZhdek/8A4Yfzf9jDdreyV3hZBgXLTHR1BEkakMpJIaNYkyAddIquV5O7NNPqp03KjHK46uO+nNPu7wvhvGrV5fCw8xI0nl51klBpgjJSV0GCeUdTSjAmJ4oqbnMfurLGPQbCnUWK2gP9Pvv4ktoFO2ZtfjAIo5UBZnsVYfGK8xrB6UzVhU0wpW1B2IkgydJ3OlAeLcXdEONcWu21ABQhgQcw1100yxr8OVBU0zS8dViuB032Pn+wTtN1/wAFrRDYx9Iycqqb/LH0FHG/ZW9+/dvDFKveO7AG2TlzEmPfE70y0Y8MfGMY9jtJWTv8rGy7ZLHD8QOllh9KDM2D/wDYh4r1BPZx/uQ/4t//AO16kdizpD9+/CP9KOYcS4SzC/dyqQMS6zJmTeyxttr1pM1RaKWnLvOxGrh3UhGUO1k3stsu199jpPtP/wDTbn71n/7EppbHI6N/9heEv6WC9lcS1rgYu2/ft277r5lWuNGvWIqR2DjYqWMlHmwrthhFv2sNi7eptXLVwHraZlzfLwt/dpai0uNgarhKVJ/xJrztp9AP2wn+wr/xU/wvRlwF6Odqkmvyv0EPZ6zksYG6ty6C960hU3GyZSzAgJOUbCs7k87RtjU62E8yWzey3NX7TnIwYysVm9aEgkGCYOorRPYw9HJOtquD+COTYJf19kkk/rrcFiTpnHWtOVZE/Avo4mc+sg0ksstklw7jtfa7gz4ux3Vu53TZlbNqdBOmhB51UnY59CpGnNSlG65HNO1fYu/hcM198VnVSgygOJzMF5uRz6VHJnWoYmjWqKmqaV+PZff+Uc+xJpt4k/tW/wDCwoyVnZfehixc5Tp0pS3cX/Uxhj+ymMfiH6Qt4JZ7xH0uNOVQsrkAymSDuedRvQMMRRjQcHG8rPgt+d99ORR7aMagwtu0SM7XMwHMKqsC3pJA+NIw9HRbnKXBRlf3HIeE8OViWdTlIhTMazuBP19aWo+CJTp31YzwbX2XI90BZjMBLMPU+79aqaQ6hJ7l9vDJbM2xEgTqdYO8nnQ33HUVHY9JUfeG209PKjYOUQXMR3dwsNiNQCB8RymmtdGWTsyF0OWDfrCpVZIB8fPUL6xRF4kb4YZSEYLInMIHOInX5VER9x3T2QNOAJ/+W5+C08dh8f8AvI/7Y+hzHtl2kxicQv2lxN9U727AW665QC0ABTAGlThc1U6dK9Om4LtRu3rfj9DtHbN44diSf/Zf6rFMzDgv/Yp/7l6g3YIZLN2wdGs37ysPVi6n4qwNLEbHazU+DireSSfuaFd/gWLLPhhbT9HfFDEd9nEqmdbpTu4ktmG+2tRpmlYihZVbvMoZbW42te/KxL2u45EwPdloa46ZQN4Vg7H0AHzIqS2KejV+2zcEm37mvmW9jQG4KByNq+D/ABXAfrUjsLjnbFTfeeezTiAxGAFl4LWh3Z80Kyhj9wx/doLVNF/SdLqsRnXHXz4/E89qlpWwtpHbKGvKJ0+5cMa6AmIBOknWhO6jcz4OTjKbSv2ZaeRzXhvH8l63bvoVs2rqMqDe0UO2urTrM89fKqXD+Jav1ORh+lqlKrJVFpJNeBvPaX2hw7YW2qvnLslxQp3C66nkJozqZ+zDf0/XuNixqwl6m7aaXfdb+Biez2JN91N+Agu2+6YCCLmZSLSKPeUjcfZ96dYa6n2dEUdF4jEVJzdrpxlfu04HW+2eExN3D5cIxW7nUyGyeHWdflViZsoOmpp1Fdffgc84j2V4zdQ27jNcUwSrX1I0MiQY5iaj+/ux044nBweaCs+eV/8Aca+xBf1OJP7aCPRT/P6VHK7Zmx1NU4Uor8r/AKmw7hHaW8OMYjCXnJtMYsqQBlYKrQCBJkZt55Ul9QSwv+FjWjvx8LtfC3xM37V+A93ilxUE270BpkhbijQehGoHUN1qSL8HPrKMqXFa+K4+7f8AsZIXNNB8qqGuVi8VnQ/1H+tQXMXvcIHhEmNB/wB6BG+R9A56nqSR9ByqAuKMPdVW/wDKEHzkj5imZQnpsE4HFTcgqGmdAB4fjp9ajWgFLUJ4uV7xQyqFA0MTM7/LT50I7DS31H3ZrtJjMNbNrDKDbDEz3TP4jAiQR5UHWjDRtLxZ0pYWjVtKo2nZce7wZkeNYhnxLXLgGd2ctyhpJPhmRVsXeN0VyWTE04x2SsvDX9TX4vtdj71s2cQMth8qu3clYUkahiI6UnXQbsmr+KLKeDoU5KcHdpq2q39xve1xSxdtYi1dNrEv4cqqX79QrGGsggvB0zSMs707dtTn4TNUi6co3guN7ZfB9/LW4OO1nEMs/olmf+L/AJPyzVn/ABtG9sy95f8A+PoX9t/8fn+hzbt1xFrl03L5a4+VAVyNaFvfwhST4RvmkzNXXzaoarHqqeWMbRvve9/F/Kysev2r4hZwJt2ZSwFcZhb2ljm8ZEbkiaCqRvkur+I+Nw9JqVVvtePHwt8xNw/j16w8WeIm3+rCs8IAMgUwAQTcUZnVYGYlelFXvojl1a86itOV9b+8nxztJdxFmwl7ibXM6l3RkRhbbxBR+pBIJUxHqTEgUby5CQk4Xyvu8irBXnuWC97XKctq5sboBgqRzCj7fL3dY0TaVl5933yOZ0jTp5cz9r1++Z5YgsockLsT0H5f1oaM7pPKtTk08spJTehVjMZdW5mu3hh7lk/2dFAKqpVnzAndCy2/HrmLk8iKkXaPZ1+/vQ9PRl1atTdla2nJjyz21xc3c/F2ULazqFFhjmMQkgQ7ROiTEiSNYbNPggWRXwf2g8SN0BMa2JJUkp3QOXbkEBPqNKZyyq8tF3mjDUadSplm9PG3yY17D8fxOFLpYUMrlc022eG1APhZYnzPKq5VVHWTSOzWw1Oqo9ZwWmttPcw7j5usWx5OW/bu2c65cuXSEZRmYmcsFZOhmopKXaTEilBxoxV4NSvrw3fDgBcd7U8Rv2mtX0m0YJ/UkRBkHNHhINBV4S0Ul70NSwdClNTg3fx//ImwOMzAgASuh89NDUasZpy7ckuDCLl0Rrp576flQFvzPLeUkCDCgafhPyqMGly9ivp8aA2hk1uQwWI9GB/A7VYYlLgELicjhvKNI6HrUC9HcNHEEdCt0kGWgb77EMBy2oWs9CXurM13YO9/Z2Ourzr+4m9cHpZ2qrw+bO1GN4x8F6GJ4/bnFXG6Pc1+L/zrt4R/sIeCK3Tl18KltEnd/wDL6nQu0VycG48k/wAS15zBS/xUfF/MtjG2V969UMv0jvLt2+3vu7qJ+zbts1tVHQeEsepatfS2Ikpqnwtcro0lGEYLgl72k2/jbwRBsa+rd0TZW6tlruYaXDlHuRJUFgJn4UYdF5qWa/a+Abxvlvra9u7x56XsJu2GCW5bFzZlgT1UnY+kz86q6LxEus6vg/gyzImnF7P14Mv4FC4ID9m4dfMsfxNVY6X+Kfl6IXER0m/EF7J4Fbdo3njxjSQNEE6n139Iq7pOt+1VOPD1ZKkIKTlbRX9+7+S8gvtEllrShwApYfsg6GAzDVVJgE8p+IXoycutduXzKqqkqblTSbs9/AytrAXL179d+rUMtvaADoBbQbRBHkBrz17c6ipw7G9mzxWHwdbF1mpaW38FwQ57R8Dtd2rWwEYQoHJp2BPWedcrA46pKo1LVb+B3Mf0JGVNOgtUtuf6i3h7FbMYgZVS4O4n3++DCVUHe3BOadASI1MHsSs4trkY+hPxClKNuzZ3v8bGs43jhYstdFtWyldDA3YLvB615rBUniKmTNbS56mVO1tDP2e2hn/d0Ho3/RXSfRP+v4fqWdRb+zLewrwb3mE/zUnS7soefyC7SUWuXzYzsXu8xV0N7tsq2XkxyZVbzgNc+OWg8QqeBjZ6vT4u/wABLK1vH3Xv9Bd264k2TulBIjO8cgDp6iQT/dqdFUbvrZeC+YlSXVxc1utvH9N/cYLhzTcnOVEAErHMnXXeu9PVHEg+1cc4bEqE1cu2sACSRMAQNNapZpjOy5krHDLu4uQx1C8hP2c28UHNEyy5jAcJuHe4s/uk/WdaGZEafMz44a4MArE+9EmPT/WnzFKi0VXrDW2ytqN8wUx8eh+NFaku4vUhecR5z7pEH0g1CORs+yWIAst5tI/hWvOdMJ9dG35fmz0NCGaCfcvRFuJ47hwxDJJBMnKp/EzSUuj8XKClF6PvYHl4r0+pfxnGA2HywZy6HzYf15VV0epLFRv3+jLJw0T716ovweLOTxDK2a6SszBN64SJGhgyPhV3TEW66t+VerBSg2vd/TEdNiF/2bd8Q1xgI8x+kWztXo6X7teCOU1/jF/sf9LM/wAaxIa0wnmv+IV5joxNYlX7zruDSuVcPxA/RQu3hYfOdabGL/G67XXoiqtBulNpcyfGcaq2sifahFHRdv8ADpSYaMq1eVSWyvJ/ITEQy08r5Nvy+rsvMH7U3g1gga6j8DV3Q6fXu/L5otrQyQfg/RiPA4lj3WZicjrlBJ8IDAwOgrp4hNVZy4ZX6HnsHSqxxkpTi0stldO2ttEaTjmJBtgb+ND8mBrk9Ep9f5M9JODS9/ozPdosUXu4c58yqHETMap+VeiirQkjkU6U4zd012ZGuxGMXIxPiAE5YktqAABzMkV5PC0KtaeWDs7eHodarCy1V/vvM5xXi1lka2LRR9N1UEQQY0M7V2sLgcTSqqdSV1rxfLvRTDImmkl/x+TLeyl3Kbk/s/5qq6aTtC3f8g4WLdOPh82HYjtEFu93kJEgZp6xrEefWslPo2dSj1qlwbt4FjTV9Nvvl8z3jrI4RifErKo1jMrMAUJ6QSddtetaeiK83J0pbWuu4FSlaLXBp++10/gYDiGFeyTIyu050IjKynYcudehjyZ5qWizLiPuydm7eYW7am54SRAVRpvqSBt5zSypt6pFkJ5VdmhtqEzZiAVJUgkeEjcEzG9Z2mnZl6kmroEu8XtTvPwNHJImZCtb1MVXL1ueVQNyGMuGBlUMw1E8vOikuIJPkBWcYyyIgkydI19KyYrC9bK65HqcBOmqSz34cHyQrxhm6h82J+T/AM63Uo5aajyscjENfjoW/wBX/wBvqNExb3YtiZkb6bEHn6RHPaudRweSop2O3Wq0pUrRvfT+F81fgNeIvcBgtbzA3JGYKZN243ukyB4gfQijisM6s8yXAGCnSjT7V+HBv+FL5GtTE2zw15XU4hXzZCRk762xOcAiMoPOt0WlHKcGcX+MX+1r+VnP8RjWIIOoNYcPhHCpmsehxNSi6fZvfwZ5hsYwAUef896GIwjnUcrfdiUKlKMO1e93wb4k794+8xnLEQZ10NLTpKmurW7T+iOTi8VCeJ6qPFPxstFpzbbfgkeYjFMVIJHLnVmFwzpzvY6uKnScezz4prgyuziIgAD5fnS16NScm9bCQjhXFdZF38G+OncXXccwMEqfQgiq4YOcHeOhpc8PPdP/AIv6FGMaVBhZ1GkeRG3xrdQhJJqb95hxPV3/AGfLk+/9Am1xS4NQYkR8PMGsUMFODvHR+KN05YaatK/uYJjL8lpUFiNwOZHl/Qq5U691eT95TNYbI8qd7PgyOExbJMSZ8vM/lFPi8O6tu4qwlSmm823cr8Xy8i98TqGKgn01H8qzrDVVHJd25XNV8K3e38r+ha99mADSAddR0/7j51rwGDUJuXE5vSGMppZYffC4zbiKNhjZuWw75lKXGCkogjwAkZo0Ok8/KK62RZrnnMnauOOzfD71m4mJuFbFpd2unLmUgggKdSSNvhvQnJWsCpJNWQi7acTs4jEFrCQoEFsoXvGkkuRv0GuuhrLJ3ZIRaWohFljsCaF0PZjBqpIX2zpUIeZqhAbFtnEAA6xJ1A9OpploK9S7A4Syk5kJPU+IfLrW2hVopdvfv2MVenWv2du4b4QlTmslbcc03+akR9a6GSM1aysYc0ovd3HPB+OPYLsyi6zxLuTm02GbXw+Uc96zVcHGWzt5aF1PEuPC5HiXau66nNdW2nRCF/5pzfWjDC0aestfEEq9SeiOY3bwlgokSwHLwyY+kVgnNJuxq6/KrPc0vCO16YfD91asm25966GDE9WjKNeg1j8cc4ys8u/39oyTlJq63KblsONdZ1n85riqcoyutzApSi7rcuxNnNYJjUgHQbnTWu5Tldpnp081NPmrgmCtgINIJ39enwrk4qo5VZX5nnsTOUqsr8xnb7U20tthsRbN63GgEAqd4zSCBzHT8NuFzyh2tuBbRlK2pk2uI+ZCWVTsxGaNZGYDU/Ct6lob411KOWT8xzgMBcFtItuRlBBCsQwjcGNQa2wayo1waSSuNeL8Sa5Ys4d7Solocx75iJIYaHf1LGioq5FFXvuMOxvZHDYi1de4jb5FyOyQQAxIykAnUb6Uk0r6FVWEb2sYe1gzZuMc75gSuujDXZh16jrVD10YacMutw+ziXuMqsxPQ6aeW2xpV2O1Euvc1mGxaWh+osqrx/5tw96w81BAVfWPhUliG9gdW37TFHFcLdvOLhul2OnjJMen3R5CBVaq8x8ltjyxw1VPj8Rn4Urm3sMkMBdYaKABy5VWMZ0A7TzO1XFFi0KY3gwfMUNA2PchkCdx/RmoSxZ3MD8PKo2S1iWYc+dAJ5ZIjNGpLHltOmvpRTa2FaTWp6Wk6GNRrv8AjTObe7uBQS2Rbl0MmemnL86rbtsOCLwCywn9IyMSZU22MamIYabRUuc2rQnndkSXs3ZGrYgt5IhBPxJIoZhFQqP+FjHBtbXQ2DlAAWWBOn3jMDlsPnVPUw5Ib8BLuPFZQMs6gCrrHUWisSOQIf1Wa5qZmAZYnkQZjyqp0oSd2kYK2Dc5uWmopxXBUuHMLhtk7qyloPkybj1FWQjkWVFLwtSOiQL/ALB5d8vPZLn5qB9ae5Fh6j4GpwOKuWUVLd24iroBmMD4HT6UVOS2Z1OrjyDR2jxI0NzMOjKh/wAoputkhepiev2lxIGVSiDqqAR56yPpR66ROpiZa7w5CTq8nWSZk85J3PnS9YxsiJYHBqpzCSeUn8IFCU21YKikMCx3gabj+R9arGK+/nlFG1gkrNyPOgS5Y13yo2JcR2xrTlSCVoBPmMEfGoQ+NyahLnyGoQ8VNNOXKoAsSB1FQJLOKDGR81RBJLNAhNV50CFi2wTMCaILBdAJXlFEhWVE77UyAWZvOgE8zDfpUIeMwioQHeJ1qEKmEbGoEvzGKUBGNaJLlyNUIVuBUIKYpystLflQCeDcfGiAvCCgMfIu1QB4V1qEPmGtQhB6hD1CetSwS2dvWgS567mKliXLrG4qWJcLVagTy6lQgFdGvwooUiGM0SXLkY0Aplq/yoBItbETGtAJSyUUQlHn1qAPiNKhD5hFAh4oqEP/2Q==",
     "preview": "Gon Freecss embarks on a journey to become a Hunter and find his long-lost father, meeting new friends and facing tough challenges along the way. Will he succeed in the grueling Hunter Examination and achieve his goal?",
     "link": "/view/12"},
    {"id": 13,
     "title": "Yu Yu Hakusho: Ghost Files",
     "start_year": 1992,
     "end_year": 1995,
     "summary": "14-year-old Yusuke Urameshi dies while saving a child from traffic, surprising the Spirit World due to his previously bad personality. He discovers that his death was accidental, and he is given a chance to return to life. After being resurrected, Yusuke becomes a Spirit Detective, tasked with solving supernatural cases and protecting the human world. Alongside his friends and allies, Yusuke embarks on various adventures, ranging from investigations to intense fighting tournaments.",
     "genres": ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Romance"],
     "characters": ["Yusuke Urameshi", "Kazuma Kuwabara", "Kurama", "Hiei", "Botan", "Koenma"],
     "writer": "Yoshihiro Togashi",
     "average_rating": 8.5,
     "age_rating": "TV-PG",
     "number_episodes": 112,
     "tags": ["Limbo", "Friend", "Saving the world", "Supervillain", "Flight", "Hand to hand combat", "One on one action", "Teamwork", "Juvenile Delinquency", "Middle school", "Rivalry", "Spiritual power", "Swearing"],
     "image": "data:image/jpeg;base64,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",
     "preview": "Yusuke Urameshi, a teenage delinquent who unexpectedly dies while saving a child, is given a second chance at life as a Spirit Detective. Alongside his newfound allies, Yusuke embarks on thrilling adventures, solving supernatural cases and battling powerful enemies to protect the human world.",
     "link": "/view/13"}
]

def clean_tags(tags):
    return [tag[:-2] if tag.endswith(" x") else tag for tag in tags]

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/search_results/<path:query>', endpoint="search_results")
def search_results(query):
    query = urllib.parse.unquote(query)
    query = ' '.join(''.join(c for c in query if c.isalnum() or c.isspace()).split())
    results = [item for item in items if query.lower() in item["title"].lower() or query.lower() in item["writer"].lower()]

    return render_template('search_results.html', query=query, results=results)

@app.route('/search', methods=['GET'])
def search_redirect():
    query = request.args.get('q', '').strip()

    if not query:
        return render_template('search_results.html', query='', results=None)

    decoded_query = urllib.parse.unquote(query)
    encoded_query = urllib.parse.quote(decoded_query)

    return redirect(f"/search_results/{encoded_query}")

@app.route('/view/<int:item_id>')
def view_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)

    if item:
        item["tags"] = clean_tags(item["tags"])
        if item["tags"]:
            print("tags: ", item["tags"])

    return render_template('view.html', item=item)

def prune_duplicates(lst):
    seen = set()
    unique_list = []
    for d in lst:
        serialized = json.dumps(d, sort_keys=True)
        if serialized not in seen:
            seen.add(serialized)
            unique_list.append(d)
    return unique_list

def highlight_query(text, query):
    if not query or not text:
        return text

    pattern = re.compile(re.escape(query), re.IGNORECASE)
    highlighted_text = pattern.sub(lambda match: f'<span class="highlight">{match.group()}</span>', text)
    return highlighted_text

app.jinja_env.filters['highlight'] = highlight_query

@app.template_filter('trim_x')
def trim_x(value):
    return value[:-2] if value.endswith(" x") else value

app.jinja_env.filters['trim_x'] = trim_x

@app.route("/search_combined")
def search_combined():
    query = request.args.get("q", "").strip()
    
    title_results = items
    preview_results = items
    writer_results = items
    genre_results = items
    tag_results = items

    if query:
        query_lower = query.lower()
        title_results = [item for item in title_results if query_lower in item["title"].lower()]
        preview_results = [item for item in preview_results if query_lower in item["preview"].lower()]
        writer_results = [item for item in writer_results if query_lower in item["writer"].lower()]
        genre_results = [item for item in genre_results if any(query_lower in genre.lower() for genre in item.get("genres", []))]
        tag_results = [item for item in tag_results if any(query_lower in tag.lower() for tag in item.get("tags", []))]

    all_results = title_results + preview_results + writer_results + genre_results + tag_results
    unique_results_list = prune_duplicates(all_results)

    return render_template("search_results.html", unique_results_list=unique_results_list, query=query)

@app.route('/add', methods=['GET'])
def add_item():
    return render_template('add.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    if request.method == "POST":
        if not request.is_json:
            return jsonify({"error": "Invalid request. Expected JSON data."}), 400

        data = request.get_json()
        item.update({
            "title": data["title"].strip(),
            "start_year": int(data["start_year"]),
            "end_year": int(data["end_year"]) if data["end_year"] else None,
            "summary": data["summary"].strip(),
            "writer": data["writer"].strip(),
            "age_rating": data["age_rating"].strip(),
            "number_episodes": int(data["number_episodes"]) if data["number_episodes"] else 0,
            "average_rating": float(data["average_rating"]) if data["average_rating"] else 0,
            "image": data["image"].strip(),
            "characters": data.get("characters", []),
            "genres": data.get("genres", []),
            "tags": data.get("tags", []),
            "preview": data["preview"].strip()
        })

        return jsonify({"message": "Success", "link": f"/view/{item_id}"}), 200

    return render_template("edit.html", item=item)

@app.route('/add', methods=['POST'])
def save_item():
    data = request.get_json()

    required_fields = ["title", "start_year", "summary", "writer", "age_rating", "number_episodes", "average_rating", "image", "preview"]
    for field in required_fields:
        if not data.get(field) or not str(data[field]).strip():
            return jsonify({"error": f"{field.replace('_', ' ').capitalize()} is required."}), 400

    new_id = max([item["id"] for item in items], default=0) + 1

    newCharsList = data.get("characters", [])
    index = newCharsList[0].rfind(" x")
    if index != -1:
        newCharsList[0] = newCharsList[0][:index] + newCharsList[0][index+1:]

    new_item = {
        "id": new_id,
        "title": data["title"].strip(),
        "start_year": int(data["start_year"]),
        "end_year": data.get("end_year"),
        "summary": data["summary"].strip(),
        "genres": data.get("genres", []),
        "characters": newCharsList,
        "writer": data["writer"].strip(),
        "tags": data.get("tags", []),
        "age_rating": data["age_rating"].strip(),
        "number_episodes": int(data["number_episodes"]),
        "average_rating": float(data["average_rating"]),
        "image": data["image"].strip(),
        "preview": data["preview"].strip(),
        "link": f"/view/{new_id}"
    }

    items.append(new_item)
    return jsonify({"message": "Success", "id": new_id, "link": new_item["link"]}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)