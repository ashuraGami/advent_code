import argparse
from commons import get_current_path
from anio2021.adventCode import solutions2021
from anio2022.adventCode import solutions2022

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--advent_year", type=int, help="Year of the advent code")
    parser.add_argument("-d", "--advent_day", type=str, help="Day of the advent code")
    args = vars(parser.parse_args())
    return(args)

def main(arguments, path):
    if arguments["advent_year"] == 2021:
        solutions2021(arguments["advent_year"], arguments["advent_day"], path)
    elif arguments["advent_year"] == 2022:
        solutions2022(arguments["advent_year"], arguments["advent_day"], path)

if __name__ == '__main__':
    path = get_current_path()
    arguments = arguments()
    main(arguments, path)
    