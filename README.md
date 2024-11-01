## RecommendationMovies

A user-based movie recommendation system using collaborative filtering and cosine similarity. This project uses the MovieLens dataset to provide movie recommendations based on user similarity.

## Overview
This project provides movie recommendations by identifying similar users based on their movie ratings. Using collaborative filtering, it suggests movies that users with similar preferences have enjoyed.

## Features
- Uses collaborative filtering to generate personalized movie recommendations.
- Calculates user similarity using cosine similarity.
- Recommends top N movies for a specific user based on preferences from similar users.

## Project Structure
RecommendationMovies/ │ ├── RecommendatonSystemMovies.py # Main Python script for generating recommendations ├── README.md # Project description and instructions ├── requirements.txt # Python dependencies ├── javaproject/ │ └── u.data # MovieLens dataset (user-item interactions) └── .gitignore # Files to ignore in version control

## Dataset
The dataset used in this project is the **MovieLens `u.data`** file, which contains user-item interaction data. Each row in `u.data` represents a rating given by a user to a specific movie. It includes the following columns:
- **user_id**: Unique identifier for each user.
- **item_id**: Unique identifier for each movie.
- **rating**: Rating score given by a user to a movie (ranging from 1 to 5).
- **timestamp**: Time at which the rating was recorded.

**Note**: The MovieLens dataset is publicly available, and you can download it from [MovieLens](https://grouplens.org/datasets/movielens/). Ensure the `u.data` file is in the `javaproject` folder or adjust the file path in the code.

## Installation

1. **Clone the repository**:
   git clone https://github.com/your-username/RecommendationMovies.git
   cd RecommendationMovies
2. **Install dependencies**: Use requirements.txt to install the required packages:
pip install -r requirements.txt

3. **Download and Place the Dataset**: Place the u.data file from the MovieLens dataset in the javaproject folder. Ensure that the file path in the code is correct.

4. **Run the recommendation script**: To generate recommendations for a user, run the script:
python RecommendatonSystemMovies.py

5. **Customize Recommendations**: Inside the script, you can change the following parameters:
- **userID**: Set this to the user ID for whom you want recommendations.
- **numOfRecommendations**: Set the number of recommendations you wish to generate.

## Credits
Special thanks to MovieLens for providing the dataset and to the creators of pandas and scipy libraries for their excellent tools.
