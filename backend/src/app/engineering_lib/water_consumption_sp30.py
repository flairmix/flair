import pandas as pd
from scipy.interpolate import interp1d
from pathlib import Path


def calculate_qn(q_tot, U, T, N):
    """
    Рассчитывает средние за расчетный период удельные часовые расходы воды на расчетном участке, отнесенные к одному прибору.

    q_tot (float): Общий расчетный расход воды потребителем в средние сутки, л.
    U (int): Число водопотребителей.
    T (float): Расчетное время потребления воды (за сутки), ч.
    N (int): Число санитарно-технических приборов.
    """
    return q_tot * U / (T * N)


def calculate_maximum_hourly_flow(q0_hr, alpha_hr):
    """
    Рассчитывает максимальный часовой расход воды (стоков) по формуле:
    q_hr = 0.005 * q0_hr * alpha_hr

    Параметры:
    - q0_hr: базовый расход воды, м³/ч
    - alpha_hr: коэффициент, зависящий от числа приборов и вероятности их использования

    Возвращает:
    - Максимальный часовой расход воды, м³/ч
    """
    return 0.005 * q0_hr * alpha_hr


def calculate_NPhv(qhru, q0_hr, U) -> float:
    """
    - qhru: расчетный расход горячей воды, л, потребителем в час наибольшего водопотребления, принимаемый по таблице А.2
    - q0_hr: базовый расход воды, м³/ч
    - U (int): Число водопотребителей.
    """ 
    return float(qhru*U / q0_hr)


def calculate_heat_kW(flow_m3_h, delta_t):
    return round(1.163*flow_m3_h*delta_t)


def calculate_alpha(np_value, file_path="SP_30_table_5.2.csv"):
    '''
    Возвращает:
    alpha_hr: коэффициент, зависящий от числа приборов и вероятности их использования
    
    '''
    BASE_DIR = Path(__file__).parent
    CSV_PATH = BASE_DIR / "SP_30_table_5.2.csv"

    try:
        df =pd.read_csv(CSV_PATH, delimiter=';')
    except Exception as ex:
        print(f"Error {ex}")

    exact_match = df[df['NP или NPhr'] == np_value]
    if not exact_match.empty:
        return float(exact_match['alpha'].iloc[0])
    
    f = interp1d(df['NP или NPhr'], df['alpha'], kind='linear')
    
    return float(f(np_value))