# Technical Lesson: Advanced Tableau

# Technical Lesson: Advanced Tableau

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: Advanced Tableau

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

**Scenario:** We are working as a junior product analyst for a company that sells bicycles and biking equipment/accessories/gear. We have been tasked with producing a comprehensive and interactive dashboard to analyze and highlight sales metrics across products, countries, and customer demographics in order to form targeted marketing campaigns.

**Key Process Steps:**

* Creating parameter controls
* Major sales metrics
* Creating calculated fields to match the parameter controls
* Incorporating navigation to switch between dashboards

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of advanced Tableau.

[VIDEO LINK](https://player.vimeo.com/video/1038345705?h=17b7e5987c)

### Resources

To follow along and practice during this lesson, you'll need:

* Tableau Public Account
* [Sales Dataset


  Links to an external site.](https://www.kaggle.com/datasets/abhishekrp1517/sales-data-for-economic-data-analysis/data)
* [Flaticon


  Links to an external site.](https://www.flaticon.com/?k=1731082831222&sign-up=google)

### Instructions

#### Step 1: Connect to Data and Create Profit and Profit Margin

After connecting to the resources:

* **Create** Calculated Field - Profit
* **Right click** the Revenue Field. **Select** “Create Calculated Field”.  
  + [Revenue] - [Cost]

![Tableau screen with Revenue Field and Create Calculated Field highlighted.](https://moringa.instructure.com/courses/1426/files/631531/download)

* **Create** Calculated Field - Profit Margin  
  + ([Profit] / [Revenue]) \* 100

![Profit Margin window displaying the provided calculation.](https://moringa.instructure.com/courses/1426/files/631566/download)

#### Step 2: Plan out multi dashboard approach

* **Dashboard 1**: General Overview (regional map, highlevel kpi)
* **Dashboard 2**: Regional/Country trends/differences
* **Dashboard 3**: Customer demographic differences
* Parameter to control and switch b/t KPI:
  + Total Units sold
  + Total Profit
  + Average Profit Margin
* Dynamic KPI Metric based on parameter control
* Allow for cross dashboard filtering (products/categories)
* Home screen with navigation controls
  + Home navigation button on each dashboard

#### Step 3: Dashboard 1

* Create Parameter on first worksheet

![Tableau data menu with Create Parameter option selected.](https://moringa.instructure.com/courses/1426/files/631533/download)

* + **Name:** Metric Selector
  + **Data type:** String
  + **List Values** (add in all three)
    - Total Units Sold
    - Total Profit
    - Average Profit Margin

![Tableau Edit Parameter form.](https://moringa.instructure.com/courses/1426/files/631529/download)

* Create dynamic calculated field
  + Use CASE WHEN THEN logic to match the new dynamic field to your metric selector parameter values
    - Names/conditions must match exactly how you entered them above  
      ![Tableau Dynamic Metric calculation.](https://moringa.instructure.com/courses/1426/files/631414/download)

Now that we have the dynamic metric we can use this to create multiple worksheets visuals to place on our 1st dashboard. The created parameter can be used as a dropdown selector, similar to a filter by right clicking the Metric Selector parameter and choosing “Show Parameter”

* Map for total #s across major regions  
  ![Tableau global map results.](https://moringa.instructure.com/courses/1426/files/631470/download)
* Metric across product/categories (bar chart)
  + Make sure to change the formatting of your y-axis to use the value from Metric Selector  
    ![Edit Axis form for the Dynamic Metric.](https://moringa.instructure.com/courses/1426/files/631317/download)
                
    ![Bar chart of Product Breakdown total units sold.](https://moringa.instructure.com/courses/1426/files/631564/download)

* + Time series line chart for sales trends?  
    ![Graph of monthly sales trends by product categories.](https://moringa.instructure.com/courses/1426/files/631538/download)

**Dashboard 1 Executive Summary Result:**

![Dashboard 1 Executive Summary of Product Breakdown, Sales Trends, and Global Map.](https://moringa.instructure.com/courses/1426/files/631431/download)

#### Step 4: Dashboard 2

**Create visuals for dashboard 2**

* Filter for country
* Tree map for categories and dynamic metric  
  ![Product categories filtered by country.](https://moringa.instructure.com/courses/1426/files/631520/download)
* Break down by sub region (state)

**Dashboard 2 Regional Summary:** Included product breakdown but as a new horizontal chart (separate worksheet) to avoid connecting to the original for the country filter.

![Dashboard 2 results displaying regional Summary of Product Categories, Sub-Regions, and Breakdown.](https://moringa.instructure.com/courses/1426/files/631562/download)

#### Step 5: Dashboard 3

**Create visuals for dashboard 3**

* Age and Gender breakdowns (counts)
* Product breakdowns (metrics) based on gender bins
* Product breakdown for filtered subcategories
  + Only have filter apply to this one graph so users can drill down to look at specific products across gender and age bins

**Dashboard 3 Customer Summary:**

![Dashboard 3 Customer Summary of Age Breakdown, Profits, and Product Categories.](https://moringa.instructure.com/courses/1426/files/631402/download)

#### Step 6: Create homepage dashboard

Now that we have created multiple dashboards looking at different aspects of the data, we can consider adding in navigation controls to make it easy for users to switch between the different views. Note how for each dashboard, we utilized the “Metric Selector” Parameter to enable dynamic charts and look at all three metrics across the different dashboards.

Let’s start by creating a fourth and final ‘dashboard’ that will act as our homepage. This will allow us to treat the full dashboard as an interactive set of pages for the user to explore, akin to its own website.

* Add navigation containers to Home Page dashboard.  
  + Two for each dashboard
  + Image/Icon or text or both!
* Add empty horizontal containers above and below your navigation.
* Add empty vertical containers to the left and right of your navigation.  
  + These two things will allow for easy formatting and spacing of your navigation.
  + This also could be done solely with floating navigation containers but requires more finicky formatting.  
    ![Home page dashboard displaying the Navigation containers.](https://moringa.instructure.com/courses/1426/files/631403/download)
* For each navigation container you need to assign text or icon to be displayed.
  + You could create two side by side containers if you wanted text and icon (as done here).
  + You could also have the icon navigate and just use text containers for description but no navigation ability.
  + We want the navigation to point towards the three respective dashboards.
  + Double clicking a navigation container will open up edit window:  
    - Navigate to - dropdown menu to select which sheet or dashboard  
      * Option: You can navigate to individual sheets/visualizations.
    - Button Style - whether you want an image/icon or text  
      * We will showcase both side by side.
      * Icons taken from [Flaticon.


        Links to an external site.](https://www.flaticon.com/)

In our end result here both the text and the icons will navigate to their respective individual dashboards. This home page could see lots of additional formatting including adding company images, logos and adding thematic color. We will forgo that here for the sack of simplicity. All we added extra was a title for the homepage.

![Home page completed with icons and titles for each dashboard.](https://moringa.instructure.com/courses/1426/files/631319/download)

#### Step 7: Create navigation containers to go back to homepage

Incorporate into each dashboard for easy movement between.

* We will add a ‘homepage’ icon to allow users a one click option to get back to the landing page.
* We use the same navigation container as before!
* Navigate to Home Page.

#### Step 8: Dashboard actions

Tableau “Actions” can also be used to help add in interactivity, navigation, and filtering. In fact, there should already be several actions already automatically created via the filtering that was included in the visualizations above. Actions can also be created manually to add specific interactions between the user and the dashboard/worksheets.

A simple action to add is to navigate to a sheet by clicking into a specific visual. Let’s add an action that will allow us to click the global map on the executive Summary Dashboard and be brought immediately to the Regional Summary dashboard. In this essence the visual itself is acting as a navigation container.

* On any dashboard, click into the Dashboard menu at the very top of program bar and select actions.
* We want to “Add Action” to create a new manual/custom one. We will select the “Go to Sheet” option.
  + Note the other options available and the different actions that allow for interactivity and customization.  
    ![Add Action menu selecting the Go to Sheet option.](https://moringa.instructure.com/courses/1426/files/631400/download)
* Choose Executive Summary as the source sheet - and only select the Global Map
  + Run action on - Select: This enables you to control when/how the action gets run based on clicking or hovering or providing a menu selection
  + Target Sheets - choose Regional Summary as the target

#### Step 9: Hide Sheets and Publish

* The final step is to publish this dashboard. To clean up the published view, hide the worksheets associated with each dashboard. Right click the Dashboard in the bottom toolbar and select “Hide All Sheets” - this can be done for all dashboards.
* The dashboard(s) can now be published wherever it needs to be (in this case Tableau Public).
* [Finished Dashboard


  Links to an external site.](https://public.tableau.com/shared/CFNGTRNFX?:display_count=n&:origin=viz_share_link)

**ICON Attribution:**

* [Data report icons created by Mehwish


  Links to an external site.](https://www.flaticon.com/free-icons/data-report)
* [Countries icons created by Freepik


  Links to an external site.](https://www.flaticon.com/free-icons/countries)
* [Experience icons created by Freepik


  Links to an external site.](https://www.flaticon.com/free-icons/experience)
* [Home button icons created by Freepik


  Links to an external site.](https://www.flaticon.com/free-icons/home-button)

### Common Challenges

**Performance Issues**

* **Challenge:** Slow dashboard loading with multiple calculations
* **Solution:** Use extracts, optimize calculations, implement efficient filters
* **Impact:** Balances functionality vs speed

**Data Integration**

* **Challenge:** Multiple source complexity
* **Solution:** Proper data modeling, strategic blending vs. joins
* **Impact:** Affects refresh rates and maintenance

**User Adoption**

* **Challenge:** Complex features overwhelming users
* **Solution:** Progressive disclosure, guided analytics, simple filters
* **Impact:** Determines dashboard effectiveness

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248469

Scraped At: 2026-05-15T10:05:15.025263
