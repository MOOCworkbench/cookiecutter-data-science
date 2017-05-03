# -*- coding: utf-8 -*-
import os
import click
import logging
import json
from dotenv import find_dotenv, load_dotenv

import pandas
from pandas.io.json import build_table_schema

SCHEMA_LOCATION = 'schema/schema.json'


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
def main(input_filepath):
    """ Create your data frame from your data set and call the function
        pdf_to_json to save a JSON table schema representing your data.

    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    df = pandas.read_csv(input_filepath)
    pd_to_json(df, logger)


def pd_to_json(df_or_series, logger):
    table_schema = build_table_schema(df_or_series)
    logger.info('created table schema: {0}'.format(table_schema))
    table_schema_json = json.dumps(table_schema)
    output_file = os.path.join(project_dir, SCHEMA_LOCATION)
    with open(output_file, 'w') as out:
        out.write(table_schema_json)
        out.close()
    logger.info('written table schema to {0}'.format(SCHEMA_LOCATION))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
