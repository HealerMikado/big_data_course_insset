import json

from ish_parser import ish_parser, ish_report

import gzip
import os
import concurrent.futures
from itertools import repeat

out_folder = 'json'
in_folder = 'isd'



def transform_data(weather_station):

        print(f"process file {weather_station}")
        with gzip.open(f"{out_folder}/{weather_station}.jsonl.gz", "wt") as fout:
            try : 
                with gzip.open(f"{in_folder}/{weather_station}", 'rb') as fin:
                    content = bytes.decode(fin.read())
                    wf = ish_parser()
                    wf.loads(content)
                    lines = []
                    for report in wf.get_reports():
                        lines.append(report.toJson())
                    fout.write("\n".join(lines))
            except UnicodeDecodeError as e:
                print(f'le fichier {file} est en erreur')


def main():
    try:
        os.mkdir(f"{out_folder}")
    except OSError as error:
        print(error)

    weather_station = os.listdir(in_folder)

    # with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        executor.map(transform_data, weather_station)


if __name__ == "__main__":
    main()
