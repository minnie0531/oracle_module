import cx_Oracle
import os
from sqlalchemy import create_engine

class Oracle:
    def __init__(self, id=os.getenv("MEMORY_ID"), pw=os.getenv("MEMORY_PW"), dsn=os.getenv("MEMORY_DSN")):
        
        if dsn is None:
            dsn = "dev dsn"
        
        self.update(id, pw, dsn)
        con_str = f"oracle+cx_oracle://{self.id}:{self.pwd}@{self.dsn}"
        self.engine = create_engine(con_str, echo=True)

    def update(self, id, pwd, dsn):
        self.id = id
        self.pwd = pwd
        self.dsn = dsn

    def get_engine(self): 
        return self.engine

