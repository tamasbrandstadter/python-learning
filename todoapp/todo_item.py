class TodoItem:

    def __init__(self, desc, due_date):
        self.description = desc
        self.completed = False
        self.due_date = due_date

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        if len(new_description) > 5:
            self.__description = new_description
        else:
            print('Description length is not long enough, minimum 5 chars')
