import sqlite_utils
import llm

import argparse
from pathlib import Path

# i played around with using the tool to generate the argparse code making this a standalone cmd line tool - it worked
# like w/ this prompt: "uv run llm -m o4-mini -f text_to_sql.py -s 'Extend the code in this file to make it a command line tool that uses argparse to extract the needed parameters and then run the function. Include error handling code for invalid paths to the database and also for errors while running the SQL.' -u"

model = llm.get_model('gpt-4.1-mini')

def text_to_sql(db: sqlite_utils.Database, question: str) -> str:
    """Convert a prompt to SQL using the LLM."""
    prompt = f"Schema:\n\n{db.schema}\n\nQuestion:\n\n{question}"
    return model.prompt(
        prompt,
        system='reply with sqlite SQL, not in markdown - just the SQL'
    ).text()

def main():
    parser = argparse.ArgumentParser(
        description='Turn a natural language query into SQL and, optionally, run it.'
    )
    parser.add_argument(
        'question',
        help='The question to ask of your SQLite database, in plain English.',
    )
    parser.add_argument(
        '--db',
        '-d',
        default=str(llm.user_dir() / 'logs.db'),
        help='Path to the SQLite database file. [default: %(default)s]',
    )
    parser.add_argument(
        '--execute',
        '-x',
        action='store_true',
        help='Execute the generated SQL and print the results instead of just showing the SQL.',
    )
    args = parser.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        parser.error(f'Database file not found: {db_path!r}')

    db = sqlite_utils.Database(db_path)
    sql = text_to_sql(db, args.question)

    if args.execute:
        try:
            rows = list(db.query(sql))
        except Exception as e:
            print('Error running the SQL: ', e)
            print('SQL: ', sql)
            raise SystemExit(1)
        # and print rows as simple CSV data
        for row in rows:
            print(row)
    else:
        # no execute, so only output the SQL
        print(sql)

if __name__ == '__main__':
    main()