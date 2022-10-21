from dataclasses import dataclass
import random as rd
import json as js
import sys, os


@dataclass
class Data :
    data : str

    def show(self) -> str :
        with open("lib/src.json", "r") as f :
            self.data = js.load(f)
            run = rd.choice(self.data)
            f.close()
            return f"\t\t{run['adagium']}\n\n{run['arti']}\n"


def main() :
    data = Data(None)
    print(data.show())


def choice() :
    c = input("Ulang Lagi ? : ")
    try :
        while True :
            if c.__eq__("tidak") or c == "t" :
                sys.exit("\n\t\t--------Keluar--------")
            elif c.__eq__("iya") or c == "ya" or c == "y" :
                if os.name.__eq__("posix") :
                    os.system("clear")
                else :
                    os.system("cls")
                main()
                choice()
            else :
                sys.exit("\n\t\t--------Keluar--------")
    except KeyboardInterrupt :
        sys.exit()


if __name__ == "__main__" :
    main()
    choice()
