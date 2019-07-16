# **Seaborn Aggregate Visualizations**
The purpose of this repository is to demonstrate my ability to perform aggregate
data visualizations using Python's Seaborn library. All data was ethically
sourced from kaggle.com. The data is from a micro finance company called Kiva.
I decided to use aggregate visualizations to examine the equity of their lending
practices.

## Bar Chart: Mean Investment Amount by Country
* El Salvador and Cambodia receive significantly larger lone sums
* It is important to remember that the data are in units of USD and are not
normalized for individual countries currency value
* Cambodia has a much larger standard deviation in loan amount. That should
be analyzed to see if variance is caused by gender, religion, economic class or
other inappropriate reasons

### Bar Chart: Mean Investment Amount by Country (gender = nested)
* There appears to be significant preferential loan practices for men in Pakistan, Kenya and Cambodia
  * Followup statistical analyses ANOVA should be ran

#### Box Plot: Loan Amount Distributions by country
* I'm not drawing conclusions from these plots because my violin plots are way better

##### Violin Plot: Loan Amounts and Distributions by Business Type
* There is a higher frequency of larger sum loans being given to farming businesses. Is this because of larger ROI? Is there a larger barrier to entry? Or is this a poor lending practice?

###### Violin Plot: Loan Amounts and Distributions by Country (gender = nested)
* There appears to be a trend where women receive a higher frequency of smaller loans where as men receive a higher frequency of larger loans
* Are these trends consistent with ROI?
