# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

#https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

twwcu = media.Movie("The Wind Will Carry Us","Abbas Kiarostami","1999","Prefer the present to these fine promises. Even a drum sounds melodious from afar.","http://pxhst.co/avaxhome/2007-06-13/PDVD_042.jpg","https://www.youtube.com/watch?v=xq1gXC3119A")

Lightness = media.Movie("The Unbearable Lightness of Being","Philip Kaufman","1988","During the Prague Spring, Tomas has a sophisticated lover, Sabina, but becomes smitten with a bookish country girl named Tereza, and the two begin a relationship.","https://upload.wikimedia.org/wikipedia/en/e/e3/Unbearable_lightness_of_being_poster.jpg","https://www.youtube.com/watch?v=m1zYYWHFRNw")

Fellowship = media.Movie("The Fellowship of the Ring","Peter Jackson","2001","In a small village in the Shire a young Hobbit named Frodo (Elijah Wood) has been entrusted with an ancient Ring. Now he must embark on an epic quest to the Cracks of Doom in order to destroy it.","https://upload.wikimedia.org/wikipedia/en/a/a5/Fotrcd-cover.jpg","https://www.youtube.com/watch?v=V75dMMIW2B4")

Sonnenschein = media.Movie("Sonnenschein","Istvan Szabo","1999","The film follows a Jewish family living in Hungary through three generations, rising from humble beginnings to positions of wealth and power in the crumbling Austro-Hungarian Empire.","https://upload.wikimedia.org/wikipedia/en/8/8d/Sunshine_1999_poster.jpg","https://www.youtube.com/watch?v=MGoQb2N6dt0")

Trains = media.Movie("Closely Watched Trains","Jiri Menzel","1966","At a village railway station in occupied Czechoslovakia, a bumbling dispatcher's apprentice longs to liberate himself from his virginity.","https://upload.wikimedia.org/wikipedia/en/thumb/8/88/Closelywatchedtrains.jpg/220px-Closelywatchedtrains.jpg","https://www.youtube.com/watch?v=Igc0Jp62kEg")

Green_Ants = media.Movie("Where the Green Ants Dream","Werner Herzog","1984","In the wilds of Australia, aboriginal tribe culture is threatened by a giant corporation that wants to mine in one of the holiest sites.","https://upload.wikimedia.org/wikipedia/en/7/72/Where_the_green_ants_dream_DVD_cover.jpg","https://www.youtube.com/watch?v=dddMp8iknTA")

Fitzcarraldo = media.Movie("Fitzcarraldo","Werner Herzog","1982","A would-be rubber baron Brian Sweeney Fitzgerald, an Irishman known in Peru as Fitzcarraldo, is determined to transport a steamship over a steep hill in order to access a rich rubber territory in the Amazon Basin.","https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Fitzcarraldo.jpg/220px-Fitzcarraldo.jpg","https://www.youtube.com/watch?v=F53yUsgVuL0")

Zelary = media.Movie("Zelary","Ondrej Trojan","2003","A nurse and her surgeon-lover are part of a resistance movement in 1940s Czechoslovakia. When they are discovered, her lover flees and she must find a place to hide. A patient whose life she saved, a man from a remote mountain village where time stopped 150 years ago, agrees to hide her as his wife.","https://upload.wikimedia.org/wikipedia/en/3/3d/Zelary.jpg","https://www.youtube.com/watch?v=UeYkplAeA1o")

Cherry = media.Movie("Taste of Cherry","Abbas Kiarostami","1997","Mr. Badii (Homayoun Ershadi) drives around Tehran in hopes of finding someone willing to burry him after he commits suicide. He has little luck finding an accomplice willing to bury him, suicide is forbidden under Islamic law and this is what puts him in this desperate situation.","https://upload.wikimedia.org/wikipedia/en/f/fc/Tasteofcherryposter.jpg","https://www.youtube.com/watch?v=XDSQLTtGZE0")


movies = [twwcu, Lightness,Fellowship,Sonnenschein,Trains,Green_Ants,Fitzcarraldo,Zelary,Cherry]

fresh_tomatoes.open_movies_page(movies)
