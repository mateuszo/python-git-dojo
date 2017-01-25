class GittieHelper():

    def __init__(self):
        """
        Initialize attributes with default value
        """
        pass

    def set_temperature(self, temperature_degree):
        """
        Method sets temperature to attribute and validate input
        :param temperature_degree:
        """
        pass

    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:
        """
        pass

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        if air_pollution_level < 0:
            raise ValueError("Air pollution level must be positive number")
        self.air_pollution_level = air_pollution_level

    def set_day_of_the_year(self, day_number):
        """
        Method sets day number from beginning of the year to attribute and validate input
        :param day_number:
        """
        pass

    def get_value(self):
        """
        Method should calculate if exiting home is safe for gittie
        """
        pass
