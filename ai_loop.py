import time
import os
from supabase import create_client

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

while True:
    try:
        supabase.rpc("run_ai_loop").execute()
        print("AI loop executed")

    except Exception as e:
        print("Error:", e)

    time.sleep(300)
