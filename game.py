import decimal


class Game:

    def __init__(self, file_path="pi.txt", digits=100):
        # to load arguments
        self.file_path = file_path
        self.digits = digits

        # boolean states of the game
        self.states = {
            "running": True
        }

        # to initialize the precision
        self.dec = decimal.Decimal
        try:
            decimal.getcontext().prec = len(open(self.file_path, "r").read())-1 + self.digits
        except FileNotFoundError:
            decimal.getcontext().prec = self.digits

        # to load pi
        try:
            self.pi = [self.dec(open(self.file_path, "r").read()),
                       self.dec(open(self.file_path, "r").read())]
        except FileNotFoundError:
            self.pi = [self.dec(2)*self.dec.sqrt(self.dec(2)),
                       self.dec(4)]

    def handling_events(self):
        pass

    def update(self):
        if self.pi[0] != self.pi[1]:
            self.pi[1] = self.dec((2*self.pi[0]*self.pi[1])/(self.pi[0]+self.pi[1]))
            self.pi[0] = self.dec.sqrt(self.pi[0]*self.pi[1])

            open(self.file_path, "w").write(str(self.pi[0]))
        else:
            self.states["running"] = False

    def display(self):
        pass

    def run(self):
        # game LOOP
        while self.states["running"]:
            # check events
            self.handling_events()
            # the logic of the game
            self.update()
            # display
            self.display()
