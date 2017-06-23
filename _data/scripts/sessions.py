"""
Script for computing the session ID for each paper in a conference program.

python3 _data/scripts/sessions.py _data/conference_program.csv _data/papers.csv _data/sessions.csv
"""

import argparse
import csv
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('program')
    parser.add_argument('papers')
    parser.add_argument('sessions')
    args = parser.parse_args()

    with open(args.program) as f:
        reader = csv.DictReader(f)
        sessions = { '{0:0>2}'.format(event['session_id']) : event['papers'].split()
                     for event in reader if event['papers'] != '0' }

    with open(args.papers) as f:
        reader = csv.DictReader(f)
        papers = { paper['external_id'] : (paper['title'], paper['authors'])
                   for paper in reader }

    with open(args.sessions, 'w') as f:
        writer = csv.DictWriter(f,
            fieldnames=['id', 'session', 'title', 'authors'],
            lineterminator='\n')

        writer.writeheader()
        for session in sorted(sessions):
            for paper_id, session_letter in zip(sessions[session], 'ABCD'):
                session_id = session + session_letter
                title, authors = papers[paper_id]
                writer.writerow({
                    'id': paper_id,
                    'session': session_id,
                    'title': title,
                    'authors': authors,
                })

if __name__ == '__main__':
    main()
