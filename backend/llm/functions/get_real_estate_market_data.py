from typing import Optional, Tuple
from .function_interface import Function
from models.stream_response import StreamResponse
import pandas as pd
from sshtunnel import SSHTunnelForwarder
import pymysql
from datetime import datetime, timedelta
import os 
import logging

class GetRealEstateMarketData(Function):

    ssh_host = "evaluation.danamelk.ir"
    ssh_user: str = os.getenv('DANAMELK_USER', None)
    ssh_password: str = os.getenv('DANAMELK_PASSWORD', None)
    
    mysql_host: str = "localhost"
    mysql_db: str = os.getenv('DANAMELK_DB_NAME', None)
    mysql_user: str = os.getenv('DANAMELK_DB_USER', None)
    mysql_password: str = os.getenv('DANAMELK_DB_PASSWORD', None)
    mysql_port: int = int(os.getenv('DANAMELK_DB_PORT', None))
    mysql_table: str = "crawler_divar_post_info"

    def dump_real_estate_data(cls):
        logging.warn("Starting dump_real_estate_data")
        if None in (cls.ssh_host, cls.ssh_user, cls.ssh_password, cls.mysql_user, cls.mysql_password, cls.mysql_db):
            logging.error("Missing SSH or MySQL credentials in environment variables.")
            raise ValueError("SSH and MySQL credentials must be provided in the environment variables.")
        try:
            logging.warn("Setting up SSH tunnel to %s", cls.ssh_host)
            with SSHTunnelForwarder(
                (cls.ssh_host, cls.ssh_port),
                ssh_username=cls.ssh_user,
                ssh_password=cls.ssh_password,
                remote_bind_address=(cls.mysql_host, cls.mysql_port),
                local_bind_address=('127.0.0.1', cls.mysql_port)
            ) as tunnel:
                logging.warn("SSH tunnel established. Connecting to MySQL...")
                conn = pymysql.connect(
                    host='127.0.0.1',
                    port=3306,
                    user=cls.mysql_user,
                    password=cls.mysql_password,
                    db=cls.mysql_db
                )
                last_month = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
                cte_where_clauses = [
                    f"crawl_timestamp >= '{last_month}'",
                    f"year_built >= 1398",
                    f"parking = 1",
                    f"elevator = 1",
                    f"storeroom = 1",
                    f"sanad = 'تک‌برگ'",
                ]
                final_where_clauses = [
                    f"t1.subtitle_neighborhood IN ('مرزداران', 'ولنجک', 'پونک', 'دروس', 'شهرک غرب')",
                    f"t2.similar_divar_post_pred BETWEEN -0.15 AND -0.05",
                ]
                query = f"""
                    with cte as 
                    (
                        SELECT
                        *
                        FROM crawler_divar_post_info
                        where {' AND '.join(cte_where_clauses)}
                        LIMIT 1000
                    )
                    SELECT
                        *
                    FROM cte as t1
                    INNER JOIN real_estate_evaluation as t2
                    on t1.post_id = t2.id
                    WHERE {" AND ".join(final_where_clauses)}
                    LIMIT 5
                """
                logging.warn("Executing SQL query: %s", query)
                df = pd.read_sql(query, conn)
                conn.close()
                logging.warn("Query executed and connection closed. DataFrame shape: %s", df.shape)
                return df
        except Exception as e:
            logging.exception("Error in dump_real_estate_data: %s", e)
            raise

    @classmethod
    def run(cls, *args, **kwargs) -> Tuple[Optional[StreamResponse], str]:
        logging.warn("GetRealEstateMarketData.run called with args: %s, kwargs: %s", args, kwargs)
        try:
            real_estate_suggestions = cls.dump_real_estate_data().to_json(orient='records', force_ascii=False)
            logging.warn("Real estate suggestions generated. Length: %d", len(real_estate_suggestions))
            return None, real_estate_suggestions
        except Exception as e:
            logging.exception("Error in GetRealEstateMarketData.run: %s", e)
            return None, f"Error: {e}"
    
    @classmethod
    def get_name(cls):
        return "get_real_estate_market_data"
    
    @classmethod
    def get_props(cls, store_profile: Optional[dict] = None):
        return {
            "type": "function",
            "function": {
                "name": "get_real_estate_market_data",
                "description": "This function takes no arguments and returns real estate market data in JSON format.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False
                }
            }
        }
