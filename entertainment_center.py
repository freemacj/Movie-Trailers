import fresh_tomatoes
import media

casino_royale = media.Movie("Casino Royal", "Daniel Craig as James Bond, agent 007", "http://www.the007dossier.com/007Dossier/james-bond-007-movie-posters/casino-royale/Casino%20Royale%20Poster%203.jpg", "https://www.youtube.com/watch?v=36mnx8dBbGE")

quantum_of_solace = media.Movie("Quantum of Solace", "Daniel Craig as James Bond, agent 007", "http://www.the007dossier.com/007Dossier/james-bond-007-movie-posters/quantum-of-solace/Quantum%20Of%20Solace%20Poster%203.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")

skyfall = media.Movie("Skyfall", "Daniel Craig as James Bond, agent 007", "http://www.impawards.com/2012/posters/skyfall_ver8.jpg", "https://www.youtube.com/watch?v=6kw1UVovByw")

spectre = media.Movie("Spectre", "Daniel Craig as James Bond, agent 007", "http://www.impawards.com/2015/posters/spectre.jpg", "https://www.youtube.com/watch?v=ashLaclKCik")

movies = [casino_royale, quantum_of_solace, skyfall, spectre]

fresh_tomatoes.open_movies_page(movies)