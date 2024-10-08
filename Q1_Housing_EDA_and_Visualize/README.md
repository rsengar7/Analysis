## House Price EDA and Analysis

This task involves an exploratory data analysis (EDA) on house prices, focusing on understanding the relationship between various features such as area, number of rooms, air conditioning, and more. The analysis includes visualizations and statistical methods to uncover insights about the factors that impact house prices.

### Data Description

The dataset includes features such as:

- Area (sq ft)
- Number of Bathrooms
- Air Conditioning (Yes/No)
- Total Rooms (Bedrooms + Guestroom)
- Number of Stories
- Basement (Yes/No)
- Furnishing Status (Unfurnished, Semi-furnished, Furnished)
- Parking Spaces
- Guestroom (Yes/No)

### Key Insights

1. Feature Importance: An important part of the analysis was identifying which features most influenced home prices. The plot below shows that area and number of bathrooms are the top two features, with air conditioning and total rooms also playing a role. Based on this, the Graphs are created.

![Feature Importance](https://github.com/rsengar7/Analysis/blob/main/Q1_Housing_EDA_and_Visualize/Screenshots/feature_importance.png)

2. Home Price vs Area: We observed a strong positive correlation between the area of a house and its price. As shown below, homes with larger areas generally have higher prices, although there are a few exceptions.

![Correlation Graph](https://github.com/rsengar7/Analysis/blob/main/Q1_Housing_EDA_and_Visualize/Screenshots/correlation_graph.png)

3. Price Distribution by Number of Bathrooms: The number of bathrooms is another important factor affecting home prices. Homes with more bathrooms tend to have higher prices, as displayed in the box plot below.

![Bathroom Plot](https://github.com/rsengar7/Analysis/blob/main/Q1_Housing_EDA_and_Visualize/Screenshots/bathroom_price_box_plot.png)

4. Home Prices by Number of Stories: Houses with more stories are typically priced higher. The bar chart below demonstrates how prices rise with the number of stories. 

![Price vs Stories](https://github.com/rsengar7/Analysis/blob/main/Q1_Housing_EDA_and_Visualize/Screenshots/stories_price_box.png)

5. Air Conditioning and Price Distribution: Homes with air conditioning generally show a broader price range. The violin plot below illustrates that homes with air conditioning tend to have slightly higher prices than those without.

![Air Condition vs Price](https://github.com/rsengar7/Analysis/blob/main/Q1_Housing_EDA_and_Visualize/Screenshots/violin_plot_aircondition.png)

### Future Work
- Implement predictive modeling (e.g., Linear Regression, Decision Trees) to predict house prices.
- Explore other factors such as neighborhood, proximity to amenities, etc.
