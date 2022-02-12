class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num.replace(" ", "")

    def valid(self):
        if not self.card_number.isdigit() or len(self.card_number) <= 1:
            return False

        # personally I find this less readable than using a regular for loop and
        # incrementing a total value.  However it does demonstrate nested if expressions
        # fairly well
        return (
            not sum(
                integer_digit
                if offset % 2 == 0
                else (integer_digit * 2) - 9
                if integer_digit >= 5
                else integer_digit * 2
                for offset, integer_digit in list(
                    enumerate(int(_) for _ in self.card_number[::-1])
                )
            )
            % 10
        )
