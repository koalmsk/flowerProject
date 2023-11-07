from datetime import timedelta, date


class Flower_card:

    def __init__(
            
    self, id: int,
    name: str, 
    photo: str, 
    planted: str,
    recomendation: str, 
    how_often_to_water: int, 
    last_water_date: str, 
    next_date: str

                ) -> None:
        self.id = id
        self.name = name
        self.photo = photo
        self.planted = date(*tuple(map(int , planted.split(".")))).strftime("%a %d %b %Y")
        self.recomendation = recomendation.capitalize().strip().replace(".", "\n")
        self.how_often_to_water = timedelta(days=int(how_often_to_water))
        self.last_water_date = date(*tuple(map(int, last_water_date.split("."))))
        self.next_date = date(*tuple(map(int , next_date.split("."))))