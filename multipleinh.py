class Theory:
    def th(self):
        print("theory marks ")

class Sessional:
    def ss(self):
        print("Sessional marks ")


class Result(Theory,Sessional):
    def res(self):
        print('result')

r=Result()
r.th()
r.ss()
r.res()