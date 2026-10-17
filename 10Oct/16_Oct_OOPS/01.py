class Netflix:
    no_of_movies = 4000
    no_of_shows = 2001

    def __init__(obj,country,making_cost, no_of_views):
        obj.country = country
        obj.making_cost = making_cost
        obj.no_of_views = no_of_views

bhopal = Netflix('India',67216321,1612736421763)

print(bhopal.__dict__)
