{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks=pd.read_csv('NFLX.csv')\n",
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume  \n",
      "0   19864.089844  6482450000  \n",
      "1   20812.240234  6185580000  \n",
      "2   20663.220703  6941970000  \n",
      "3   20940.509766  5392630000  \n",
      "4   21008.650391  6613570000  \n",
      "5   21349.630859  7214590000  \n",
      "6   21891.119141  5569720000  \n",
      "7   21948.099609  6150060000  \n",
      "8   22405.089844  6342130000  \n",
      "9   23377.240234  7302910000  \n",
      "10  24272.349609  7335640000  \n",
      "11  24719.220703  6589890000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks=pd.read_csv('DJI.csv')\n",
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "5    2017-01-10  131.270004  132.220001  129.289993  129.889999  129.889999   \n",
      "6    2017-01-11  130.910004  131.500000  129.250000  130.500000  130.500000   \n",
      "7    2017-01-12  130.630005  130.850006  128.500000  129.179993  129.179993   \n",
      "8    2017-01-13  131.149994  133.929993  130.580002  133.699997  133.699997   \n",
      "9    2017-01-17  135.039993  135.399994  132.089996  132.889999  132.889999   \n",
      "10   2017-01-18  133.210007  133.649994  131.059998  133.259995  133.259995   \n",
      "11   2017-01-19  142.009995  143.460007  138.250000  138.410004  138.410004   \n",
      "12   2017-01-20  139.360001  140.789993  137.660004  138.600006  138.600006   \n",
      "13   2017-01-23  138.649994  139.490005  137.309998  137.389999  137.389999   \n",
      "14   2017-01-24  138.110001  140.929993  137.029999  140.110001  140.110001   \n",
      "15   2017-01-25  140.800003  141.389999  139.050003  139.520004  139.520004   \n",
      "16   2017-01-26  140.449997  141.210007  138.509995  138.960007  138.960007   \n",
      "17   2017-01-27  139.460007  142.490005  139.000000  142.449997  142.449997   \n",
      "18   2017-01-30  141.770004  141.970001  138.800003  141.220001  141.220001   \n",
      "19   2017-01-31  140.550003  141.830002  139.699997  140.710007  140.710007   \n",
      "20   2017-02-01  141.199997  142.410004  139.300003  140.779999  140.779999   \n",
      "21   2017-02-02  140.610001  141.039993  139.050003  139.199997  139.199997   \n",
      "22   2017-02-03  139.509995  140.639999  139.100006  140.250000  140.250000   \n",
      "23   2017-02-06  140.000000  141.000000  139.160004  140.970001  140.970001   \n",
      "24   2017-02-07  141.490005  144.279999  141.050003  144.000000  144.000000   \n",
      "25   2017-02-08  143.570007  145.070007  142.559998  144.740005  144.740005   \n",
      "26   2017-02-09  144.979996  145.089996  143.580002  144.139999  144.139999   \n",
      "27   2017-02-10  144.679993  145.300003  143.970001  144.820007  144.820007   \n",
      "28   2017-02-13  145.190002  145.949997  143.050003  143.199997  143.199997   \n",
      "29   2017-02-14  143.199997  144.110001  140.050003  140.820007  140.820007   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "221  2017-11-16  194.330002  197.699997  193.750000  195.509995  195.509995   \n",
      "222  2017-11-17  195.740005  195.949997  192.649994  193.199997  193.199997   \n",
      "223  2017-11-20  193.300003  194.320007  191.899994  194.100006  194.100006   \n",
      "224  2017-11-21  195.039993  197.520004  194.970001  196.229996  196.229996   \n",
      "225  2017-11-22  196.580002  196.750000  193.630005  196.320007  196.320007   \n",
      "226  2017-11-24  196.649994  196.899994  195.330002  195.750000  195.750000   \n",
      "227  2017-11-27  195.559998  195.850006  194.000000  195.050003  195.050003   \n",
      "228  2017-11-28  195.339996  199.679993  194.009995  199.179993  199.179993   \n",
      "229  2017-11-29  198.910004  199.029999  184.320007  188.149994  188.149994   \n",
      "230  2017-11-30  190.309998  190.860001  186.679993  187.580002  187.580002   \n",
      "231  2017-12-01  186.990005  189.800003  185.000000  186.820007  186.820007   \n",
      "232  2017-12-04  189.360001  189.720001  178.380005  184.039993  184.039993   \n",
      "233  2017-12-05  183.500000  188.139999  181.190002  184.210007  184.210007   \n",
      "234  2017-12-06  183.380005  186.479996  182.880005  185.300003  185.300003   \n",
      "235  2017-12-07  185.710007  187.339996  183.220001  185.199997  185.199997   \n",
      "236  2017-12-08  186.500000  189.419998  186.300003  188.539993  188.539993   \n",
      "237  2017-12-11  187.850006  189.419998  185.910004  186.220001  186.220001   \n",
      "238  2017-12-12  186.009995  187.850006  184.820007  185.729996  185.729996   \n",
      "239  2017-12-13  186.100006  188.690002  185.410004  187.860001  187.860001   \n",
      "240  2017-12-14  187.979996  192.639999  187.199997  189.559998  189.559998   \n",
      "241  2017-12-15  189.610001  191.429993  188.009995  190.119995  190.119995   \n",
      "242  2017-12-18  191.199997  191.649994  188.899994  190.419998  190.419998   \n",
      "243  2017-12-19  190.179993  190.300003  185.750000  187.020004  187.020004   \n",
      "244  2017-12-20  187.940002  189.110001  185.259995  188.820007  188.820007   \n",
      "245  2017-12-21  189.440002  190.949997  187.580002  188.619995  188.619995   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "5     5985800      Q1  \n",
      "6     5615100      Q1  \n",
      "7     5388900      Q1  \n",
      "8    10515000      Q1  \n",
      "9    12183200      Q1  \n",
      "10   16168600      Q1  \n",
      "11   23203400      Q1  \n",
      "12    9497400      Q1  \n",
      "13    7433900      Q1  \n",
      "14    7754700      Q1  \n",
      "15    7238100      Q1  \n",
      "16    6038300      Q1  \n",
      "17    8323900      Q1  \n",
      "18    8122500      Q1  \n",
      "19    4411600      Q1  \n",
      "20    6033400      Q1  \n",
      "21    3462400      Q1  \n",
      "22    3512600      Q1  \n",
      "23    3552100      Q1  \n",
      "24    8573500      Q1  \n",
      "25    6887100      Q1  \n",
      "26    4555100      Q1  \n",
      "27    6171900      Q1  \n",
      "28    4790400      Q1  \n",
      "29    8355000      Q1  \n",
      "..        ...     ...  \n",
      "221   5678400      Q4  \n",
      "222   3906300      Q4  \n",
      "223   3827500      Q4  \n",
      "224   4787300      Q4  \n",
      "225   5895400      Q4  \n",
      "226   2160500      Q4  \n",
      "227   3210100      Q4  \n",
      "228   6981100      Q4  \n",
      "229  14202700      Q4  \n",
      "230   6630100      Q4  \n",
      "231   6219500      Q4  \n",
      "232   9069800      Q4  \n",
      "233   5783700      Q4  \n",
      "234   5490100      Q4  \n",
      "235   4659500      Q4  \n",
      "236   4987300      Q4  \n",
      "237   5298600      Q4  \n",
      "238   4265900      Q4  \n",
      "239   4710000      Q4  \n",
      "240   7792800      Q4  \n",
      "241   7285600      Q4  \n",
      "242   5011000      Q4  \n",
      "243   7033000      Q4  \n",
      "244   6545400      Q4  \n",
      "245   4729800      Q4  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly=pd.read_csv('NFLX_daily_by_quarter.csv')\n",
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#2017"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#The data is represented by days in NFLX_daily_by_quarter, and by months in NFLX and DJI CSVs\n",
    "#All of the CSVs show the open, close, adj close, high, low, and volume of the stock or index. Additionally, NFLX_daily_by_quarter shows the respective quater for the day\n",
    "#NFLX_stocks_quarterly has an additional column that designates the quarter the particular day is within. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns={'Adj Close':'Price'},inplace=True)\n",
    "dowjones_stocks.rename(columns={'Adj Close':'Price'},inplace=True)\n",
    "netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'},inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume  \n",
       "0  181772200  \n",
       "1   91432000  \n",
       "2  110692700  \n",
       "3  149769200  \n",
       "4  116795800  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Quarter</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-03</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>128.190002</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>9437900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-01-04</td>\n",
       "      <td>127.489998</td>\n",
       "      <td>130.169998</td>\n",
       "      <td>126.550003</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>129.410004</td>\n",
       "      <td>7843600</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-01-05</td>\n",
       "      <td>129.220001</td>\n",
       "      <td>132.750000</td>\n",
       "      <td>128.899994</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>131.809998</td>\n",
       "      <td>10185500</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-01-06</td>\n",
       "      <td>132.080002</td>\n",
       "      <td>133.880005</td>\n",
       "      <td>129.809998</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>131.070007</td>\n",
       "      <td>10657900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-01-09</td>\n",
       "      <td>131.479996</td>\n",
       "      <td>131.990005</td>\n",
       "      <td>129.889999</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>130.949997</td>\n",
       "      <td>5766900</td>\n",
       "      <td>Q1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close       Price  \\\n",
       "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
       "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
       "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
       "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
       "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
       "\n",
       "     Volume Quarter  \n",
       "0   9437900      Q1  \n",
       "1   7843600      Q1  \n",
       "2  10185500      Q1  \n",
       "3  10657900      Q1  \n",
       "4   5766900      Q1  "
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dowjones_stocks.head()\n",
    "netflix_stocks_quarterly.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax=sns.violinplot(data=netflix_stocks_quarterly, x='Quarter', y='Price')\n",
    "ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')\n",
    "ax.set_ylabel('Closing Stock Price')\n",
    "ax.set_xlabel('Business Quarters in 2017')\n",
    "plt.savefig('DistributionNStock.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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7eYiRo9s5HNfGUH5NacUumlmmdPmmX1ENALTgYeB1cCDEfGSpDslVQFIOktSHfBJ4NuSXkoXPw2olvQfwJPAXRGx6tCtdJ4ufMJxi2bOnMm4ceMoLy9nxowZPPvssyxdupSbb76ZiooK1q9fz9SpU1m4cCGQPDbh1ltv5dxzz6WyspIXXniByy67jJNPPpn7778fSB6l/Cd/8ieceeaZjB8/np/+9KcHt7V+/XoqKiq4+eabAbj77rs566yzKC8v5/bbb++aneyA8mtO4Y6nLmbe2gu446mLHfRmBZLXlbKI+AXwi2Zlt+W8X04yvNN8uWeB8R1sY7t01ROO3377bSoqKg5Oz5o1i0svvZTFixfz8ssvI4mdO3cyZMgQqqqqmDhxItdcc02L6xo1ahS/+c1v+Ku/+iumTp3KM888w549ezj99NOZNm0axcXFLF68mEGDBvHGG29wzjnnUFVVxV133cWLL7548C+MRx55hLVr17Js2TIigqqqKp5++mkuvPDCI99RM+uT+txtEV31hOOWhnEaGxspLi7m85//PB//+Mfz/hrBqqrk4wbjx49n9+7dDBw4kIEDB1JcXMzOnTs57rjjuPXWW3n66afp168fmzdv5vXXXz9kPY888giPPPIIZ5yRXAbZvXs3a9euddib2SH6XNh30ROOW1RUVMSyZct4/PHHWbBgAXPnzuWJJ55oc7mjjz4agH79+h18f2C6sbGRH/7wh2zbto0VK1YwYMAAysrKmjwW+YCIYNasWdx4442dt1Nm1if1uWfjdNETjlu0e/duGhoauOKKK7jnnnsOnvk3f7xxezU0NDBixAgGDBjAk08+yauvvtriei+77DLmzZvH7t27Adi8eTNbt27twB6ZWV/V587sDzzhOPdunM99ruN34zQfs58wYQI33XQTkyZNYs+ePUQE3/zmN4HkW6yuv/567r333oMXZtvj2muv5ROf+MTBxyafeuqpAAwbNozzzz+fD37wg1x++eXcfffdrF69mnPPPReA448/nh/84AeMGDGiYztrZn2OH3GcAT5+Zn2fH3FsZmYOezOzLOg1Yd/Thpt6Cx83M4NeEvbFxcVs377dwdVOEcH27dspLi4udFPMrMB6xd04paWl1NXV4ccft19xcTGlzT9lZmaZ0yvCfsCAAYwZM6bQzTAz67V6xTCOmZl1jMPezCwDHPZmZhnQ4z5BK2kb8Gonre4E4I1OWpd1jPuiZ3F/9Byd1RcnRUSr3+va48K+M0mqPtzHh637uC96FvdHz9FdfeFhHDOzDHDYm5llQF8P+wcK3QA7yH3Rs7g/eo5u6Ys+PWZvZmaJvn5mb2ZmOOzNzDKhx4W9pHmStkp6MadMkr4iaa2kVyT9UlJ5Ou9YSf8q6WVJL0m6K2e5oyX9WNI6Sc9LKkvLh0l6UtJuSXNz6g+UtDLn9Yake7pv73sWSaPS47Q6PbY3peXujwKQVCxpmaT/SI/tV9PyoyTdI2l9emx/Lml0Oq/FPkznDZX0aNqPj0oqSctPlfQbSe9ImpFT/4+a9ccuSV/q7uPQk0jqL+m3kn6eTvfcvoiIHvUCLgTOBF7MKZsO/AI4Np3+GMkHr44DjgUuTsuPAn4FXJ5OfwG4P30/Bfhx+v444CPANGDuYdqyAriw0MekgH1xInBm+n4g8Aowzv1RsP4QcHz6fgDwPHAOMAf4LtA/nfcZ4LckJ3Mt9mE6PRuYmb6fCfxD+n4EcBbw98CMVtrSH/hPkg/yFPzYFLBPvgz8CPh5Ot1j+6LgB6uVxpfRNOw3ASc3q/N94IYWlv1H4Pr0/cPAuen7IpJPqSmn7tTWwgUYm25XR7offe0F/BS41P1R+BfJL9UXgI8C24FBzeb/CvhYa32Yvl8DnJi+PxFY06zuHYcJmI8BzxT6OBS4D0qBx4E/Bn6e9kmP7YseN4zTnKRBwHERsb7ZrGqSs8zcukOAT5B0AMBIkoAgIhqBBmBYnpv+FMmZp29XAtIhlzNIzibdHwWSDhusBLYCjwL1QG1E7GpWtaX+KOO9PgT4g4h4DSD9OaIdTZkCzG9v+/uYe4BbgP3p9AfowX3R48P+MNRkQioi2eF7I2JDS3VS+YaF/zGnJB0PPAQcbkzQ/dENImJfRFSQnFWeTXJMWzqGzfvjYB+2EEbtIukooAr4SUfW05tJmghsjYgVucX04L7o8WGfHoz/kvT+ZrPOJPmNecADwNqIyL2AVweMgoPhMxjY0dY2JX0IKGrWkZkkaQDJP8wfRsQi90fPEBE7gaeAK4GTJA1sVuVgfzTvw5w6r0s6Ma1zIslfC/m4HHghIl4/8j3o9c4HqiRtBBaQDOXcQQ/uix4f9qm7gXslHQMg6RLgdGBhOv2/SIKj+ZnnUuC69P01wBN5DgN8Cp9FIkkkF5tWR8Q3cma5PwpA0vB0aIz02F9CctH6n4FvSOqfzvs0sAd45jB9CE374zqSMeR8ZL4/ImJWRJRGRBnJX51PRMRV9OS+KPRFjhYuNswHXgP2kpwJfo7kz6DbgLXARmALMDTnIkkAq4GV6evz6bxikj9v1gHLgPfnbGcjyVnl7nQ743LmbQBOLfSxKPSL5A6ZAGpyju0V7o+C9Uc5yZ0dNcCLwG1p+dHAvelx3Zwe82MO14fpvGEk11PWpj8P9OEfpn2wC9iZvh+UzjtwEXJwoY9HT3kBF/He3Tg9ti963eMS0vGuxcDyiD6gDvQAAABJSURBVLi10O3JOvdHzyLpD4F/B74VEX7+TQH1tL7odWFvZmbt11vG7M3MrAMc9mZmGeCwNzPLAIe9mVkGOOzNzDLAYW9mlgH/H58iXStx15DaAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41]\n",
    "plt.scatter(x_positions,earnings_actual, color='red', alpha=0.5)\n",
    "plt.scatter(x_positions,earnings_estimate, color='blue', alpha=0.5)\n",
    "plt.legend(['Actual', 'Estimate'])\n",
    "plt.xticks(x_positions, chart_labels)\n",
    "plt.title('Earnings Per Share in Cents')\n",
    "plt.savefig('EarningsPerShare.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "plt.bar(bars1_x, revenue_by_quarter)\n",
    "\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "plt.bar(bars2_x, earnings_by_quarter)\n",
    "\n",
    "\n",
    "plt.title('Revenue vs Earnings for Each Quarter')\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "plt.savefig('RevenuevsEarnings.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.04348657718120806"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#There seems to be a correlation between reveune per quarter and earnings per quarter. As depicted in the above bar graph, earnings per quarter increases when revenue increases.\n",
    "#Approximately 5% of revenue constitutes earnings "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 2880x4320 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "plt.figure(figsize=(40,60))\n",
    "ax1 = plt.subplot(1, 2, 1)\n",
    "plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])\n",
    "ax1.set_title('Netflix')\n",
    "ax1.set_xticks(netflix_stocks['Date'])\n",
    "ax1.set_yticks(netflix_stocks['Price'])\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Stock Price')\n",
    "plt.subplots_adjust(wspace=0.5, top=0.9, bottom=0.7)\n",
    "\n",
    "\n",
    "\n",
    "# Right plot Dow Jones\n",
    "ax2 = plt.subplot(1, 2, 2)\n",
    "plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])\n",
    "ax2.set_title('Dow Jones')\n",
    "ax2.set_xticks(dowjones_stocks['Date'])\n",
    "ax2.set_yticks(dowjones_stocks['Price'])\n",
    "plt.xlabel('Date')\n",
    "plt.ylabel('Stock Price')\n",
    "plt.subplots_adjust(wspace=0.5, top=0.9, bottom=0.7)\n",
    "\n",
    "plt.savefig('NvsDJ2017.png')\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
