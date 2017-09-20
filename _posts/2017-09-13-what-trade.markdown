---
layout: post
title:  "Intro to Options Trading"
date:   2017-09-13 15:05:00 -0700
categories:
---

If someone asks me about trading, I usually can't speak very well about it on the spot.  So here we go.  

* TOC
{:toc}

There are 3 trading styles: investing, swing trading, and scalping.
There are 6 markets to trade: OTC (pinks), equities, commodities, futures, cryptocurrencies, and options.
Careers have been made in each of the 18 possiblities.

I've tried swing trading OTC, investing in equities, swing trading cryptocurrencies, and scalping options.  90% scalping options.

|                  | Investing | Swing Trading | Scalping |
|------------------|:---------:|:-------------:|:--------:|
| OTC              |           | x             |          |
| Equities         | x         |               |          |
| Commodities      |           |               |          |
| Futures          |           |               |          |
| Cryptocurrencies |           | x             |          |
| Options          |           |               | x        |


# What are Options
Options are a type of derivative created to hedge underlying positions.  They require less capital than an equity position and allow fine-tuning of risk.  Call options are long positions and put options are short positions.

Here's an example of a put option.

## Why Options exist
Goldman holds a lot of `$GM` in its Blue Chip ETF.  `$TSLA` is founded and poses a significant threat to `$GM`. Goldman wants to lower risk.  Goldman's can't just liquidate the stake.  
His buddy Silverman is a big `$GM` bull.
So Goldman says to Silverman, "I'll give you a dime now for the right to sell you a `$GM` share at today's price until the new year".  Sounds good to Silverman, so he writes a contract and sells it to Goldman.

If `$GM` tanks, Goldman could offload his `$GM` shares to Silverman at the higher price from several months ago.
If `$GM` price goes up or doesn't move, the put option will been worthless.

That's a put option.

## How Options Work
Options are frequently traded "naked" or without owning the underlying.  
Risk is premium paid.  Premium is based on the underlying price relative to the contract strike, the underlying volatility, and the contract's time to expiration.  

An aggressive scalp setup is an out-of-the-money weekly option.  This position is cheap because the stock needs to move a lot in a little time (low probability).
A conservative swing setup is an in-the-money LEAP option.  This position is expensive because the stock has wiggle room and lots of time (high probability).

So the value of options is the ability to specifically express your view in the market.  

### Advantage of Option over Stock
Say you think $AAPL is going to go up from $150 to $160 during the special event this week.  
You could spend $15,000 on 100 shares for a potential return of $1000.  `1000/15000 = 6.6% return`
Or you could buy a weekly call option with 150 strike for $2 per share est.  This would cost $200 for 100 shares and would increase to $10+ per share on a move to $160, or $1000+ potential return. `1000/200 = 500% return`
If Apple announces that they are getting out of the computer business and the stock drops to $100. The equity position would lose $5,000 ($15k-10k) but the call option would only lose its premium, $200.

Some powerful stuff!

# How to think about Risk

Proper risk control means a risk/return profile like a wager you might make with a friend.  There are odds, a wager, and defined event.

For example, Pats vs 49ers.  A confident Pats fan offers a 49ers fan 2:1 odds, betting him $5 that the Pats beat the 49ers. If Pats win he gets $5, lose and owes $10. 

*The only way to trade is define risk similarly.  You can do this with a stop, or betting small.  Once your risk is defined, you can examine potential return targets.*

Each trade is measured by R - how many units of risk you won or lost on the trade.  
`R = (profit or loss)/(risked amount)`

For example say you want to buy the bottom in `$SNAP`.  It has been going down ever since it IPO'd.  If last week `$SNAP` hit $10 and bounced to $11, and you think $10 is the bottom and $15 is the target, then you can build a trade around this idea. 

If you want to lose no more than $50 on the trade, you can do two things:
-buy 50 shares and stop out below $10.  If you are correct and `$SNAP` continues upwards, you can lock in profits along the way by trailing your stop up or selling partials at price targets, ie. $15, a 5R trade.
-buy a weekly 10 call option around $120 and set a stop at $70.  If `$SNAP` hits $15 the option will be worth at least $500, a 10R trade.

Random position sizing affects expectancy.
ie. a red-herring event can wipe out a portfolio, so traders focused on risk will size their positions equally.

The goal is to maximize your overall expectancy.  
`Expectancy = (P(Win) * Avg(Win)) - (P(Loss) * Avg(Loss))`
Expectancy goes up if you have more % trades that work, or if you increase your win size or decrease your loss size.

# Finding Trades
**You are trying to find fast directional moves as early as possible without decreasing odds**.

2 common methods of finding reliable moves is buying dips in uptrends or rips in downtrends, or buying breakouts.  

To buy a breakout, first you have to identify it.  Start on higher timeframes like the weekly chart and find levels of resistance.  If price has not been able to get past $200 in several years, a break above $200 would be meaningful.  If, after a series of higher lows, price breaks above $200, that's a bullish move.  Bullish moves signal a surplus of buyers vs sellers.  Therefore, trading this setup would give a higher than average win rate.
Additionally, you could go into the lower timeframes and confirm price continuation.


# Technical Charts
Charts are visualizations of price action.  There are several types beyond the default line chart.  Besides the Candlestick chart, two other charts are common.  
Heikin Ashi charts show trend reversals.  
Bar charts reduce noise for long term trades.

The most common type of chart for traders is the Candlestick chart.  A candlestick chart divides price action into periods, usually 5m, 1hr, or 1d in length.  
Each of these candlestick bodies contain info: `Open, High, Low, Close`  The longer the period contained by the candlestick, the more significant its levels are.  

As charts can be viewed on various timeframes, any timeframe can be traded.  Shorter timeframes are more volatile and subject to noise.  Longer timeframes are more reliable, but may not help intraday.  

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

### Moving Averages
Moving Averages are lines used as support/resistance.  
ie. Longs are valid above the Moving Average, while Shorts are valid below the Moving Average.  

The most common Moving Averages to see are 8 and 21 for short term trading and 50 and 200 for long term trading.  5, 10, 14, and 30 are also used.

Importantly, Moving Averages vary depending on timeframe.  For example, a 8MA on the 15m chart is equal to 24MA on the 5m chart because it contains 120 minutes.

Moving averages can be exponential (EMA) or simple (SMA) depending on preference.  It makes little difference.

### Fibonacci Levels
Fibonacci Levels are from the Fibonacci sequence where each number (after two 1's) is the sum of the two before it.  This growth pattern shows up in nature such as plants.  
Its application in the market is in measuring moves.

The levels are 23.6%, 38.2%, 50%, 61.8%, and 100%.
The rule of thumb is if a pullback holds the .618 (61.8%) of the move, that's a healthy move.

# Reference
[Twitter List of Traders][list]


[list]: https://twitter.com/ale627/lists/trading-whitelist






