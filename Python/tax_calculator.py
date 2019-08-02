import dateutil


def calculateAddedTax(orders):
        tax = 0
        for order in orders:
            if order.date < dateutil.parser.parse("2018-01-01T00:00Z"):
                tax += 10
            else:
                tax += 20

            for product in order.products:
                if product.isEvent:
                    tax += product.price.getAmountInCurrency("USD")* 0.25;
                else:
                    tax += product.price.getAmountInCurrency("USD")* 0.175;

        return tax
