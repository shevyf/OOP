import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "On an alien world, a soldier fights for the inalienable rights - of aliens.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "162 min",
                     "Sci-fi",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4",
                     "PG-13")

star_trek_beyond = media.Movie("Star Trek Beyond",
                               "At a time of crisis, Kirk faces an enemy not that different to himself.",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BODgzN2E1YjctODg5Yi00YzYwLWJjZjAtNDg2MGE2Y2MyYjBmXkEyXkFqcGdeQXVyNjM1MTQ0NTQ@._V1_SY500_CR0,0,320,500_AL_.jpg",
                               "122 min",
                               "Sci-fi",
                               "https://www.youtube.com/watch?v=XRVD32rnzOw",
                               "PG-13")

the_godfather = media.Movie("The Godfather",
                            "Italian mafiosi struggle to walk the line between dominance and family",
                            "https://movietalkexpress.files.wordpress.com/2015/12/the-godfather.jpeg",
                            "175 min",
                            "Crime, Drama",
                            "https://www.youtube.com/watch?v=sY1S34973zA",
                            "R")

incredibles = media.Movie("The Incredibles",
                        "A superpowered family come out of retirement with a blast!",
                        "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
                        "115 min",
                        "Animation, Action, Adventure",
                        "https://www.youtube.com/watch?v=fwHlyurv-0U",
                        "PG")

flight_of_dragons = media.Movie("The Flight of Dragons",
                                "Drawn into a magical game, a young scientist fights evil with logic!",
                                "http://3.bp.blogspot.com/-dh4w_svq-T0/Ufmf1FhpadI/AAAAAAAEa0A/tt9XUOgkPdA/s1600/TheFlightOfDragons.jpg",
                                "96 min",
                                "Animation, Adventure, Family",
                                "https://www.youtube.com/watch?v=vn9xV6_yyG0",
                                "U")

sanjuro = media.Movie("Sanjuro",
                      "The lone samurai is back.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/7/75/SanjuroPoster.jpg/220px-SanjuroPoster.jpg",
                      "96 min",
                      "Action, Crime, Drama",
                      "https://www.youtube.com/watch?v=ZHIRcbAMFHo",
                      "N/A")

all_movies = [avatar, star_trek_beyond, the_godfather, incredibles, flight_of_dragons, sanjuro]

fresh_tomatoes.open_movies_page(all_movies)
