class Item:
    def __init__(self, name, desc):
        self.name = name
        self.description = desc

    def on_take(self):
        print(f"You have picked up a {self.name}")

    def on_drop(self):
        print(f"You have dropped the {self.name}")