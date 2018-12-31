# Firefly algorithm (v0.2)
Optimization algorithm for trading


## What is Firefly?
`Firefly` is a Nature-inspired metaheuristic optimization algorithm developed by Xin-She Yang at the Cambridge University in 2007 [^1]. The algorithm follows the flashing patterns and behavior of fireflies. Several research papers have been pubished since then with promising results. Most of them compared it versus other well-know metaheuristic algorithms such as the Genetic Algorithm and Particle Swarm Optimiation with promising results[^2] [3][4][5]. 

## Introduction
FA (Firefly) is an efficient method to solve complex problems such as the travelling salesman problem or to optimize computation time for digital image compression. However, little was studied when it comes to finance related problems. Reason why I decided to study it for my master thesis(2013). The main idea for using FA in finance is to find the optimal parameters for the trading system. In my original paperwork, I got decent results. It outperformed the b&H strategy by 4%. (You can find my original paperwork with the results here.). 

However, my paper got lots of drawbacks such as the use of VBA and Excel for the testing/developing environment, or the usage of poor datasets with biases. Also, the algorithm was only backtested on small population sets with limited time series. Mainly, what lacked  was several performance metrics and stress events to truly measure the algorithm.

Since then, computer performance improved and developing tools became lighter and faster. With the rise of AI and ML, decreasing transaction costs, and better developing tools, I decided to study/test again the performance in the actual market. 

## Summary of New features

| Original paper| v0.2          |
|:-------------|:-------------|
| VBA           | Python        |
| Excel      | Jupyter notebooks      |
| Bubble sort | Other sorting algorithms (Bubble,Radix,Heat,...) |
| High Biased datasets | Low  biases datasets |
|S&P500 benchmark | Single stocks and portfolio |
|Time Series(Daily,Monthly) | Hourly|
|Fixed Transactions costs | Variable Transaction costs|
|MA, MACD, TRB, PT strategy | MA Cross strategy|
||Custom coded object-oriented Backtesting system|
||Performance stats (Sharpe Ratio, Maximum drawdown, VaR,  Beta, ...|
||Datasets stats (seasonality, ...)|
||Tested on Stress events|
||Graphs to see potential correlations|


## Results
coming soon...
See the the following Jupyter link to test and train the

## Conclusion
coming soon...Faster

## Future developments
In the near future, I will use the Firefly algorithm in an event-based live environment and compare the results. Also, I would like to use it with different trading strategies and see which of them performs better. Lastly, I would like to integrate some ML variables in the Firefly algorithm

Footnotes

#### ² Note Two
[²]:#-note-two
