class Television:
    """
    Class to make TV objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Function that initializes the TV object and its status
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__tv: bool = False

    def power(self) -> None:
        """
        This Function turns the TV off if it is on and if the TV is on it turns it on
        """
        if not self.__tv:
            self.__tv = True
        else:
            self.__tv = False

    def channel_up(self) -> None:
        """
        This Function flips up the channels once you reach the max channel its starts over form the lowest channel
        """
        if self.__tv:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This Function flips down the channels once you reach the min channel its starts over from the highest channel
        """
        if self.__tv:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Function that turns up the volume by one until it reaches its max volume
        """
        if self.__tv:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Function that turns down the volume until it reaches its min value
        """
        if self.__tv:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Function to return the status of the TV object
        :return: TV Status
        """
        return f'TV status: Is on = {self.__tv}, Channel = {self.__channel}, Volume = {self.__volume}'
