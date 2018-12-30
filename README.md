# Firefly algorithm for trading (v0.2)
Optimization algorithm for trading

### What is Firefly?
Firefly is a Nature-inspired metaheuristic optimization algorithm developed by Xin-She Yang at the Cambridge University in 2007 (1). The algorithm follows the flashing patterns and behavior of fireflies. Several research papers have been pubished since then with promising results. Most of them compared it versus other well-know metaheuristic algorithms such as the Genetic Algorithm and Particle Swarm Optimiation with promising results (2,3,4). 

### Firefly for finance v0.2
FA (Firefly) is an efficient method to solve complex problems such as the travelling salesman problem or to optimize computation time for digital image compression. However, little was studied when it comes to finance related problems. Reason why I decided to study it for my master thesis(2013). The main idea for using FA in finance is to find the optimal parameters for the trading system. In my original paperwork, I got decent results. It outperformed the b&H strategy by 4%. (You can find my original paperwork with the results here.). 

However, my paper got lots of drawbacks such as the use of VBA and Excel for the testing/developing environment, or the usage of poor datasets with biases. Also, the algorithm was only backtested on small population sets with limited time series. Mainly, what lacked  was several performance metrics and stress events to truly measure the algorithm.

Since then, computer performance improved and developing tools became lighter and faster. With the rise of AI and ML, decreasing transaction costs, and better developing tools, I decided to study/test again the performance in the actual market. 

### Summary of New features
- Python in conjunction with libraries such as Numpy, Pandas and matplotlib for graphs. 
- Jupyter notebooks
- [x] Custom coded Backtesting system **Done**
- [ ] Algorithm Classes (Strategy.py, Portfolio.py, Performance.py)
- Different sorting algorithms(Bubble) and test performances
- New datasets sources to remove Biases
- Different populations(S&P500, single stocks, portfolio of stocks
- Different time series(Daily, hourly) 

- Different transactions costs
- Biases taken into account such as (...
- New strategies(MA Cross,...) compared to v0.1(MA)

- Performance stats (Sharpe Ratio, Maximum drawdown, VaR,  Beta, ...
- Datasets stats(seasonality, ...)
- Tested on Stress events
- Graphs to see potential correlations

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2


- Python in conjunction with libraries such as Numpy, Pandas and matplotlib for graphs. 

In the original work, VBA was the language used due to lack of ressources and computer performance. The algorithm performed well but the design of the algorithm and the backtesting environment which was Excel was prime of errors and long development. Fragile. 
Python is used because it is a very fast language to put an idea into code and comes with lots of fast and easy frameworks which makes it an amazing tool for backtesting trading strategies. 

- Jupyter notebooks

I used Excel at that time as it was an easy tool to perform quick and various data analysis. It is widely used in the corporate world. However, when it comes to large data sets or deep analysis for trading systems eg., I encountered several problems such as performance issues, development problems and difficulty to share identical results with my supervisor.  
 
Jupyter Notebook resolves all these issues. It's a web application that was recently developed and contains lots of features. It's biggest advantage is it allows you to create and share documents that contain live code, equations, visualizations and narrative text. Another big force  is its interactiveness and easy big data integrations which makes data analysis super easy. Eg. data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning all these can be done in few simple line codes.

In other words, it's a perfect research environment for data analysis and therefore for backtesting trading strategies.

- Custom coded object-oriented Backtesting system **Done**

Backtesting was done on Excel on my original paper. It contained lots of pitfalls such as poor execution and biases. Excel backtesting did not include any reference to portfolio/risk management. The decision to code my own backtesting system is to have a better command on different parameters such as the risk portfolio or the capital requirements. But mainly, to be able to reuse the code without the need to rewrite the whole strategy. Different components such as Risk management, Portfolio and Strategy are seperated which results in better algorithm/strategy management. Add-ons can also be easier implemented versus a  
It forces you to consider all aspects of your trading infrastructure such as fees, risk management, position sizing, etc.

- Backtesting components (Strategy.py, Portfolio.py, Performance.py)

Strategy - A Strategy class receives a Pandas DataFrame of bars, i.e. a list of Open-High-Low-Close-Volume (OHLCV) data points at a particular frequency. The Strategy will produce a list of signals, which consist of a timestamp and an element from the set {1,0,−1}
 indicating a long, hold or short signal respectively.

Portfolio - The majority of the backtesting work will occur in the Portfolio class. It will receive a set of signals (as described above) and create a series of positions, allocated against a cash component. The job of the Portfolio object is to produce an equity curve, incorporate basic transaction costs and keep track of trades.

Performance - The Performance object takes a portfolio and produces a set of statistics about its performance. In particular it will output risk/return characteristics (Sharpe, Sortino and Information Ratios), trade/profit metrics and drawdown information.

- Test different sorting algorithms(Bubble) and test performances

Original FA code uses the bubble sort algorithm. Other sorting algos will  be used to test the performance

- New datasets sources to remove Biases

Original paper uses raw data from Yahoo finance but contained biases such as(). I will use Morningstar.

- Different populations(S&P500, single stocks, portfolio of stocks

Original paper tested the trading strategies on  S&P500. This, which is a good comparison  as it's used predominatnely in papers. I would like to test the optimization on single stocks and a portfolio of stocks to measure the performance.

- Different time series(Daily, hourly)

Original paper used daily and monthly. I would like to test hourly. 

- Different transactions costs

Static transaction costs were tested. I would like to test different transactions costs as they lowered these past years

- Remove/reduce Biases

Biases such as survivorship were included in the datasets.

- New strategies(MA Cross,...) compared to v0.1(MA)

Original paper, the strategies used were.... I would like to test these again plus use a single strategy calles MA Cross as it is considered useful for calibrating

- Performance stats (Sharpe Ratio, Maximum drawdown, VaR,  Beta, ...

Little metrics were used in  original paper(...). In v0.2, I will measure ....

- Datasets stats(seasonality, ...)

Others stats to measure are ...

- Tested on Stress events

Stress events are useful to see if the algo performs well in different scenarios. sdfdf framework written in Pythin allows you to easy performthese tests.

- Graphs to see potential correlations

No graphs were used in original paper. This time, I will use the Pandas framweork to see any potentiona  correlations and .

### Results
coming soon...
See the the following Jupyter link to test and train the

### Conclusion
coming soon...Faster

### Future developments
In the near future, I will use the Firefly algorithm in an event-based live environment and compare the results. Also, I would like to use it with different trading strategies and see which of them performs better. Lastly, I would like to integrate some ML variables in the Firefly algorithm
