#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import argparse


# Version ohne Parser
# lauffähig machen mit sudo chmod +x logger.py

def run(args):
    rd = open(args.input)  # Eingabedatei
    wrt = open(args.output, 'w')  # Ausgabedatei
    for line in rd:  # zeilenweises Auslesen
        line = line.rstrip('\n')
        zeile = line.split(',')
        date, feucht_a, temp_a, feucht_i, temp_i, stand, volk = zeile[0], zeile[1], zeile[2], zeile[3], zeile[4], zeile[
            5], zeile[6]  # zeile in tuple zerlegen
        if feucht_i == '0.00':  # kein Wert für Luftfeuchte innen?
            feucht_i = feucht_a
        wrt.write(
            "INSERT INTO wetter (datum,luftfeuchte,temperatur,stand) VALUES (" + "'" + date + "'" + ","
            + feucht_a + "," + temp_a + "," + "'" + stand + "'" + ");\n")
        wrt.write(
            "INSERT INTO stock (datum,luftfeuchte,temperatur,volk) VALUES (" + "'" + date + "'" + ","
            + feucht_i + "," + temp_i + "," + "'" + volk + "'" + ");\n")
    # Ausdabe in Datei
    rd.close()  # Datei schließen
    wrt.close()


def main():
    parser = argparse.ArgumentParser(description="csv-logger-Datei lesen")
    parser.add_argument("-in", help="csv input file", dest="input", type=str, required=True)
    parser.add_argument("-out", help="sql output file", dest="output", type=str, required=True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
