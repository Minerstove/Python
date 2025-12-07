from oj import Fruit, FruitKind, Ripeness

class FruitStore:
    def __init__(self):
        # store all fruits that have not completely rotted
        self._fruits = []

    def add(self, name, kind):
        # newly added fruit is UNRIPE
        self._fruits.append(Fruit(name=name,
                                 kind=kind,
                                 ripeness=Ripeness.UNRIPE))

    def pass_time(self):
        new_fruits = []
        for f in self._fruits:
            if f.ripeness == Ripeness.UNRIPE:
                # UNRIPE → RIPE
                new_fruits.append(f)
            elif f.ripeness == Ripeness.RIPE:
                # RIPE → OVERIPE (still in store, but no longer sellable)
                new_fruits.append(f)
        self._fruits = new_fruits

    def inventory(self, kind=None):
        # fruits you can sell: any that are NOT overripe
        sellable = [
            f for f in self._fruits
            if f.ripeness != Ripeness.OVERRIPE
            and (kind is None or f.kind == kind)
        ]
        # sorted list of names
        return sorted(f.name for f in sellable)

store = FruitStore()

store.add("apple", FruitKind.ACCESSORY)
store.pass_time()
store.add("apple", FruitKind.ACCESSORY)
assert store.inventory() == ["apple", "apple"]
store.add("pineapple", FruitKind.MULTIPLE)
store.pass_time()
assert store.inventory(FruitKind.MULTIPLE) == ["pineapple"]
assert store.inventory() == ["apple", "pineapple"]
store.pass_time()
assert store.inventory() == []
