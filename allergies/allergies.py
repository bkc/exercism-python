class Allergies:
    ALLERGENS = (
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats",
    )

    def __init__(self, score):
        # convert score to a set of allergens
        self.allergen_set = {
            allergen
            for offset, allergen in enumerate(self.ALLERGENS)
            if 2**offset & score
        }

    def allergic_to(self, item):
        return item in self.allergen_set

    @property
    def lst(self):
        return list(self.allergen_set)
