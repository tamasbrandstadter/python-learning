class Aircraft(object):

    def __init__(self, max_ammo, base_dmg):
        self.__current_ammo = 0
        self.__max_ammo = max_ammo
        self.__base_dmg = base_dmg

    def fight(self):
        dmg = self.__current_ammo * self.__base_dmg
        self.__current_ammo = 0
        return dmg

    def refill(self, missing):
        self.__current_ammo += missing

    def is_priority(self):
        return None

    def get_type(self):
        return 'Regular AirCraft'

    def get_current_ammo(self):
        return self.__current_ammo

    def get_base_dmg(self):
        return self.__base_dmg

    def get_missing_ammo(self):
        return self.__max_ammo - self.__current_ammo


class F16(Aircraft):
    def __init__(self):
        super().__init__(8, 30)

    def get_type(self):
        return 'F16'

    def get_status(self):
        ammo = self.get_current_ammo()
        dmg = self.get_base_dmg()
        return self.get_type() + ', ammo: {}, base dmg: {}, all dmg: {}'.format(ammo, dmg, ammo * dmg)

    def is_priority(self):
        return False


class F35(Aircraft):
    def __init__(self):
        super().__init__(12, 50)

    def get_type(self):
        return 'F35'

    def get_status(self):
        ammo = self.get_current_ammo()
        dmg = self.get_base_dmg()
        return self.get_type() + ', ammo: {}, base dmg: {}, all dmg: {}'.format(ammo, dmg, ammo * dmg)

    def is_priority(self):
        return True
