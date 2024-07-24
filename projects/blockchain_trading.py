import ccxt
import pandas as pd
import time

# Set up the exchange
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
})

# Define the trading pair
symbol = 'BTC/USDT'

# Define the trading strategy
def trading_strategy():
    # Calculate the RSI
    rsi = calculate_rsi()
    
    # Check if the RSI is below 30 (buy signal)
    if rsi < 30:
        return 'buy'
    # Check if the RSI is above 70 (sell signal)
    elif rsi > 70:
        return 'sell'
    else:
        return 'hold'

# Define the RSI calculation function
def calculate_rsi():
    # Get the historical data
    hist = exchange.fetch_ohlcv(symbol, timeframe='1m')
    
    # Convert the historical data to a DataFrame
    df = pd.DataFrame(hist, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    # Calculate the RSI
    delta = df['close'].diff(1)
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up = up.rolling(window=14).mean()
    roll_down = down.rolling(window=14).mean().abs()
    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))
    
    return rsi.iloc[-1]

# Set up the trading loop
while True:
    try:
        # Get the current ticker
        ticker = exchange.fetch_ticker(symbol)
        
        # Check the trading strategy
        action = trading_strategy()
        
        # Execute the trade
        if action == 'buy':
            exchange.create_market_buy_order(symbol, 0.01)
            print('Buy signal! Buying 0.01 BTC')
        elif action == 'sell':
            exchange.create_market_sell_order(symbol, 0.01)
            print('Sell signal! Selling 0.01 BTC')
        else:
            print('No signal. Holding.')
        
        # Wait for 1 minute
        time.sleep(60)
    except ccxt.BaseError as e:
        print(f'An error occurred: {e}')
        time.sleep(60)
