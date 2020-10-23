# Tanzanian Water Well Predictor README.md
![elephant1](https://timbuktutravel.imgix.net/countries/kodak_images/000/000/005/original/Elephants-Serengeti-Safari-timbuktu.jpg?w=1420&h=946&auto=format&crop=fit&fit=min&dpr=1&q=50)

# Table of Contents

### Reports
- [Presentation Notebook](https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/notebooks/report/report.ipynb)
- [Presentation Powerpoint]( https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/reports/Tanzanian_Water_Well_Data_Presentation.pdf )

### Exploratory Notebooks
- [Andrew's EDA]( https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/notebooks/exploratory/ayeh_eda.ipynb )
- [Sindhu's EDA]( https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/notebooks/exploratory/Sindhu_EDA.ipynb )

### Helpful Resources
- [Tanzania Water Well Competition](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/)
- [Tanzania Water Well Project ]( https://www.tanzaniawaterproject.org/ )

# Background
![Tanzania](/reports/figures/Tanzania.jpg)

Tanzania is a developing country in East Africa, and is home to the tallest mountain on the continent.  Due to it's geographical location, many citizens are forced to walk three to miles round trip a day on order to acquire water, which is not even guaranteed to be safe for consumption.  This lack of access to drinkable water, combined with inadequate sanitation and poor hygiene leads to a very serious health crisis in which charity organizations are doing their best to combat.  One such organization is the Tanzania Water Project, which does it's best in an attempt to install numerous waterpoints around the country.  Waterpoints are wells in which locals can use to draw water from, heavily reducing the time spent each day drawing water as well as providing safer, more hygenic water to use.  However, many of the water wells have become either non functional or require repairs.  As it is both time and money costly venture to go to each one in order to check their condition, we needed a way to predict which wells were fine at the time being, and which wells were more likely to require repairs.

# Tanzanian Water Well Challenge

Through a collaboration from Taarifa, a rwandan news platform, and the Tanzanian Ministry of Water, the competition 'Pump it Up: Data Mining the Water Table' has been hosted.  Contestants will be given sample data about current existing wells that we know the condition of.  Data we receive ranges from the group that funded the well, longitude/latitude coordinates, and water well pump type, and participants are expected to utilize this information to create a predictive model that can find the status of a well just by being given preliminary information. The following is a comprehensive map of all the known wells in the country, as well as their state.

![Tanzania_train](/reports/figures/Tanzania_train.jpg)

To judge our model, we are given data on wells in which we do not know the status of.  We will aim to predict the status of these wells with the best performance that we can.  This is a map showing all the locations of wells with an unknown status that we aim to fill in.

![Tanzania_test](/reports/figures/Tanzania_test.jpg)


# Tanzania EDA

To help predict the status of wells that we cannot visibly see, we can first look at trends in past data.  In the following models, we will use the legend below.  Orange colored imagery symbolizes functional wells, blue colored imagery symbolizes non-functional wells, and grey colored imagery symbolizes functional wells that need repair.

<img src = '/reports/figures/legend.png' alt = 'legend' width = '200'>

Right off the start, we look at how the well age can affect the status.  While the number of wells that are 'non functional' and 'functional but needs repair' has remained relatively stable, in comparison the number of wells that are functional has exponentially grown as the years go by.  We can assume that newer or younger wells are more likely to be functional than not.

![wells_per_year](/reports/figures/wells_per_year.png)

Here we look to see if the type of the pump can affect the state.  Most of the pumps here are relatively balanced in their results, though gravity pumps and handpumps having slightly more reliability for being functional.  Something that does stand out however is that wells with an 'unknown' pump are vastly more likely to broken compared to the others.

![pump_types](/reports/figures/pump_types.png)

Now we look at how the quality of the water as well as its source could affect its state.  The rows symbolize the two water source types, while the columns symbolize the quality of the water.  We can see from the middle column that only milky or colored water has significantly different results when looking at the water source.  In terms of water quality on the other hand, it's easy to see that water that is good quality or has fluoride has a much higher chance to have a functioning water pipe, while pipes with salty or unknown water quality have a much higher chance of being non functional.

![source_and_quality](/reports/figures/source_and_quality.png)


# Tanzania Modeling

For our predictive model we are mainly looking at two things: accuracy and recall.  Accuracy is a good general metric for determining model performance, and recall is a metric for determining how good we are at lessening the chance of false negatives.  We want a good recall score for our non-functional pumps since we don't want to mistakenly mark a broken pump as functional.  This is because it could lead to loss of lives in the worst case scenario

<img src = '/reports/figures/legend_models.png' alt = 'legend_models' width = '200'>

We start our journey with a simple first single model that utilizes a base logistic regression model.  We can see that we start out with a very high score of 0.75 for accuracy and but a low 0.56 for recall.

![1_model_FSM](/reports/figures/1_model_FSM.png)

While we started out with a high accuracy, we know that it is inaccurate due to the very low recall value, thus our next step was to undergo proper data preprocessing which included imputing, scaling, and up-sampling.  After all that and with a bit of hyperparameter tuning, we used our logistic regression model again.  As seen on the graph, almost all of our metrics went down, but on the contrary our recall score had a significant jump

![2_model_LR](/reports/figures/2_model_LR.png)

Next we went through decision trees.  Our recall score did not change at all, but our other metrics went up a significant amount

![3_model_DT](/reports/figures/3_model_DT.png)

After that our next model utilized KNN.  While nothing significant happened, this lead to a slightly increase to all metrics performance wise, especially our recall score.

![4_model_KNN](/reports/figures/4_model_KNN.png)

(VE explanation)

![5_model_VE](/reports/figures/5_model_VE.png)

(RF explanation)

![6_model_RF](/reports/figures/6_model_RF.png)

# Tanzania Final Model

(LGB explanation)

![7_model_LGB](/reports/figures/7_model_LGB.png)


# Tanzania Model Prediction Results and Conclusion

Using our model above, we took the input data and predicted the status of all of them.

![Tanzania_final](/reports/figures/Tanzania_final.jpg)


![elephant2](https://pixy.org/src/25/253641.jpg)
