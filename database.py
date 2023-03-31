from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ["DB_CONNECTION_STR"]

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def get_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    # print("type(result):", type(result))
    #print("type(result_all:)", type(result_all))
    #print(result_all)
    #first_result = result_all[0]
    #print(first_result)
    # Convert sqpalchemy row to a python dict
    result_dict = []
    for row in result_all:
      result_dict.append(row._asdict())

    #print("type(result_dict):", type(result_dict))
    #print(result_dict)
  return result_dict
