from typing import Annotated, Literal
from litestar import Controller, get
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST

from ..engineering_lib.vent_general import *


class VentController(Controller):
    path = "/vent"
    tags = ["vent"]
        
    @get("/get_calculate_airVelocity_m_s", status_code=HTTP_200_OK)
    async def get_calculate_airVelocity_m_s(self,
        flow_m3_h: float = 5000,  
        a_side_m: float = 0.5, 
        b_side_m: float = 0.5, 
        diameter_m: float = 250,
        square_m2: float = 0,
        shape: Literal ["rect", "circle"] = "rect", 
        ) -> float:

        try:
            return calculate_airVelocity_m_s(flow_m3_h=flow_m3_h,
                                             a_side_m=a_side_m,
                                             b_side_m=b_side_m,
                                             diameter_m=diameter_m,
                                             square_m2=square_m2,
                                             shape=shape
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
        
    @get("/get_calculate_air_heating_power_kW", status_code=HTTP_200_OK)
    async def get_calculate_air_heating_power_kW(self,
        flow_m3_h: float = 1000,  
        temp_in: float = -26,    
        temp_out: float = 18,   
        air_density: float = 1.2,  
        specific_heat: float = 1.005  
        ) -> float:

        try:
            return calculate_air_heating_power_kW(
                flow_m3_h=flow_m3_h, 
                temp_in=temp_in,
                temp_out=temp_out,
                air_density=air_density,
                specific_heat=specific_heat
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

    @get("/get_calculate_air_pressure_loss_Pa", status_code=HTTP_200_OK)
    async def get_calculate_air_pressure_loss_Pa(self,
        flow_m3_h: float = 5000, 
        length_m: float = 1, 
        a_side_m: float = 0.1, 
        b_side_m: float = 0.1, 
        diameter_m: float = 0.45, 
        shape: Literal ["rect", "circle"] = "rect", 
        air_density: float = 1.205, 
        kinematic_viscosity: float = 1.49619e-5,
        roughness: float = 0.0001  
        ) -> dict:

        try:
            return calculate_air_pressure_loss_Pa(
                flow_m3_h = flow_m3_h,
                length_m = length_m,
                a_side_m = a_side_m,
                b_side_m = b_side_m,
                diameter_m = diameter_m,
                shape = shape,
                air_density = air_density,
                kinematic_viscosity = kinematic_viscosity,
                roughness = roughness,
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