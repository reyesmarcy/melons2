"""Classes for melon orders."""

class AbstractMelonOrder:
    """general melon order"""
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        return total

    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

        
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""

        total = super().get_total()
        print(total)

        if self.qty < 10:
            total = total + 3 

        return total


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
        self.tax = 0


    def mark_inspection(self, passed):

        self.passed_inspection = passed







