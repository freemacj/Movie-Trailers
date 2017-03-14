import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")

skyfall = media.Movie("Skyfall", "Daniel Craig as James Bond, agent 007", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjG-ovs79TSAhWG5CYKHdn9BJ0QjRwIBQ&url=http%3A%2F%2Fcollider.com%2Fjames-bond-skyfall-uk-poster%2F&psig=AFQjCNGvArHlrIppdBQcllL182jKeRSHTQ&ust=1489542361855143", "https://www.youtube.com/watch?v=6kw1UVovByw")

inception = media.Movie("Inception", "Planting an idea in a person's subconscious, or inception", "http://www.impawards.com/2010/posters/inception.jpg", "https://www.youtube.com/watch?v=66TuSJo4dZM")

movies = [toy_story, avatar, skyfall, inception]

fresh_tomatoes.open_movies_page(movies)