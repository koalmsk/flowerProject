from datetime import timedelta, date


class Flower_card:

    def __init__(
            
    self, name: str, photo: str, recomendation: str,
    planted: tuple, how_often_to_water: int, last_water_date: tuple, is_water: bool

                ) -> None:
        
        self.name = name.lower().capitalize().strip()
        self.photo = photo
        self.planted = f"Дата посадки растения: {str(date(*planted))}"
        self.recomendation = recomendation.capitalize().strip().replace(".", "\n")
        self.how_often_to_water = timedelta(days=how_often_to_water)
        self.last_water_date = date(*last_water_date)
        self.is_water = is_water
        
    

        
