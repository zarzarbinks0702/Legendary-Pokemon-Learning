# Legendary-Pokemon-Learning
Machine learning project classifying pokemon from all 8 generations based on type and legendary status. 

# Objective
    In this project, we aim to analyse existing data to classify pokemon into Legendary or Non-Legendary.

    Using scikit-learn and multiple ML classification types, we are seeking to determine the best model for this task.​

       * Logistic regression​

       * KNN​

       * Neural Network​

       * Random Forest​

       * SVC ​


#  Our data set

    We found our dataset on kaggle that contained Pokemon from Generations 1-8. 
       
        * (https://www.kaggle.com/tlegrand/pokemon-with-stats-generation-8) 
        
    This dataset contained 13 columns of data which we precleaned and sort into Generations 1-6, 7, & 8. These dataframes were then saved to our database via Sqlite.


# Training / Testing

    Each model was trained using the data from Generations 1-6. 
    
        We used these variables as x values in our algorithm to determine Legendary Status (LEGENDARY_FLAG column) of Pokemon.​

            * 'TYPE1', 'TYPE2', 'ABILITY1', 'ABILITY2', 'ABILITY_HIDDEN', 'HP', 'ATK', 'DEF','SP_ATK', 'SP_DEF', 'SPD', 'TOTAL', 'CAPTURE_RATE'

    Generations 7 & 8 were then used to run 2 independent tests.

    The results were validated by accuracy and confusion matrix.


# Visualize

    We created a dashboard showing the outcome of our machine learning Legendary classification, as well as general Pokemon stats.​
    
    We used Python Pandas, HTML/CSS/Bootstrap, JavaScript D3.js, SQL Database (SQLite), and Tableau.​

       * Python Pandas to clean our data and load clean data into a database​

       * Python Flask app​

    HTML/CSS/Bootstrap to create a web dashboard ​

       * JavaScript D3.js and Tableau to create visualizations​

       * ML results as a table [ML model, Accuracy, R2] ​

            Best model results [Precision, Recall, F1 Score, Support, R2] and confusion matrix​

       * Double bar charts to show the average stats of  stats legendary vs non-legendary pokemon​

       * Bubble chart showing how many legendaries can perform each move​

       * Pie chart displaying legendaries per generation 
    
    SQL Database - store data for Flask app


# Deployment
      ​
    Application hosted on Heroku using gunicorn. 


# Authors 

    Josh Hopkins, Kaylie Sheehan