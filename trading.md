---
layout: post
title:  "Trading Reference"
---

If someone asks me about trading, I usually can't give a good answer because I'm not sure where to start.  Knowledge can be really amorphous in your head.  What are the main topics, and how are they related?

So I decided to write it out.  Over the course of several weeks I expanded several sections and reflowed the writing.  This reference now has a dedicated page and receives routine edits.  Check back as it expands into a corpus of knowledge.

* TOC
{:toc}

# Markets
There are 6 markets to trade: OTC, equities, futures, commodities, cryptocurrencies, and options.

- OTC, over-the-counter, "pinks", and penny stocks are all names for the same thing.  These equities are not big enough to trade on a regulated exchange.  These low quality stocks tend to lay dormant for years, and spike on news.  Since prices can be as low as hundredths of a penny, leverage is built into the product.

- Equities refers to exchange traded stocks.  This is the most common vehicle for investing and trading.

- Futures are dated based on month and are the market's best guess of future value.  These trade 24/7.
- Commodities are futures contracts for amounts of commodities such as hog, corn, sugar, coffee.  These also trade 24/7.

- Cryptocurrencies are blockchain based digital currencies.  `$BTCUSD`, `$ETHUSD`, and `$LTCUSD` are the most common currently.


# Styles
There are 2 trading styles: investing and price action trading.  

Here's what I've tried:

|                  | Investing | Price Action Trading |
|------------------|----------:|---------------------:|
| OTC              |           | 1 year               | 
| Equities         | 6 years   |                      |
| Commodities      |           |                      |
| Futures          |           |                      |
| Crypto           |           | 1 year               |
| Options          |           | 2 years              |

What's the difference between the styles?

## Investing
Investing involves fundamental analysis and a fair value, with the assumption that over time the market will reflect actual value.  Maybe you remember some fundamental valuation models from school, such as DCF (Discounted Cash Flow) and CAPM (Capital Asset Pricing Model).

Investing has no opinion about short term price movement, and may encourage adding to losing positions as the stock is "cheaper."  The art is in distinguishing between a cheaper yet still sound investment, and an investment that is no longer valid.  Time horizon is long term.  

The two approaches to investing are Growth and Value.  

Growth looks for strong earnings.  

Value looks for undervalued instances.
There are various measurements value investors use in assessing a stock's value.

- Price/Equity 
- Price/Book
- Debt/Equity

These are calculated from the company's released financial statements:
- Cash Flow Statement
- Balance Sheet
- Income Statement


I have maintained a passive portfolio for 6 years, as well as a 401k, but I do not manage either of them.  They are diversified across low-fee ETFs.

## Price action trading
Price action trading is the focus of this reference. A trade is a "swing" if it is medium-long term, while it is a "scalp" if it is short term. (usually intraday)

Price action trading looks at price action to find prices that offer good risk/return versus an area of support or resistance.  It uses a systematic approach.

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

An option's strike is the price you can execute the option at:
- A call option is OTM (out-of-the-money) if the underlying > strike.
- A call option is ATM (at-the-money) if the underlying = strike.
- A call option is ITM (in-the-money) if the underlying < strike.

Risk is premium paid.  Premium is based on the underlying price relative to the contract strike, the underlying volatility, and the contract's time to expiration.  

Therefore, as opposed to equities where you only lose money if price goes against you, an option buyer loses money (premium decreases) if:
1. Price goes against you
2. Volatility decreases
3. Time decays

As a result of those factors, specific types of moves are suited to option buyers.
**Look for fast directional moves as early as possible without decreasing odds.**  Price goes with you and volatility increases, while time decays only slightly.   

How does this work across trade styles?
- An aggressive scalp setup ("Lotto") is an out-of-the-money weekly option.  This position is low probability because the stock needs to move a lot in a little time.  Therefore the option is cheap.
- A conservative swing setup ("LEAP") is an in-the-money long-term option.  This position is high probability because the stock has wiggle room and lots of time.  Therefore the option is expensive.

There's no free lunch - Trades that have a high probability of working have a low payout, and trades that have a low probability of working have a high payout.

The advantage of options is the ability to specifically express your level of certainty of a given price move in a given time. 

(Options on equities are not bought to directly take advantage of volatility increases.  This can be accomplished by going long the volatility index (VIX) through ETFs such as 1x `$VXX` and 3x `$UVXY`.)

### Advantage of option over stock
Say you think $AAPL is going to go up from $150 to $160 during the special event this week.  This idea can be traded with a stock, or with an option.  
You could spend $15,000 on 100 shares for a potential return of $1000.  `1000/15000 = 6.6% return`
Or you could buy a weekly call option with 150 strike for $2 per share est.  This would cost $200 for 100 shares and would increase to $10+ per share on a move to $160, or $1000+ potential return. `1000/200 = 500% return`
If Apple announces that they are getting out of the computer business and the stock drops to $100. The equity position would lose $5,000 ($15k-10k) but the call option would only lose its premium, $200.

Some powerful stuff!

# Characterizing risk
Risk is the possibility of loss.  Any activity is inherently risky.  But people still drink, smoke, drive cars, eat BBQ, and do other "risky" things.  Trading is definitely risky.

Taking risk on is the only way you can do anything in life.  There's the risk of dying, the risk of taking a big loss, the risk of missed opportunities.  **You only learn by taking on risk.**

How do you operate in a risky environment?  When driving, you reduce the risk of dying by wearing a seatbelt.  

When managing multiple positions, you diversify across uncorrelated assets.  This keeps exogenous factors from causing a drawdown across holdings, therefore decreasing portfolio risk.  See [Efficient frontier][ef] on Wikipedia for a better explanation.

When managing a single position, you set a stop loss.  
This is the max amount you can lose.  **How much are you really OK with losing?**  

You will not win every time.  So you need to have a "bad plan" or a way to manage your position if it goes against you.  

It is very easy to rationalize a bad position and hold onto a losing position, hoping it will return.  This is called "holding the bag."  The problem with this approach is: if you are trading price action, and price has decreased more than you expected, you have received bearish info which further invalidates your trade idea.  So remaining in the position is not a sound trading move, it is purely emotional.

Since trading is systematic, the goal is to remove as much emotion as possible.  An emotional trader will buy the top, sell the bottom, scalp a swing, etc.  

Let's be real: since it's real money, there will always be emotion.  The goal is to trade safely, so your emotions are not in control.  

The best way to approach a trade is to accept the loss ahead of time.  **Your default mindset should be that you will be wrong.**  This way, you are not micromanaging the trade or scalping a promising swing.

You put your stop at a level of support if you are long, or a level of resistance if you are short.

## Market dynamics
What does support and resistance mean, or more precisely how do you assert where these are?  Before we talk about these concepts, we first have to build our basis in the understanding of market dynamics. 

### Mean reversion
Any series will tend to revert to its trend over time, simply due to the definition of a trend.  Once the series extends beyond statistical norms, odds are it will revert.   

### The auction
Any series can be analyzed with an understanding of the underlying phenomenon.  In this instance, it's a market.

Markets are made up of buyers and sellers at an auction.  This is the reason price analysis has predictive value - it allows you to identify where buyers and sellers are positioned.  
Participants have a trade idea and are positioned accordingly.  Buyers are at support, and sellers are at resistance.  

#### Memory
Since these participants are acting on all timescales short and long, there is a memory to the market.  Positions persist over time, so areas of reversal in the past remain significant going forward.  This is another reason why charts are so intuitively useful, especially on longer timeframes.

### Support and resistance
Support and resistance are important concepts in price action trading.  Once identified, you want to enter longs at support and exit at resistance, and enter shorts and resistance and exit at support.

Support and resistance are horizontal or diagonal lines extending along local lows and highs.  Their slope indicates relative demand and supply. **Horizontal lines are more reliable than diagonal lines, as the participants are "holding the line" on their position, not being forced to adjust to new levels.**

If price retraces and retests support, price will be absorbed by the stops of all the buyers who bought at that level.  If there are more sellers now than buyers previously, price will break below the level.  

If price pushes up against resistance, it will absorbed by the stops of all the sellers at that level.  If there are more buyers now than sellers previously, price will break above that level.

For example, an upsloping support line means higher lows, which means each time sellers have attempted to break down price, buyers have stepped in before their previous buy point to defend their positions.  There are more and more buyers.  

A horizontal resistance line is like a brick roof.  Imagine mario jumping to break through it.  Each time it is tested, more sellers stop out - the roof gets weaker.

## Measuring risk
Whether trading or investing, you must size your positions appropriately.  

As a rule of thumb, each position should risk 2% of your portfolio.  More risk means more emotions and exposure to exogenous factors unrelated to your trade thesis.  

A portfolio of $10,000 therefore could risk $200.  

### R
Each trade is measured by R - how many units of risk you won or lost on the trade.  
`R = (profit or loss)/(risked amount`

For example say you want to buy the bottom in `$SNAP`.  It has been going down ever since it IPO'd.  If last week `$SNAP` hit $10 and bounced to $11, and you think $10 is support and $15 is resistance, then you can build a trade around this idea. 

If you want to lose no more than $50 on the trade, you can do two things:
- buy 50 shares and stop out below $10.  If you are correct and `$SNAP` continues upwards, you can lock in profits along the way by trailing your stop up or selling partials at price targets, ie. $15, a 5R trade.
- buy a weekly 10 call option around $120 and set a stop at $70.  If `$SNAP` hits $15 the option will be worth at least $500, a 10R trade.


### Expectancy
The overall goal is to maximize your overall expectancy.  
`Expectancy = (P(Win) * Avg(Win)) - (P(Loss) * Avg(Loss))`

*If you win 50% of trades and win 1R per trade, your expectancy is 0.
If you win 30% of trades and win 2.5R per trade, your expectancy is 10%.*

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

# Price Charts
Charts are visualizations of price action.  There are several types beyond the default line chart.  Besides the Candlestick chart, two other charts are common.  
Heikin Ashi charts show trend reversals.  
Bar charts reduce noise for long term trades.

The most common type of chart for traders is the Candlestick chart.  A candlestick chart divides price action into periods, usually 5m, 1hr, or 1d in length.  
Each of these candlestick bodies contain info: `Open, High, Low, Close`  The longer the period contained by the candlestick, the more significant its levels are.  

As charts can be viewed on various timeframes, any timeframe can be traded.  Shorter timeframes are more volatile and subject to noise.  Longer timeframes are more reliable, but may not help intraday.  

## Trade setups
As uncorrelated assets reduce risk in a portfolio, trade ideas can be strengthened by multiple sources of uncorrelated confirmation.  A way to be more confident in a trade is to find confluence between indicators, timeframes, and trading styles.

There are several general shapes which price action will take, given a market condition, that indicates specific information.
- Head and Shoulders
This is a bearish (sell signal) pattern that is characterized by a three highs, with H1 even with H3 and H2 above both.  This is what major tops look like.
- Inverse Head and Shoulders
This is the opposite of the H&S as a buy signal, with L2 below L3=L1.  This is usually a reliable bull signal to the top of the initial selling before L1.
- Flag
This is a channel that develops following a bullish or bearish move.  It is a continuation signal on a break.
- Pennant
This is a triangle of narrowing support and resistance that develops after a move.  It is usually a continuation move, and includes the time of continuation at the intersection of S/R.
- Rising Wedge
Rising wedges tend to develop at the end of uptrends as a reversal signal.  Their vertice formed by S/R is the point of expected directional shift.
- Falling Wedge
Falling wedges are a very reliable method of buying bottoms.  They are a bullish reversal signal at the intersection of S/R and are often reliable to the top of resistance's first point.

2 common methods of finding reliable moves is buying dips in uptrends or selling rips in downtrends, or buying breakouts.  The former is better in shorter timeframes or to trade around positions, while the latter is a longer timeframe approach for entering holding positions. (investments)

### Buying dips and selling rips
BTFD (buy the fucking dip) or less commonly STFR (sell the fucking rip) is very counterintuitive but essential to grasp in today's markets.  BTFD has been working since early 2016 as the market has trended up strongly.  STFR works in bear markets.  

In order to do the above, you need to identify the market trend, then identify support and resistance.  

In a bull market, support and resistance will likely form either a channel, a flag, or a pennant.  This simple strategy can be used within the the pattern created by support and resistance, or aggressively on breaks of the pattern by assuming the break is false.
Buy at or beyond support, and sell at or beyond resistance.  

### Buying breakouts
To buy a breakout, first you have to identify it.  Start on higher timeframes like the weekly chart and find levels of resistance.  If price has not been able to get past $200 in several years, a break above $200 would be meaningful.  If, after a series of higher lows, price breaks above $200, that's a bullish move.  Bullish moves signal a surplus of buyers vs sellers.  Therefore, trading this setup would give a higher than average win rate.
Additionally, you could go into the lower timeframes and confirm price continuation.
As price often will retest the breakout area, some traders will use the breakout-retest as their primary signal to get long.  This eliminates the mean reverting reversal that is common after the strong rip from the breakout buyer/seller imbalance.

## Indicators
Indicators are price calculations with a trailing period. They are used to build trade confidence, and define risk.  

The reason indicators work, in my opinion, is their succinct capture of human trading psychology.  Charts as a visual system enable the viewer to estimate the relative significance of price moves.  Indicators are derived from this price, summarizing specific aspects of the price movement.  They are like business reports, enabling a higher level view into the data.  Of course, they are not all always relevant.  But if you know the correct conditions under which to apply an indicator, they do accurately predict participant reactions.

The reason why price tends to react *exactly* to indicator values is hard to identify.  It is partially due to the snowball effect of their usage, wherein more participants relying on these indicators increases their significance.  

We *could* be just collectively imagining it.

I use moving averages and fibonacci levels.  Here are some of the others:

- `VWAP` (volume weighted average price)
- `KC` (keltner curves)
- `BB` (bollinger bands)

- `RSI` (relative strength index)
- `MACD` (moving average convergence divergence)
- `%R` (william's %R) 

- `ATR` (average true range)

### Moving averages
Moving Averages are lines used as dynamic support/resistance.  
ie. Longs are valid above the Moving Average, while Shorts are valid below the Moving Average.  

The most common Moving Averages to see are 8 and 21 for short term trading and 50 and 200 for long term trading.  5, 10, 14, and 30 are also used.

Stocks in a short term trend hold the 8 and 21 MA, while stocks in a long term uptrend hold the 50 and 200 MA.  A price break of the lower MA (8, 50) indicates caution and a break of the higher MA (21, 200) indicates a trend reversal.  These signals are especially reliable on a break below followed by a retest that rejects closely below the MA.

Important to note, Moving Averages vary depending on timeframe.  So they move around if you change timeframes.  For example, a 8MA on the 15m chart is equal to 24MA on the 5m chart because it contains 120 minutes.

Moving averages can be exponential (EMA) or simple (SMA) depending on preference.  It makes little difference.

### Fibonacci levels
Fibonacci Levels are from the Fibonacci sequence where each number (after two 1's) is the sum of the two before it.  This growth pattern shows up in nature such as plants.  
Its application in the market is in measuring moves.

The levels are: `23.6%, 38.2%, 50%, 61.8%, 100%, 161.8%, 261.8%..`
The rule of thumb is if a pullback holds the .618 (61.8%) of the move, that's a healthy move.

Of course, it makes some non-fancy sense that 61.8% would be an approximate good place for a trade to hold, as it's a little less than 2/3.  But that doesn't account for the numerous instances of price reversing directly (to the .01) at the various fibonacci levels.

Breakouts tend to extend from 100% to 161.8% and 261.8% as upside targets.

# Edge
Of course, you didn't show up to lose.  You have to define your edge.  Edge emerges from a combination of factors - trade selection, risk control, trade management.

Edge can be defined ahead of time with backtesting, but plenty of issues arise with backtest reliability, including in-sample size, out-of-sample testing, and controlling for relevant factors.  

Edge can be refined over time with a trade journal, by trading small and documenting your success factors and risk factors.  Once you see what works, you can capture this edge and automate away your risk.

With a defined edge, you can stop avoiding risk and move towards risk.

# Trading Systems
Trading systems are modularized and cover the full process, from trade ideas to trading and journaling.  Here are two systems I've seen described.  They are both full stack from generation to tracking.

System 1:
- Backtesting
- Trading Signals
- Risk and Position Management
- Portfolio and Order Management
- Execution
- Reporting

System 2:
- Price Stream
- Trading Strategy
- Risk Management
- Execution Handler
- Logging

If you are interested in building a trade system, start pulling some basic data into [Google Sheets][gs] and running backtests on [Quantopian][quant].

Frankly, you need a lot of money and patience to trade fully automated.  I trade by hand and am testing various strategies in real time.  No point in automating something if it doesn't make money, right?

# Reference
[Twitter List of Traders][list]

[ef]: htts://en.wikipedia.org/wiki/Efficient_frontier
[list]: https://twitter.com/ale627/lists/trading-whitelist
[gs]: https://google.com/sheets
[quant]: https://quantopian.com






