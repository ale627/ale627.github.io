---
layout: post
title:  "What do you mean, trade?"
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

## Put Option Example
Goldman holds a lot of `$GM` in its Blue Chip ETF.  `$TSLA` is founded and poses a significant threat to `$GM`. Goldman wants to lower risk.  Goldman's can't just liquidate the stake.  
His buddy Silverman is a big `$GM` bull.
So Goldman says to Silverman, "I'll give you a dime now for the right to sell you a `$GM` share at today's price until the new year".  Sounds good to Silverman, so he writes a contract and sells it to Goldman.

If `$GM` tanks, Goldman could offload his `$GM` shares to Silverman at the higher price from several months ago.
If `$GM` price goes up or doesn't move, the put option will been worthless.

That's a put option.

# Option Mechanics
Options are frequently traded "naked" or without owning the underlying.  
Risk is premium paid.  Premium is based on the underlying price relative to the contract strike, the underlying volatility, and the contract's time to expiration.  

An aggressive scalp setup is an out-of-the-money weekly option.  This position is cheap because the stock needs to move a lot in a little time (low probability).
A conservative swing setup is an in-the-money LEAP option.  This position is expensive because the stock has wiggle room and lots of time (high probability).

So the value of options is the ability to specifically express your view in the market.  

## Call vs Equity Example
Say you think $AAPL is going to go up from $150 to $160 during the special event this week.  
You could spend $15,000 on 100 shares for a potential return of $1000.  1000/15000 = 6.6% return
Or you could buy a weekly call option with 150 strike for $2 per share est.  This would cost $200 for 100 shares and would increase to $10+ per share on a move to $160, or $1000+ potential return. 1000/200 = 500% return
If Apple announces that they are getting out of the computer business and the stock drops to $100. The equity position would lose $5,000 ($15k-10k) but the call option would only lose its premium, $200.

Some powerful stuff!

# Risk

Proper risk control means a risk/return profile like a wager you might make with a friend.  There are odds, a wager, and defined event.  
For example, Pats vs 49ers.  A confident Pats fan offers a 49ers fan 2:1 odds, betting him $5 that the Pats beat the 49ers. If Pats win he gets $5, lose and owes $10. 

_Equity traders using this system limit their risk with a stop, usually 2 x ATR(13) or key MAs.  The most common MAs to see are 8 and 21 for short term trading and 50 and 200 for long term trading.  5, 10, 14, and 30 are also used._

The goal is to maximize your expectancy per trade.  
Expectancy = (P(Win) * Avg(Win)) - (P(Loss) * Avg(Loss))
Expectancy goes up if you have more % trades that work, or if you increase your win size or decrease your loss size.

_Random position sizing affects expectancy, ie. a red-herring event can wipe out a portfolio, so traders focused on risk will size their positions equally._

## Charts
Charts are useful for increasing win rate, and R/R.

_The most common type of chart for traders is the candlestick chart.  A candlestick chart divides price action into periods, usually 5m, 1hr, or 1d in length.  Each of these candlestick bodies contain important information: Open, High, Low, Close.  The longer the period contained by the candlestick, the more significant its levels are._ 

### Increase Win Rate
A common method of finding reliable moves is to start on the weekly chart, look for trends, and trade the breakouts.  If price has not been able to get past $200 in several years, a break above $200 would be meaningful.  If price breaks above $200, that signals a surplus of buyers vs sellers.  Therefore, trading this setup would give a higher than average win rate.
Additionally, you could go into the lower timeframes and confirm price continuation.

### Increase R/R
You increase R/R by defining risk, and fitting your position size to that risk.  
For example say you want to buy the bottom in `$SNAP`.  It has been going down ever since it IPO'd.  If last week `$SNAP` hit $10 and bounced to $11, and you think $10 is the bottom, then you can build a trade around this idea.  If you want to lose no more than $50 on the trade, you can buy 50 shares and stop out below $10.  If you are correct and `$SNAP` continues upwards, you can lock in profits along the way by trailing your stop up or selling partials at price targets, ie. $12, $15.

# Reference
[@JMVala_Trades][jm] $300-$10,000 
[@TheTradingNinja][ninja] $150-$50,000




[jm]: https://twitter.com/jmvala_trades
[ninja]: https://twitter.com/thetradingninja





