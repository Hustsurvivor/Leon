JOB_DATA_PATH='data/join-order-benchmark/'
STACK_DATA_PATH=''

QUERY_LOG_FILE='query_log_file.txt'
LATENCY_FILE='latency.json'

# PG
DATABASE = "imdb"
USER = "lgn"
PASSWORD = ""
HOST = "localhost"
PORT = "5432"

LOCAL_DSN = f"postgres://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
REMOTE_DSN = LOCAL_DSN
