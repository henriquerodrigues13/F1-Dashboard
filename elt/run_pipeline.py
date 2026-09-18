from elt import load, transform
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(message)s")
    logging.info("iniciou pipeline")
    load.load()
    transform.transform_dataframe()
    logging.info("finalizado pipeline")