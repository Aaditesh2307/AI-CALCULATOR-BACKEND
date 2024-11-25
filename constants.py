from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'localhost'
PORT = '8900'
ENV = 'dev'

GEMINI_API_KEY = os.getenv("AIzaSyClVvDqyyDC-7Cwa0sgtdPmzrNrLPU1e3I")