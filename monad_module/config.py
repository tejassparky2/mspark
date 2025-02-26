import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    class SETTINGS:
        ATTEMPTS = int(os.getenv("ATTEMPTS", "3"))
        PAUSE_BETWEEN_ATTEMPTS = (
            int(os.getenv("PAUSE_BETWEEN_ATTEMPTS_MIN", "1")),
            int(os.getenv("PAUSE_BETWEEN_ATTEMPTS_MAX", "3"))
        )
        PAUSE_BETWEEN_SWAPS = (
            int(os.getenv("PAUSE_BETWEEN_SWAPS_MIN", "1")),
            int(os.getenv("PAUSE_BETWEEN_SWAPS_MAX", "3"))
        )
        RANDOM_PAUSE_BETWEEN_ACTIONS = (
            float(os.getenv("RANDOM_PAUSE_BETWEEN_ACTIONS_MIN", "1")),
            float(os.getenv("RANDOM_PAUSE_BETWEEN_ACTIONS_MAX", "3"))
        )

    class BIMA:
        LEND = os.getenv("BIMA_LEND", "true").lower() == "true"
        PERCENT_OF_BALANCE_TO_LEND = tuple(
            map(int, os.getenv("BIMA_PERCENT_OF_BALANCE_TO_LEND", "20,30").split(","))
        )

    class MAGMA:
        AMOUNT_TO_STAKE = tuple(map(float, os.getenv("MAGMA_AMOUNT_TO_STAKE", "0.0001,0.001").split(",")))
    
    class KINTSU:
        AMOUNT_TO_STAKE = tuple(map(float, os.getenv("KINTSU_AMOUNT_TO_STAKE", "0.0001,0.001").split(",")))
   
    class AMBIENT_SWAP:
        AMOUNT_RANGE = tuple(map(float, os.getenv("AMBIENT_SWAP_AMOUNT", "0.01,0.02").split(",")))
        TOKEN_OUT = os.getenv("AMBIENT_SWAP_TOKEN", "usdc,weth,wbtc,usdt")
        SWAP_ALL = os.getenv("AMBIENT_SWAP_ALL", "False").lower() in ("true", "1", "yes")

    class BEAN_SWAP:
        AMOUNT_RANGE = tuple(map(float, os.getenv("BEAN_SWAP_AMOUNT", "0.01,0.02").split(",")))
        TOKEN_OUT = os.getenv("BEAN_SWAP_TOKEN", "weth,usdc,usdt,jai,wmon")
        SWAP_ALL = os.getenv("BEAN_SWAP_ALL", "False").lower() in ("true", "1", "yes")
    class NAD_SWAP:
        AMOUNT_RANGE = tuple(map(float, os.getenv("NAD_SWAP_AMOUNT", "0.01,0.02").split(",")))
        TOKEN_OUT = os.getenv("NAD_SWAP_TOKEN", "cupang")
        SWAP_ALL = os.getenv("NAD_SWAP_ALL", "False").lower() in ("true", "1", "yes")



def get_config() -> Config:
    return Config
