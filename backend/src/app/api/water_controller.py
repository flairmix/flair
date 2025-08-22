from typing import Annotated
from litestar import Controller, get
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST

from ..engineering_lib.water_consumption_sp30 import *


class WaterController(Controller):
    path = "/water"
    tags = ["water"]
    
    @get("/calculate_NPhv", status_code=HTTP_200_OK)
    async def get_calculate_NPhv(
        self, 
        U: float,
        qhru: float = 6.5,
        q0_hr: float = 200,
        ) -> float:

        try:
            if qhru <= 0 or q0_hr <= 0 or U <= 0:
                raise ValueError("Все параметры должны быть положительными числами")
                
            result = calculate_NPhv(qhru, q0_hr, U)
            return result
        
        except ValueError as ve:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка в параметрах: {str(ve)}"
            )
        except TypeError as te:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка типа данных: {str(te)}"
            )
        except ZeroDivisionError:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Деление на ноль в расчетах"
            )
        
    @get("/calculate_alpha", status_code=HTTP_200_OK)
    async def get_calculate_alpha(
        self, 
        np_value: float,
        ) -> float:

        try:
            alpha = calculate_alpha(np_value)

            return alpha
        
        except ValueError as ve:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка в параметрах: {str(ve)}"
            )
        except TypeError as te:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка типа данных: {str(te)}"
            )
        
    @get("/calculate_flow_max_hr", status_code=HTTP_200_OK)
    async def get_calculate_flow_max_hr(
        self, 
        alpha: float,
        q0_hr: float=200,
        ) -> float:

        try:
            return calculate_maximum_hourly_flow(alpha, q0_hr)
        
        except ValueError as ve:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка в параметрах: {str(ve)}"
            )
        except TypeError as te:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка типа данных: {str(te)}"
            )
        
    @get("/calculate_flow_max_hr_full", status_code=HTTP_200_OK)
    async def get_calculate_flow_max_hr_full(
        self, 
        U:float,
        qhru: float=6.5,
        q0_hr: float=200,
        ) -> float:

        try:
            if qhru <= 0 or q0_hr <= 0 or U <= 0:
                raise ValueError("Все параметры должны быть положительными числами")
                
            NPhv = calculate_NPhv(qhru, q0_hr, U)
            alpha = calculate_alpha(NPhv)
            return calculate_maximum_hourly_flow(alpha, q0_hr)
        
        except ValueError as ve:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка в параметрах: {str(ve)}"
            )
        except ValueError as ve:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка в параметрах: {str(ve)}"
            )
        except TypeError as te:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=f"Ошибка типа данных: {str(te)}"
            )
