def percentage(interest_rate, principle):
    i = 1
    while i <= 365:
        interest = (interest_rate * principle)/100
        principle = interest + principle
        print(principle)
        i += 1

#Example taken here, Interest rate 2, Principle amount 1000
percentage(2, 1000)
