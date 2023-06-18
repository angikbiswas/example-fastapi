import json

import base64 

import os

import psycopg2

from psycopg2.extras import RealDictCursor 
#from botocore.exceptions import ClientError

from dotenv import load_dotenv

load_dotenv()


params_ = {"host":'localhost', "port": 5432,"database":'fastapi', "user":'postgres', "password":'41721635'}

async def connect(query:str):

    conn=None 
    try:

        conn=psycopg2.connect(**params_) 
        cur =conn.cursor(cursor_factory=RealDictCursor)

        cur.execute(query=query) 
        result =cur.fetchall()

        return result 
    except Exception as e:

        raise e 
    finally:
        if conn is not None: 
            conn.close()

async def execute(query:str): 
    conn=None

    try:

        conn=psycopg2.connect(**params_)

        cur =conn.cursor() 
        result=cur.execute(query=query)

        conn.commit()

        return result

    except Exception as e: 
        raise e
    finally:
        if conn is not None: 
            conn.close()