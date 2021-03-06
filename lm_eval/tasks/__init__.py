from . import superglue
from . import glue

TASK_REGISTRY = {
    "cola": glue.CoLA,
    "mnli": glue.MNLI,
    "mrpc": glue.MRPC,
    "rte": glue.RTE,
    "qnli": glue.QNLI,
    "qqp": glue.QQP,
    "stsb": glue.STSB,
    "sst": glue.SST,
    "wnli": glue.WNLI,
    "boolq": superglue.BoolQ,
    "commitmentbank": superglue.CommitmentBank,
    "copa": superglue.Copa,
    "wic": superglue.WordsInContext,
    "wsc": superglue.WinogradSchemaChallenge,
}


ALL_TASKS = sorted(list(TASK_REGISTRY))


def get_task(task_name):
    return TASK_REGISTRY[task_name]


def get_task_dict(task_name_list):
    return {
        task_name: get_task(task_name)()
        for task_name in task_name_list
    }
