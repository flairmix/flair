from typing import Annotated
from litestar import Controller, get
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST

from ..engineering_lib.water_consumption_sp30 import calculate_NPhv

class WaterController(Controller):
    path = "/water"
    tags = ["water"]
    
    @get("/calculate_NPhv", status_code=HTTP_200_OK)
    async def get_calculate_NPhv(
        self, 
        qhru: float,
        q0_hr: float,
        U: float
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