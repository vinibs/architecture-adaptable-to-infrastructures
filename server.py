from fastapi import FastAPI

from services import poke_data_collector


app = FastAPI()


@app.get("/legendaries")
def get_legendaries():
    return poke_data_collector.collect_legendaries()

@app.get("/starters/{gen_no}")
def get_starters(gen_no: int):
    return poke_data_collector.collect_starter_from_generation(gen_no)