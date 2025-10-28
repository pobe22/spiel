from .questions_dtsm import questions2ADAC_DTSM, questions3ADAC_DTSM
from .questions_inf import questions2ADAC_INF, questions3ADAC_INF, questions4ADAC_INF, questions4ADAC_INF_2
from .questions_awl import questions2ADAC_AWL
from .questions_itl import questions2ADAC_ITL

ALL_QUESTION_SETS = {
    "DTSM2": questions2ADAC_DTSM,
    "DTSM3": questions3ADAC_DTSM,
    "INF2": questions2ADAC_INF,
    "INF3": questions3ADAC_INF,
    "INF4": questions4ADAC_INF,
    "INF4_2": questions4ADAC_INF_2,
    "AWL2": questions2ADAC_AWL,
    "ITL2": questions2ADAC_ITL,
}