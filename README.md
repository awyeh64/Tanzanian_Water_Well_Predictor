# Tanzanian Water Well Predictor


# Table of Contents

### Reports
- [Presentation Notebook](https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/notebooks/report/report.ipynb)
- [Presentation Powerpoint]( https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/reports/Tanzanian_Water_Well_Data_Presentation.pdf )

### Exploratory Notebooks
- [Andrew's EDA]( https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/notebooks/exploratory/ayeh_eda.ipynb )
- [Sindhu's EDA]( https://github.com/awyeh64/Tanzanian_Water_Well_Predictor/blob/main/notebooks/exploratory/Sindhu_EDA.ipynb )

### Helpful Resources
- [Tanzania Water Well Project ]( https://www.tanzaniawaterproject.org/ )

![Tanzania](/

# Background
![Tanzania](/reports/figures/Tanzania.jpg)
Tanzania is a developing country in East Africa, and is home to the tallest mountain on the continent.  Due to it's geographical location, many citizens are forced to walk three to miles round trip a day on order to acquire water, which is not even guaranteed to be safe for consumption.  This lack of access to drinkable water, combined with inadequate sanitation and poor hygiene leads to a very serious health crisis in which charity organizations are doing their best to combat.  One such organization is the Tanzania Water Project, which does it's best in 

# Tanzanian Water Well Challenge


Through a collaboration from Taarifa, a rwandan news platform, and the Tanzanian Ministry of Water, the competition 'Pump it Up: Data Mining the Water Table' has been hosted.
![Tanzania_train](/reports/figures/Tanzania_train.jpg)

![Tanzania_test](/reports/figures/Tanzania_test.jpg)


# Tanzania EDA


To help predict the status of wells that we cannot visibly see, we can first look at trends in past data.  In the following models, we will use the legend below.  Orange colored imagery symbolizes functional wells, blue colored imagery symbolizes non-functional wells, and grey colored imagery symbolizes functional wells that need repair.

<img src = '/reports/figures/legend.png' alt = 'legend' width = '200'>

![wells_per_year](/reports/figures/wells_per_year.png)

Right off the start, we look at how the well age can affect the status.  While the number of wells that are 'non functional' and 'functional but needs repair' has remained relatively stable, in comparison the number of wells that are functional has exponentially grown as the years go by.  We can assume that newer or younger wells are more likely to be functional than not.

![pump_types](/reports/figures/pump_types.png)

Here we look to see if the type of the pump can affect the state.  Most of the pumps here are relatively balanced in their results, though gravity pumps and handpumps having slightly more reliability for being functional.  Something that does stand out however is that wells with an 'unknown' pump are vastly more likely to broken compared to the others.

![source_and_quality](/reports/figures/source_and_quality.png)

Now we look at how the quality of the water as well as its source could affect its state.  The rows symbolize the two water source types, while the columns symbolize the quality of the water.  We can see from the middle column that only milky or colored water has significantly different results when looking at the water source.  In terms of water quality on the other hand, it's easy to see that water that is good quality or has fluoride has a much higher chance to have a functioning water pipe, while pipes with salty or unknown water quality have a much higher chance of being non functional.

# Tanzania Modeling
<img src = '/reports/figures/legend_models.png' alt = 'legend_models' width = '200'>

![1_model_FSM](/reports/figures/1_model_FSM.png)
![2_model_LR](/reports/figures/2_model_LR.png)
![3_model_DT](/reports/figures/3_model_DT.png)
![4_model_KNN](/reports/figures/4_model_KNN.png)
![5_model_VE](/reports/figures/5_model_VE.png)
![6_model_RF](/reports/figures/6_model_RF.png)
![7_model_LGB](/reports/figures/7_model_LGB.png)

# Tanzania Model Prediction Results
![Tanzania_final](/reports/figures/Tanzania_final.jpg)

# Conclusion
