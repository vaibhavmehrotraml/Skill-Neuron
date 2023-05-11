from trainer import *


def main():
    roberta = AutoModelForMaskedLM.from_pretrained("roberta-base")
    state_dict = roberta.state_dict()
    pass