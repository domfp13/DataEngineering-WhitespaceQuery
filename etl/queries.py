# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by DataEngineering Team
# Copyright (c) 2019 CompuCom, All Rights Reserved

from __future__ import annotations
from typing import Optional

def WhiteSpaceUSA() -> str:
    '''
    This is the whitespace_usa query, this is to support USA data
    
    Parameters:
    None
     
    Returns:
    str: Query string

    '''
    query = '''
            WITH A AS (
                SELECT A.zipcode as zipcode,
                        A.dist_type as dist_type,
                        A.country as country,
                        A.s_x_service_team as team,
                        A.geo_code as geo_code,
                        A.geo_desc as geo_desc,
                        A.biz_org as biz_org,
                        A.dist_name AS dist_name     
                FROM DW.T_CLAR_DISTRICT_ZIP A
                WHERE A.country = 'USA' and A.dist_type = 'DISPATCH'
            )
            SELECT A.zipcode as zipcode,
                A.dist_type as dist_type,
                A.country as country,
                A.team as team,
                A.geo_code as geo_code,
                A.geo_desc as geo_desc,
                A.biz_org as biz_org,
                B.s_x_dist_name AS service_city,
                C.s_last_name || ', ' || C.s_first_name AS slmi,
                F.f_resource_name AS slmii,
                G.f_resource_name AS vp
            FROM A
            INNER JOIN DW.T_CLAR_DISTRICT B 
            ON A.dist_name = B.s_x_dist_name
            INNER JOIN DW.T_CLAR_EMPLOYEE C 
            ON B.x_district2x_supe = C.objid
            LEFT JOIN DW.T_DM_HUMAN_RESOURCES E 
            ON C.s_employee_no = E.f_resource_id
            LEFT JOIN DW.T_DM_HUMAN_RESOURCES F 
            ON E.f_resource_mgr_id = F.f_resource_id
            LEFT JOIN DW.T_DM_HUMAN_RESOURCES G 
            ON F.F_RESOURCE_MGR_ID = G.F_RESOURCE_ID
            '''
    return query

def WhiteSpaceCanada() -> str:
    '''
    This is the whitespace_canada query, this is to support Canada data
    
    Parameters:
    None
     
    Returns:
    str: Query string

    '''
    return None