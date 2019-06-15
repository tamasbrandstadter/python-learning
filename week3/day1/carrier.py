class Carrier(object):

    def __init__(self, ammo_store=500, hp=50):
        self.__aircrafts_f35 = []
        self.__aircrafts_f16 = []
        self.__ammo_store = ammo_store
        self.__hp = hp

    def add(self, aircraft):
        if aircraft.get_type() == 'F35':
            self.__aircrafts_f35.append(aircraft)
        else:
            self.__aircrafts_f16.append(aircraft)

    def fill(self):
        if self.__ammo_store == 0:
            raise ValueError('Ammo store is empty')

        required_ammo_for_f35s = 0
        for f35 in self.__aircrafts_f35:
            required_ammo_for_f35s += f35.get_missing_ammo()

        required_ammo_for_f16s = 0
        for f16 in self.__aircrafts_f16:
            required_ammo_for_f16s += f16.get_missing_ammo()

        required_total = required_ammo_for_f35s + required_ammo_for_f16s

        if required_total > self.__ammo_store:
            for f35 in self.__aircrafts_f35:
                missing = f35.get_missing_ammo()
                if missing > self.__ammo_store:
                    print('Cannot refill, empty ammo store')
                    break
                f35.refill(missing)
                self.__ammo_store -= missing
        else:
            for f35 in self.__aircrafts_f35:
                missing = f35.get_missing_ammo()
                f35.refill(missing)
                self.__ammo_store -= missing
            for f16 in self.__aircrafts_f16:
                missing = f16.get_missing_ammo()
                f16.refill(missing)
                self.__ammo_store -= missing

    def fight(self, other_carrier):
        total_dmg = 0
        for f35 in self.__aircrafts_f35:
            total_dmg += f35.fight()
        for f16 in self.__aircrafts_f16:
            total_dmg += f16.fight()

        other_carrier.lower_hp(total_dmg)

    def get_hp(self):
        return self.__hp

    def lower_hp(self, dmg):
        self.__hp -= dmg
