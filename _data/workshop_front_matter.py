"""
Script for adding Jekyll front matter and organizers to workshop pages.

python3 _data/workshop_front_matter.py _data/workshops.csv _data/workshops_raw_html/ _program/workshops/
"""

import argparse
import csv
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    parser.add_argument('indir')
    parser.add_argument('outdir')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    with open(args.data_file) as f:
        reader = csv.DictReader(f)
        workshop_data = { workshop['internal_id'] : workshop for workshop in reader }

    for fname in os.listdir(args.indir):
        internal_id = os.path.splitext(fname)[0]
        workshop = workshop_data[internal_id]

        inpath = os.path.join(args.indir, fname)
        outpath = os.path.join(args.outdir,
                               workshop['external_id'].replace('-', '').lower() + '.md')

        front_matter = [
            '-' * 3,
            'layout: page',
            'title: "{}"'.format(workshop['title']),
            'invisible: true',
            '-' * 3,
        ]

        with open(inpath) as fin:
            outtext = \
                '\n'.join(front_matter) + \
                '\n<p><i>Organizers: {}</i></p>\n'.format(workshop['organizers'].replace(',', ', ')) + \
                fin.read()

        with open(outpath, 'w') as fout:
            fout.write(outtext)

if __name__ == '__main__':
    main()
