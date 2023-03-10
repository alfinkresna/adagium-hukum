from dataclasses import dataclass
from os.path import join
from os import name, system
import json as js
import random as rd


@dataclass
class AdagiumHukum:
    
    data : list
    
    def show_data(self) -> str:
        run = rd.choice(self.data)
        return f"{run['adagium']}\n\n{run['arti']}\n"
    
    @classmethod
    def from_file(cls, file_path : str) -> "AdagiumHukum":
        with open(file_path, "r") as f:
            data = js.load(f)
            return cls(data)

    @staticmethod
    def show_adagium():
    	file_path = join("lib", "src.json")
    	data = AdagiumHukum.from_file(file_path)
    	print(data.show_data())
    	
    	while True:
    	   choice = str(input("Ulang Lagi ? (iya/tidak) : "))
    	   if choice in {"Tidak", "tidak", "T", "t"}:
    	     print("\n\t\t" + ('-' * 8) + "Keluar" + ('-' * 8))
    	     break
    	   elif choice in {"Iya", "iya", "Ya","ya", "Y", "y"}:
    	           if name == "posix":
    	           	system("clear")
    	           else:
    	           	system("cls")
    	           print(data.show_data())
    	   else:
    	   	print("\n\t\t" + ('-' * 8) + "Keluar" + ('-' * 8))
    	   	break


def main():
	AdagiumHukum.show_adagium()


if __name__ == "__main__":
    main()
