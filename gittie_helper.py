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

        self.temperature_degree = temperature_degree

        return temperature_degree



    def set_humidity(self, humidity_value):
        """
        Method sets humidity level to attribute and validate input
        :param humidity_value:
        """
        if humidity_value < 0:
            raise ValueError('Humidity level must be positive number')

        self.humidity_value = humidity_value


        return humidity_value

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
        if 0 < day_number < 365:
            raise ValueError("day_number should be between 0 and 365")
        self.day_number = day_number


    def to_go_or_not_to_go(self):
        """
        Method should calculate if exiting home is safe for gittie
        """
        if 80 < self.temperature_degree < 150:
            print('It\'s not good temperature for gittie')

        if self.humidity_value > 67:
            print('Do not go')

        if self.air_pollution_level > 44:
            print('Do not go')



