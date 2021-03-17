# plotly-challenge

<h3> Belly Button Biodiversity Dashboard </h3>
<br>
<p>The Belly Button Biodiversity Dashboard is an interactive dashboard that explores Belly Button Biodiversity and summarizes results of an analysis of microbes found in bellybutton of participants. Upon selection of participant, the summary results are displayed in three individual charts, and a demographic information panel in accordance with selected participant ID. </b>
<h5>The Dashboard</h5>
<ul>
 <li>The first chart sorts the Top Ten OTU's, as displayed by OTU ID number, found within the selected participants bellybutton in a bar chart. Hovering over each display bar, reveals the bacteria name, and the exaxct sample value of bacteria recorded. </li>
<li>The second chart, is displays a gauge parameter of washing frequency per week of selected participant. </li>
<li>The third chart, enables visulaization of the data in accordance with the bacteria label number on the x-axis, and the bacteria sample value mapped within it's position on the y-axis in accordance with it's marker size also determinate of the sample value. Hovering over each bubble displays the OTU ID number, followed by the bacteria sample value as well as the classification of the specific microbe.</li>
</ul>
<h5>The Data: </h5>
<p>The dataset was researched and logged by North Carolina State University betwwen the years 2011 and 2012. The <a href="http://robdunnlab.com/projects/belly-button-biodiversity/">study</a>, published in 2012, investigated factors of 273 participants and includes demographics for age, ethnicity, gender, location, bellybutton type (innie vs outie), and washing frequency. The taxonomic data matrix representing the participants includes 648 species of bacteria recorded of the individuals sampled within the dataset.</p>
</br>
![alt-text](https://media.giphy.com/media/QyhWbJMRlXH4wK1ZLu/giphy.gif) 



<h4>Full Site published at: </h4>
https://cspence001.github.io/Sites/plotly.io/index.html 

<h6>File Contents: </h6> The static folder contains the js folder that holds the app.js file used to render the dashboard display in the index.html file located in the main repository. The app.js file cites the samples.json in the main repository that contains the dataset in .json format.
<h6>Languages/Components/Libraries: </h6> Javascript, HTML, Bootstrap Components, plotly <br>
![alt-text](https://github.com/cspence001/plotly-challenge/blob/main/image/dashboard.gif) 
