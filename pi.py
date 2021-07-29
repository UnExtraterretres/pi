from datetime import datetime
import decimal


def calc_pi():

    def pi(precision=100):
        dec = decimal.Decimal
        decimal.getcontext().prec = precision
        try:
            s = dec(open("s.txt", "r").read())
            t = dec(open("t.txt", "r").read())
            open("log.txt", "a").write("s.txt t.txt loaded\n")
            if s != t:
                open("log.txt", "a").write("s != t\n")
                s = dec(2) * dec.sqrt(dec(2))
                t = dec(4)
        except FileNotFoundError:
            s = dec(2) * dec.sqrt(dec(2))
            t = dec(4)
            open("log.txt", "a").write("s.txt t.txt FileNotFoundError\n")

        while s != t:
            t = dec((2*s*t)/(s+t))
            s = dec.sqrt(s*t)
        open("log.txt", "a").write("calculations completed\n")

        open("s.txt", "w").write(str(s))
        open("log.txt", "a").write("s saved in s.txt\n")

        open("t.txt", "w").write(str(s))
        open("log.txt", "a").write("t saved in t.txt\n")

        open("precision.txt", "w").write(str(precision))
        open("log.txt", "a").write("precision saved in precision.txt\n")

    try:
        pi(precision=int(open("precision.txt", "r").read())+100)
    except FileNotFoundError:
        open("log.txt", "a").write("precision.txt FileNotFoundError\n")
        pi()


if __name__ == "__main__":
    open("log.txt", "a").write(f"{datetime.now()}\n")
    calc_pi()
    open("log.txt", "a").write("\n")
