---
layout: post
title:  "Option Trader's Handbook"
categories:
---

If someone asks me about trading, it's tough to give a good answer on the spot.  So I decided to write it out in a post.

Over the course of several weeks it expanded into a corpus of trading knowledge.  It now has a dedicated page and sees routine edits.  Check back.

* TOC
{:toc}

# Trading styles and markets
There are 3 trading styles: investing, swing trading, and scalping.
There are 6 markets to trade: OTC (pinks), equities, futures, commodities, cryptocurrencies, and options.

OTC, over-the-counter, "pinks", and penny stocks are all names for the same thing.  These equities are not big enough to trade on a regulated exchange.  These low quality stocks tend to lay dormant for years, and spike on news.  Since prices can be as low as hundredths of a penny, leverage is built into the product.

Equities refers to exchange traded stocks.  This is the most common route to investing and trading.

Futures are dated based on month and are the market's best guess of future value.  These trade 24/7.
Commodities are futures contracts for amounts of commodities such as hog, corn, sugar, coffee.  These also trade 24/7.

Cryptocurrencies are blockchain based digital currencies.  `$BTCUSD`, `$ETHUSD`, and `$LTCUSD` are the most common currently.

Careers have been made across styles and markets.

Here's what I've tried:

|                  | Investing | Swing Trading | Scalping |
|------------------|:---------:|:-------------:|:--------:|
| OTC              |           | 1 year        |          |
| Equities         | 6 years   |               |          |
| Commodities      |           |               |          |
| Futures          |           |               |          |
| Cryptocurrencies |           | 1 year        |          |
| Options          |           |               | 2 years  |


Investing, Swing Trading, Scalping... what do they all mean?

Investing involves fundamental analysis and a fair value.  It says nothing about short term price movement, and may encourage adding to losing positions as the equity is now "cheaper."  Time horizon is long term.  I have maintained a passive portfolio for 6 years, as well as a 401k, but I do not manage either of them.  They are diversified across low-fee ETFs.

Trading is the focus of this handbook. A trade is a "swing" if it is medium-long term, while it is a "scalp" if it is short term. (usually intraday)

Trading looks at price action to find prices that offer good risk/return versus an area of support or resistance.  It uses a systematic approach.

# What are options
Options are a type of derivative created to hedge underlying positions.  They require less capital than an equity position and allow fine-tuning of risk.  Call options are long positions and put options are short positions.

Here's an example of a put option.

## Why options exist
Goldman holds a lot of `$GM` in its Blue Chip ETF.  `$TSLA` is founded and poses a significant threat to `$GM`. Goldman wants to lower risk.  Goldman's can't just liquidate the stake.  
His buddy Silverman is a big `$GM` bull.
So Goldman says to Silverman, "I'll give you a dime now for the right to sell you a `$GM` share at today's price until the new year".  Sounds good to Silverman, so he writes a contract and sells it to Goldman.

If `$GM` tanks, Goldman could offload his `$GM` shares to Silverman at the higher price from several months ago.
If `$GM` price goes up or doesn't move, the put option will been worthless.

That's a put option.

## How options work
Options are frequently traded "naked" or without owning the underlying.  
Risk is premium paid.  Premium is based on the underlying price relative to the contract strike, the underlying volatility, and the contract's time to expiration.  

An aggressive scalp setup is an out-of-the-money weekly option.  This position is cheap because the stock needs to move a lot in a little time (low probability).
A conservative swing setup is an in-the-money LEAP option.  This position is expensive because the stock has wiggle room and lots of time (high probability).

The advantage of options is the ability to specifically express your view in the market.   

### Advantage of option over stock
Say you think $AAPL is going to go up from $150 to $160 during the special event this week.  This idea can be traded with a stock, or with an option.  
You could spend $15,000 on 100 shares for a potential return of $1000.  `1000/15000 = 6.6% return`
Or you could buy a weekly call option with 150 strike for $2 per share est.  This would cost $200 for 100 shares and would increase to $10+ per share on a move to $160, or $1000+ potential return. `1000/200 = 500% return`
If Apple announces that they are getting out of the computer business and the stock drops to $100. The equity position would lose $5,000 ($15k-10k) but the call option would only lose its premium, $200.

Some powerful stuff!

# What is risk
Risk is the possibility of loss.  Any activity is inherently risky.  But people still drink, smoke, drive cars, eat BBQ, and do other "risky" things.  Trading is definitely risky.

Taking risk on is the only way you can do anything in life.  There's the risk of dying, the risk of taking a big loss, the risk of missed opportunities.  **You only learn by taking on risk.**

How do you operate in a risky environment?  When driving, you reduce the risk of dying by wearing a seatbelt.  When managing multiple positions, you diversify across uncorrelated assets.  

When managing a single position, you set a stop loss.  
This is the max amount you can lose.  How much are you really OK with losing?  You will not win every time.  

The best way to approach a trade is to accept the loss ahead of time.  **Your default mindset should be that you will be wrong.**  This way, you are not micromanaging the trade or scalping a promising swing.

You put your stop at a level of support if you are long, or a level of resistance if you are short.

## Support/resistance
Trades that have a high probability of working have a low payout, and trades that have a low probability of working have a high payout.

Support and resistance are important concepts in trading.  Once identified, you want to enter longs at support and exit at resistance, and vice versa for shorts (enter at resistance, exit at support).

For example say you want to buy the bottom in `$SNAP`.  It has been going down ever since it IPO'd.  If last week `$SNAP` hit $10 and bounced to $11, and you think $10 is support and $15 is resistance, then you can build a trade around this idea. 

If you want to lose no more than $50 on the trade, you can do two things:
-buy 50 shares and stop out below $10.  If you are correct and `$SNAP` continues upwards, you can lock in profits along the way by trailing your stop up or selling partials at price targets, ie. $15, a 5R trade.
-buy a weekly 10 call option around $120 and set a stop at $70.  If `$SNAP` hits $15 the option will be worth at least $500, a 10R trade.

## Measuring risk

Each trade is measured by R - how many units of risk you won or lost on the trade.  
`R = (profit or loss)/(risked amount)`

The goal is to maximize your overall expectancy.  
`Expectancy = (P(Win) * Avg(Win)) - (P(Loss) * Avg(Loss))`

If you win 50% of trades and win 1R per trade, your expectancy is 0.
If you win 30% of trades and win 2.5R per trade, your expectancy is 10%.

Here's the table showing expectancy, given a `Win %` and an `R`.

| Win % |  1R |  2R |  3R |  4R |  5R |
|:-----:|:---:|:---:|:---:|:---:|:---:|
| 10    | -.8 | -.7 | -.6 | -.5 | -.4 |
| 20    | -.6 | -.4 | -.2 | 0   |  .2 |
| 30    | -.4 | -.1 |  .2 |  .5 |  .8 |
| 40    | -.2 |  .2 |  .6 | 1   | 1.4 |
| 50    | 0   |  .5 | 1   | 1.5 | 2   |
| 60    |  .2 |  .8 | 1.4 | 2   | 2.6 |
| 70    |  .4 | 1.1 | 1.8 | 2.5 | 3.2 |
| 80    |  .6 | 1.4 | 2.2 | 3   | 3.8 |
| 90    |  .8 | 1.7 | 2.6 | 3.5 | 4.4 |
| 100   | 1   | 2   | 3   | 4   | 5   |

Expectancy goes up if you have more % trades that work, or if you increase your win size or decrease your loss size.

Random position sizing affects expectancy.
ie. a red-herring event on a too-large position could kill a portfolio, so traders focused on risk will size their positions equally.

# The auction
Any series can be analyzed with an understanding of the underlying phenomenon.  In this instance, it's a market.

Markets are made up of buyers and sellers at an auction.  This is the reason price analysis has predictive value - it allows you to identify buyers and sellers, and their stops.  
Participants have a trade idea and are positioned accordingly.  Buyers have entered at support, and sellers have exited at resistance.  
If price retraces and retests support, price will be absorbed by the stops of all the buyers who bought at that level.  If there are more sellers now than buyers previously, price will break below the level.  

If price pushes up against resistance, it will absorbed by the stops of all the sellers at that level.  If there are more buyers now than sellers previously, price will break above that level.

# Charts

Charts are visualizations of price action.  There are several types beyond the default line chart.  Besides the Candlestick chart, two other charts are common.  
Heikin Ashi charts show trend reversals.  
Bar charts reduce noise for long term trades.

The most common type of chart for traders is the Candlestick chart.  A candlestick chart divides price action into periods, usually 5m, 1hr, or 1d in length.  
Each of these candlestick bodies contain info: `Open, High, Low, Close`  The longer the period contained by the candlestick, the more significant its levels are.  

As charts can be viewed on various timeframes, any timeframe can be traded.  Shorter timeframes are more volatile and subject to noise.  Longer timeframes are more reliable, but may not help intraday.  

## Trade setups
**You are trying to find fast directional moves as early as possible without decreasing odds**.

2 common methods of finding reliable moves is buying dips in uptrends or rips in downtrends, or buying breakouts.  

To buy a breakout, first you have to identify it.  Start on higher timeframes like the weekly chart and find levels of resistance.  If price has not been able to get past $200 in several years, a break above $200 would be meaningful.  If, after a series of higher lows, price breaks above $200, that's a bullish move.  Bullish moves signal a surplus of buyers vs sellers.  Therefore, trading this setup would give a higher than average win rate.
Additionally, you could go into the lower timeframes and confirm price continuation.

Trade ideas can be strengthened by multiple sources of uncorrelated confirmation.  A way to be more confident in a trade is to find confluence between indicators, timeframes, and trading styles.

## Indicators
Indicators are price calculations with a trailing period. They are used to build trade confidence, and define risk.  

I use Moving Averages and Fibonacci levels.  Here are some of the others:

- `VWAP` (volume weighted average price)
- `KC` (keltner curves)
- `BB` (bollinger bands)

- `RSI` (relative strength index)
- `MACD` (moving average convergence divergence)
- `%R` (william's %R) 

- `ATR` (average true range)

### Moving averages
Moving Averages are lines used as support/resistance.  
ie. Longs are valid above the Moving Average, while Shorts are valid below the Moving Average.  

The most common Moving Averages to see are 8 and 21 for short term trading and 50 and 200 for long term trading.  5, 10, 14, and 30 are also used.

Importantly, Moving Averages vary depending on timeframe.  For example, a 8MA on the 15m chart is equal to 24MA on the 5m chart because it contains 120 minutes.

Moving averages can be exponential (EMA) or simple (SMA) depending on preference.  It makes little difference.

### Fibonacci levels
Fibonacci Levels are from the Fibonacci sequence where each number (after two 1's) is the sum of the two before it.  This growth pattern shows up in nature such as plants.  
Its application in the market is in measuring moves.

The levels are 23.6%, 38.2%, 50%, 61.8%, and 100%.
The rule of thumb is if a pullback holds the .618 (61.8%) of the move, that's a healthy move.

# Edge
Of course, you didn't show up to lose.  You have to define your edge.  Edge emerges from a combination of factors - trade selection, risk control, trade management.

With a defined edge, you can stop avoiding risk and move towards risk.

# Trading Systems
Trading systems are modularized and cover the full process, from trade ideas to trading and journaling.  Here are two systems I've seen described.

- Backtesting
- Trading Signals
- Risk and Position Management
- Portfolio and Order Management
- Execution
- Reporting

- Price Stream
- Trading Strategy
- Risk Management
- Execution Handler
- Logging

If you are interested in building a trade system, start pulling some basic data into [Google Sheets][gs] and running backtests on [Quantopian][quant].

Frankly, you need a lot of money and patience to trade fully automated.  I trade by hand and am testing various strategies in real time.  No point in automating something if it doesn't make money, right?

# Reference
[Twitter List of Traders][list]


[list]: https://twitter.com/ale627/lists/trading-whitelist
[gs]: https://google.com/sheets
[quant]: https://quantopian.com






