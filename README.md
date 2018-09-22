    $$\                       $$\ $$\                     $$\   
    $$ |                      $$ |$$ |                  $$$$ |  
    $$$$$$$\   $$$$$$\   $$$$$$$ |$$ |      $$\    $$\  \_$$ |  
    $$  __$$\ $$  __$$\ $$  __$$ |$$ |      \$$\  $$  |   $$ |  
    $$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |       \$$\$$  /    $$ |  
    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |        \$$$  /     $$ |  
    $$ |  $$ |\$$$$$$  |\$$$$$$$ |$$ |         \$  /$$\ $$$$$$\ 
    \__|  \__| \______/  \_______|\__|          \_/ \__|\______|

# hodl

View those heavy bags of yours all in one place.
_This simple script provides a detailed overview of your cryptocurreny exchange accounts without the need to login._ 

**Supported Exchanges:**
* Bittrex
* Poloniex


## Setup

Setting up a virtual environment for a project allows us to easily keep our Python package versions consistent across anyone who works on or runs this project as well as isolates the projects packages from our individual global Python environments. 



### Prerequisites 
* `Python3.6`

#### Python installation (macOS) 

- Install [Homebrew](https://brew.sh/):

    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
  
  
- Install Python 3.6.2 using Homebrew:

    ```
    $ brew install python3
    ```
  
  
- Updating Python3 to 3.6.2:

    ```
    $ brew upgrade python3
    ```

----------------------

### Workspace Setup

1. Create a directory to store your virtual environments:

    ```
    $ mkdir ~/.virtualenvs
    ```

2. Create the virtual environment (assuming you have Python 3.6.2 installed):

    ```
    $ python3 -m venv ~/.virtualenvs/hodl
    ```

3. Activating the virtual environment:

    ```
    $ source ~/.virtualenvs/hodl/bin/activate
    ```

    - _**Note:** While the virtual environment is active you will not have access to your global Python packages. When you are done working, deactivate the virtual environment:_ `$ deactivate`


4. Install packages to a virtual environment using the requirements.txt file (assuming the virtual environment is active and the requirements.txt file is in your current directory):

    ```
    $ pip install -r requirements.txt
    ```

----------------------

### PyCharm Setup (for developers)

1. Select **PyCharm** in the menu bar, click **Preferences**.
2. In the left pane, enter Project Interpreter in the search box, then click **Project Interpreter**.
3. In the right pane, click the **gear icon**, click **More�**.
4. In the Project Interpreters dialog box, click the plus sign **+**, click **Add Local**.
5. Enter `~/Users/{username}/.virtualenvs/hodl/bin/python` in the path. Click **OK**.

----------------------

### Exchange Setup


1. Create a new set of API keys with trading enabled under settings.
    * Ensure that withdrawals are **not enabled**! 
    * Note: _As an added layer of security you can restrict API keys to a known IP address._
2. Duplicate  `/conf/credentials_example.ini`, rename to `/conf/credentials.ini` and add your new API keys.
    
    _Copy and rename the credentials configuration file:_
    ```
    $ cp conf/credentials_example.ini conf/credentials.ini
    ```
3. Add API keys to `conf/credentials.ini`:

    _Edit the text file with nano (or your favorite text editor):_
    ```
    $ nano conf/credentials.ini
    ```
    * `control+o` to save the file 
    * `control+x` to exit nano editor
    
    **DO NOT USE QUOTES AROUND YOUR API KEYS OR LOGIN INFO**
 
 ----------------------
 
### Settings Configuration 

1. Take a look at the parameters located in the settings file `conf/settings.ini`

    ```
    $ nano conf/settings.ini
    ```
     _Here you can customize which exchanges are turned on._
    * _For each exchange with API keys, set the corresponding connection to `on`._

 ----------------------

## Running 

To use `hodl` you must first follow all of the above instructions. 


1. Start your `virtualenv` from inside the project directory

    ```
    $ source ~/.virtualenvs/hodl/bin/activate
    ```
2. Run `hodl.py` with one of the supported flags

    ```
    $ python3 hodl.py --overview
    ```
    or 
    ```
    $ python3 hodl.py --detailed
    ```

*Required Flags (use only one):*

- `--overview`  : Print total and available btc balance overview
- `--detailed`  : Print verbose account balances of all your bags
- `--poloniex`  : Print only Poloniex balances
- `--poloTradeHist` : Print only Poloniex Trade History
- `--bittrex`   : Print only Bittrex balances
- `--bittrexTradeHist`   : Print only Bittrex Trade History


    
_You should immediately see feedback from the console suggesting `hodle` has started._

## Example Output:


#### Overview:

        ===================================================================
        Balances By Account (BTC)
        
          Poloniex  --- Available: 0.18786449 --- Account Value: 0.59695743
           Bittrex  --- Available: 0.14733282 --- Account Value: 0.40584864
        -------------------------------------------------------------------
        Percentage of balance at each exchange: 
        
          Poloniex  --- % 59.53
           Bittrex  --- % 40.47
        -------------------------------------------------------------------
        Percentage of account in BTC: % 33.42
        ===================================================================
        Total estimated value of all accounts: 1.00280607 BTC
        ===================================================================


#### Detailed:
        
        $$\                       $$\ $$\ 
        $$ |                      $$ |$$ |
        $$$$$$$\   $$$$$$\   $$$$$$$ |$$ |
        $$  __$$\ $$  __$$\ $$  __$$ |$$ |
        $$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |
        $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |
        $$ |  $$ |\$$$$$$  |\$$$$$$$ |$$ |
        \__|  \__| \______/  \_______|\__|
                                                      
           $$$$$$$\ $$\   $$\ $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
          $$  _____|$$ |  $$ |$$  _$$  _$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ $$ |  $$ |
          \$$$$$$\  $$ |  $$ |$$ / $$ / $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  \__|$$ |  $$ |
           \____$$\ $$ |  $$ |$$ | $$ | $$ |$$ | $$ | $$ |$$  __$$ |$$ |      $$ |  $$ |
          $$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$$ |$$ |      \$$$$$$$ |
          \_______/  \______/ \__| \__| \__|\__| \__| \__| \_______|\__|       \____$$ |
                                                                              $$\   $$ |
                                                                              \$$$$$$  |
                                                                               \______/ 

        
        
        ______     _             _           
        | ___ \   | |           (_)          
        | |_/ /__ | | ___  _ __  _  _____  __
        |  __/ _ \| |/ _ \| '_ \| |/ _ \ \/ /
        | | | (_) | | (_) | | | | |  __/>  < 
        \_|  \___/|_|\___/|_| |_|_|\___/_/\_\
        ----------------------------------------------------------------------------------------------------------
        Available BTC Balance: 0.18786449
        ----------------------------------------------------------------------------------------------------------
         --- BTC    ---  available:      0.18786489 ---  onOrders:      0.00000000 ---  btcValue:  0.18786449 ---  
         --- DASH   ---  available:      1.33335389 ---  onOrders:      0.00000000 ---  btcValue:  0.11050837 ---  
         --- GNO    ---  available:      2.32882238 ---  onOrders:      0.00000000 ---  btcValue:  0.02186042 ---  
         --- LBC    ---  available:   2366.41359120 ---  onOrders:      0.00000000 ---  btcValue:  0.06526568 ---  
         --- MAID   ---  available:   1190.47924221 ---  onOrders:      0.00000000 ---  btcValue:  0.08032163 ---  
         --- USDT   ---  available:    202.38048848 ---  onOrders:      0.00000000 ---  btcValue:  0.03384206 ---  
         --- XMR    ---  available:      4.57487942 ---  onOrders:      0.00000000 ---  btcValue:  0.09729478 ---  
        ----------------------------------------------------------------------------------------------------------
        Account Value: 0.59695743 BTC
        ----------------------------------------------------------------------------------------------------------
        Open orders: 
            open orders will print here..>
        
        
        
        ______ _ _   _                 
        | ___ (_) | | |                
        | |_/ /_| |_| |_ _ __ _____  __
        | ___ \ | __| __| '__/ _ \ \/ /
        | |_/ / | |_| |_| | |  __/>  < 
        \____/|_|\__|\__|_|  \___/_/\_\
        ---------------------------------------------------------------------------------------------------------
        Available BTC Balance: 0.14733282
        ---------------------------------------------------------------------------------------------------------
         --- STRAT  ---  balance:    113.16973733 ---  available:    113.16973733 ---  btcValue:  0.05474020 ---   
         --- WINGS  ---  balance:    581.43092329 ---  available:    581.43092329 ---  btcValue:  0.03615919 ---  
         --- APX    ---  balance:      0.76970147 ---  available:      0.76970147 ---  btcValue:  0.00084735 ---  
         --- PTOY   ---  balance:   2500.00000000 ---  available:   2500.00000000 ---  btcValue:  0.05952500 ---  
         --- OMG    ---  balance:     55.17539130 ---  available:     55.17539130 ---  btcValue:  0.06182182 ---  
         --- PART   ---  balance:     38.46638769 ---  available:     38.46638769 ---  btcValue:  0.04542226 ---  
        ---------------------------------------------------------------------------------------------------------
        Account Value: 0.40584864 BTC
        ---------------------------------------------------------------------------------------------------------
        Open orders: 
            Market: BTC-GBYTE --- Order Type: LIMIT_BUY --- Qty:      0.68277086 --- Qty Remaining:      0.68277086
        
           _____                                           
          / ___/__  ______ ___  ____ ___  ____ ________  __
          \__ \/ / / / __ `__ \/ __ `__ \/ __ `/ ___/ / / /
         ___/ / /_/ / / / / / / / / / / / /_/ / /  / /_/ / 
        /____/\__,_/_/ /_/ /_/_/ /_/ /_/\__,_/_/   \__, /  
                                                  /____/   
        ===================================================================
        Balances By Account (BTC)
        
          Poloniex  --- Available: 0.18786449 --- Account Value: 0.59695743
           Bittrex  --- Available: 0.14733282 --- Account Value: 0.40584864
        -------------------------------------------------------------------
        Percentage of balance at each exchange: 
        
          Poloniex  --- % 59.53
           Bittrex  --- % 40.47
        -------------------------------------------------------------------
        Percentage of account in BTC: % 33.42
        ===================================================================
        Total estimated value of all accounts: 1.00280607 BTC
        ===================================================================




## Donations Welcome
* **BTC** `1KWb1gP9QA2bT1fWB9B6a9C6AaBoXW92AF`
* **ETH** `0xe6fCee44C2372B1402008b29c3bC82A0309737F0`
* **LTC** `LPpo6YmsA1dJeyvGS47DUqEmmVPvjoAJUE`


