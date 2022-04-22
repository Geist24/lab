from classes import *


class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_power(self):
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_up(self):
        # Checking if channels move when TV is off
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        # Checking if channels move when tv is on and if channels loop as expected when going up
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        # Checking if channels move when TV is off
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        # Checking if channels move when tv is on and if channels loop as expected when going down
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 2, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.tv.channel_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        # Checking to see if volume moves, if the TV is off
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        # Checking to see if volume goes to max and stays there
        self.tv.power()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        # Checking to see if volume moves, if the TV is off
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

        # Checking to see if volume goes to min and stays there
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.tv.volume_down()
        assert self.tv.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
