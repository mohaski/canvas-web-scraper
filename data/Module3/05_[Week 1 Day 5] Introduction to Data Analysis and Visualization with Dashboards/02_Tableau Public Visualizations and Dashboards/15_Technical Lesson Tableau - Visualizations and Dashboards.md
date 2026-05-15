# Technical Lesson: Tableau - Visualizations and Dashboards

# Technical Lesson: Tableau - Visualizations and Dashboards

## ![Blue FS Logo](https://moringa.instructure.com/courses/1426/files/631314/preview) Technical Lesson: Tableau - Visualizations and Dashboards

Icon Progress Bar (browser only)

*​*

**Estimated Completion Time:** 1 hour

Now that you have gotten a taste of some of the features Tableau has to offer, it is time look at some additional features. We are going to use our knowledge of Tableau's interface and its functionality to create a workbook that can help us to build out a cohesive dashboard and tell a story with our data

In this lesson, we will provide a guide on how to build dashboards in Tableau in ten simple steps. The guide begins by emphasizing the importance of planning a dashboard and clarifying the objectives to visualize data effectively. The steps include creating a new dashboard, choosing the appropriate layout, adding sheets, arranging and resizing them, adding filters, titles and text, customizing the appearance, and publishing the dashboard.

We will be using a sample dataset provided by Tableau for ease of use and demonstration. Tableau has several curated datasets under the Resources section when you first open it up, which can be great places to start exploring how to visualize data in Tableau.

This lesson will cover:

* Creating individual visualizations in Tableau.
* Creating a dashboard in a Tableau workbook.
* Using horizontal and vertical containers to implement a dashboard layout.
* Applying customizations and add filters to a dashboard.
* Saving and publishing a dashboard to Tableau Public.

### Video: Technical Lesson Walkthrough

The video below will guide you through each step of the lesson. You can follow along with this video to walk through each step, refer to the written instructions provided below the video, or use both resources for a comprehensive understanding of Tableau Public - visualizations and dashboards.

[VIDEO LINK](https://player.vimeo.com/video/1038345954?h=e0c0bf791f)

### Instructions

#### Step 1. Download and Connect to Data Source

##### Access Sample Data Sets

On the right side of the landing page is the Learn Tableau section. Underneath that is an Explore sample data sets link that we want to click into.

The Superstore Sales data set is one that we will be working with. When we click on the link, a dialogue box will open to choose the location to save the file. For ease of access, we'll choose the Datasources folder in the My Tableau Repository directory. \*\*Documents/My Tableau Repository/Datasources was automatically created when you installed Tableau.

![Tableau screen of Sample Data resources with the Superstore Sales dataset selected.](https://moringa.instructure.com/courses/1426/files/631407/download)

##### Connect to Data within Tableau

Next, we will navigate to the Connect pane (2) in the upper left-hand corner of the screen, directly below the Tableau icon (1) and select To a File > Microsoft Excel(3).

![Connect pane in Tableau highlighting the Tableau icon, Connect menu, and Microsoft Excel file option.](https://moringa.instructure.com/courses/1426/files/631422/download)

Then, we'll use the Open dialogue box to retrieve and open the previously downloaded data file Sample - Superstore.

![Tableau Connect pane displaying the Open file menu with SAmple - Superstore.xls selected..](https://moringa.instructure.com/courses/1426/files/631463/download)

##### Launch the Data Source Page

After completing the steps above, Tableau will launch the Data Source page.

From the Data Source page, we need to drag the Orders sheet to the canvas. You'll notice that two more panes appear in the lower portion of the screen. This is the Data Grid on the right, which displays a preview of the first 1,000 rows of the data contained in the data source that we selected, and the Metadata grid on the left displays the fields in our data source as rows.

![Tableau Data Source page with the Orders Sheet on the canvas.](https://moringa.instructure.com/courses/1426/files/631484/download)

Next, we drag the Return sheet to the canvas as well. Since the tables have an existing link and shared field (OrderID), a line appears to form an automatic relationship between the tables.

![Tableau screen displaying the connected relationship between the Orders and Returns tables.](https://moringa.instructure.com/courses/1426/files/631426/download)

If no automatic relationship was detected by Tableau, the Edit Relationship dialog would open. Then, we can indicate which field should be used to relate the two tables.

For our purposes, we will use two tables, but in the future, you can use as many tables as needed.

**Note:** This data file is updated periodically by Tableau; newer versions might display different names/numbers than shown below.

#### Step 2. Visualizing Profits

Suppose we want to create a visualization that will communicate which kinds of products yield the most profits. A bar chart is a great choice for conveying this kind of information.

We select Sheet 1 from the Sheets tab to launch the Tableau Workspace.

##### Create a Bar Chart

1. Lets rename the new worksheet "Profits by Sub-Category".  
   1. We right click Sheet 1 on the bottom tab → select Rename option.
   2. In the Menu bar we navigate to the Fit dropdown, should default to Standard, and select the Entire View option.
2. Drag the Orders.Sub-Category pill, a Dimension, into the data pane to the Columns shelf. Then drag the Orders.Profit pill, a Measure, into the Rows shelf.  
   1. Notice that Tableau automatically switches to SUM(PROFIT) appropriately.
   2. This can be changed by accessing the dropdown menu of the pill itself within the Row shelf and selecting the Measure option.
   3. We want to leave it at sum for this instance.
3. This looks great, but it is a little difficult to read the sub-categories at the bottom of the chart. One simple fix for this instance would be to swap the axes so the sub-categories become the rows and the profit becomes the columns.  
   1. We can use the swap-axis button in the Menu bar to see how it affects the visualization.
4. Now that we have a good-looking bar chart, we can make it a little more informative. For instance, we would likely want the profit sorted so that it is easier to quickly find the highest or lowest profit-earning sub-categories. Fortunately, Tableau has a tool for this!  
   1. We can use the Sort Descending button in the Menu bar and apply it to the bar chart. And, just like that, we have a graph that helps us to find the information we are looking for.

![Tableau Workspace displaying a bar chart of the profits by sub-category.](https://moringa.instructure.com/courses/1426/files/631512/download)

##### Customizing and Styling

With so many sub-categories, it may be a bit difficult to connect the sub-category with the corresponding value. Let's make a few tweaks to improve the visibility of our visualization.

1. ![Tableau Edit Colors options for selected data.](https://moringa.instructure.com/courses/1426/files/631468/download)
   We can drag the Orders.Profit pill from the Data pane to the Color option within the Marks card. This will automatically change the color of the plot based on values from the profit pill.  
   1. We can customize by clicking on the Color card on the marks card and selecting Edit Colors…
   2. This will open up a window in which you can select specific color maps/ranges. Tableau has a great set of options via the Palette dropdown but you can also select your own colors too. You can even enter hex codes for color to help with specific brand matching!
   3. Let's choose the Orange-Blue Diverging Palette option, a good option to use for heat mapping numerical values.
2. We can also drag the other Orders.Profit pill from the Data pane to the Label card option within the Marks card. This will automatically apply a label at the end of each bar on the chart to indicate the sum of profit for that sub-category.
   1. We can do even more formatting for these labels as well by right clicking one of the SUM(PROFIT) pills and selecting Format.
   2. The Format pane will appear to the far left of the screen.
   3. Within the Default section, we can customize how the value is displayed by selecting the Number drop-down and choosing Currency (Custom), and setting the decimal places to zero.
   4. We now have our values being displayed in true monetary format, complete with dollar signs. There is lots of customization and formatting that can be done in a similar manner including changing background colors on the chart, title and axis.

##### Adding a Title

Having a visualization is great, but we want to make it look professional and make it convey the information that is being shared by the visualizations. To do this, we will give the worksheet a meaningful title.

1. The default name of the worksheet is the default name of the tab we are working in, but we can customize this.  
   1. If we right-click or double-click on the title of the visualization, which at the moment should be Profits by Sub-Category, we will be able to format and change it.
2. In the dialogue box that appears, you can see that the name of the worksheet is forced as the <Sheet Name>, hence the default naming.  
   1. We could change the name by simply replacing the default <Sheet Name> with any meaningful name. For now let's leave it as, we changed the sheet name to be verbose.
   2. We can go ahead and change the color to blue by highlighting the text and selecting the color dropdown.
   3. We can also center the title above our visual using the standard format options for centering text.
   4. Click Apply and OK to save the changes.

![Results of the Profits by Su-Category bar chart customizations.](https://moringa.instructure.com/courses/1426/files/631449/download)

#### Step 3. Visualizing Orders by Region

Next, let's create a chart that visualizes the number of orders by region so we can get a good idea of where to focus our next marketing campaigns.

##### Create a Regional Map

1. Lets select the New Worksheet Icon from the sheets tab again and rename it "Orders by Region". Let’s also center the title and change the font color to blue to match our first viz.
2. We'll drag the Orders.Orders (Count) pill from the Data pane to the Rows shelf. Then, drag the Orders.Postal Code pill to the Columns shelf. This will look a little messy and should create a bar chart for us.
3. This is where the Show Me Pane can come in really handy.  By selecting the Show Me Pane from the upper right-hand corner and choosing the symbol maps visualization Tableau will automatically rearrange the pills to generate longitude and latitude based on postal code.  
   1. Notice how it automatically created Marks cards for us. One for CNT(Orders) pertaining to size and the other for Postal Code as a Detail (important for Lat, Long).

![Tableau screen of the selected tables displayed as orders by region on a map.](https://moringa.instructure.com/courses/1426/files/631516/download)

##### Customize the Regional Map

1. Just like with the bar chart previously we want to explore some further customization options. We already have size being used to denote the number of orders for each postal code, let’s consider how we could use color as well. Utilizing the Marks cards again, lets drag the Orders.Region pill into the Color card. This will act to separate out our data points by the 4 regions present in or data.
2. We could adjust the colors as we see fit or again use a standard Tableau color palette. Let’s select Color Blind and then Assign the Palette. Notice you can also change individual colors via selecting them on the left and then selecting the specific color.
3. Navigate to the Fit drop-down on the Command bar at the top of the screen. Select "Entire View".

![Orders by Region map with regional color customizations.](https://moringa.instructure.com/courses/1426/files/631438/download)

#### Step 4. Visualize Sales Over Time

Finally for our last visualization, we want to visualize monthly sales on a time series plot, which is a version of a line graph, to try and showcase any sales trends or patterns.

##### Create a Line Chart

1. We'll select the New Worksheet Icon from the sheets tab and rename it “Sales by Month”. Let’s also go ahead and mirror the title formatting from our previous vizzes, blue and centered.
2. Before we start in let’s also navigate to the Fit drop-down on the Menu bar and select "Entire View".
3. We want to drag the Orders.Order Date pill from the Data pane to the Columns shelf. Notice that the pill is transformed and now reads YEAR(OrderDate).
4. Next we will drag the Sales pill to the Rows shelf. Notice again that it becomes SUM(Sales).

![Line Chart visualization of Sales by Month.](https://moringa.instructure.com/courses/1426/files/631486/download)

##### Customize the Line Chart

While the above chart gives us a decent look across years it really isn’t granular enough to tease out any subtle differences in sales. We can dive a little deeper into it by breaking out years into months instead and using some Color to represent a third variable.

1. Navigate to the Columns shelf and select the down-arrow on the YEAR (OrderDate) pill and select "Month" instead of “Year”.
2. We then want to drag the Orders.Category pill to the Colors card within the Marks card. You should notice a legend that provides the product category for each color.
3. While the color helps it can still be a little difficult to read. We could go one step further and actually change the line path, or style. By selecting the Path Marks card without dragging anything into it will let you select a few options for line style, let’s change it to medium dashed so we can distinguish between lines a little better.

![Sales by Month Line Chart results with customizations.](https://moringa.instructure.com/courses/1426/files/631544/download)

#### Step 5. Building a Simple Dashboard

Now that we have created several visualizations helping us explore and display profit and sale metrics we can think about combining all three into a single dashboard for ease of access. Recall our process for Dashboarding:

1. Plan (done)
2. Create vizzes (done)
3. Create Dashboard
4. Layout
5. Add sheets to dashboard (vizzes)
6. Arrange and resize as needed
7. Add interactivity/filters if desired
8. Add any extra tiles, text, images, etc…
9. Customize and style with color, font etc…
10. Publish and share

##### 1. Dashboard Planning

To complete step one, we have to understand our use case and plan our dashboard.

For this lesson, our use case is to create a dashboard that will communicate Profit and Sales metrics across several dimensions:

* Profits by Sub-Category
* Orders counts across Regions
* Sales across months for the major product categories

To communicate these data visualization needs we have created a bar chart, a regional map, and a multi-line time series chart.

##### 3 and 4. Dashboard Creation and Layout

Now that we have our three vizzes, we can build a dashboard by selecting the New Dashboard icon from the Sheets tab.

1. Let’s give it a meaningful title “Profit and Sales Metrics”  
   1. In the Size dropdown, we select Fixed Size → Generic Desktop  
      1. We won’t get into different sizing here at all but this should be considered depending on your audience, is it going into a powerpoint or will it be embedded on a website etc…
      2. You might need to make your Tableau Window larger to see the full dashboard canvas.
   2. We select Custom Layout, Tiled, and Show Dashboard Title.
   3. Right-click the dashboard title and select Edit Title. We need to make sure that the title is centered, the font size is 18, and the color is blue.
2. Let’s next drag a Vertical Container from the Objects card and add it beneath the title.   
   1. We'll drag in a 2nd Vertical Container and place it next to the first.
   2. Let’s also do the same for a Horizontal Container from the Objects card and drop it underneath the two Vertical Containers.
   3. We will populate these containers in the next section.
   4. It can be a little frustrating at times to line up the tiled containers right. It will highlight in Grey where that container will fit, when dragging in a new container to help.

##### 5 and 6. Adding Sheets and Rearranging

Now that we have a container in place for each of our three vizzes we can begin to actually populate them into the dashboard.

1. Let’s consider information importance and the F-Pattern. A lot of this is subjective to the goal and audience of the dashboard, which viz do you think is the most important?  
   1. Let’s consider Profits by Sub-Category as the most important as it can allow business to focus on the money making products. This will go in our top left container. We can drag and drop it into place from the Sheet pane on the left.
   2. Next we might consider Sales by Month as the next important given it’s slight connection to sub-category and should be placed in the top right container.
   3. Finally our third visualization Sales by Month will be placed in the bottom container. This also allocates the most elongated space on our dashboard to the time series chart so it won't get squished.
   4. NOTE: The title box can get wonky when placing containers, reselecting the “Show Dashboard Title” button in the Objects card will make it span the full top of the dashboard again.
2. Notice that the legends, for colors and size in our case, automatically get populated over into their own containers when you drag the appropriate sheet into its container. This is on purpose so you can place them individually as necessary, but can get messy initially.  
   1. Let’s place/move our legends for the Sales by Month and Orders by Region so that they are on top of each other to the far right of our dashboard.
   2. Drag both the Region legend and the Count size legend containers to the far right to create a new section to contain them both.
   3. Let’s do something similar for Sales by Month color legend but place it half way down, aligned with the top of our line chart.  
      1. We could also drag it in as a Floating container for even more flexibility and control.
      2. This would allow us to overlay the legend onto the time series given the amount of whitespace.
      3. You might need to adjust the size/length of the container for the other two legends to accommodate placement.
   4. The Profits by Sub-Category doesn’t really need the color scale label given that we labeled/provided the actual values on the figure itself so lets go ahead and save space by deleting it.

Once placed the size and location of containers and their associated visual can be further manipulated and rearranged to adapt the initial layout design if needed or desired. For instance, let’s say that after looking at the ‘finished’ dashboard from above, pictured here, we decided to place even more emphasis on the first chart Profit by Sub-Category, by making it encompass the entire left side of our dashboard. This is easily accomplished via our use of containers, we can just add in a new vertical container and replace the existing one.

![First try of arranging the sheets.](https://moringa.instructure.com/courses/1426/files/631416/download)

Take One

![Second attempt at arranging the sheets.](https://moringa.instructure.com/courses/1426/files/631542/download)

Take Two

IMPORTANT NOTE: Dashboarding is truly an iterative process especially concerning the design, layout, and choice of visuals to include. There is no "one size fits all” solution, it behooves you to change, adapt and improve your dashboards as you create them. Don’t feel stuck into a certain layout just because you initially thought it would be best.

##### 7. Filters and Other Objects

The main goal of creating a dashboard is of course to visualize and convey pertinent information for stakeholders in a convenient and easy to interpret manner. The primary focus should be on the actual visualizations that are included in the final dashboard.

That being said, it is also important to include design elements into your dashboard to add flair and make it more engaging and visually appealing. This includes incorporating user interactivity through use of filter selections that allow a specific user to hone in on a particular aspect of the data they are interested in.

1. Let’s consider how we might be able to filter our dashboard for a bit more interactivity and granularity.
2. We have several good options we could consider, including filtering by region or sub-category. Let’s implement both.
3. There are several ways to implement filters within Tableau ranging from simple chart filters to an actual filter selection menu for the user, all the way to advance dashboard and worksheet actions.  
   1. Today we are going to take a look at the first two methods. If you want to dive in deeper and learn more about advance interactivity here is a good place to start: [Tableau Actions


      Links to an external site.](https://help.tableau.com/current/pro/desktop/en-us/actions.htm)
   2. Probably the most straightforward way to add interactive filtering is by allowing the user to select elements on a visual and have it filter the rest of the dashboard.  
      1. When a container is selected that contains a viz we can see a toolbar in the top right corner of the container.
      2. The third icon, the funnel shape, is the Use as Filter option. By selecting this for all three vizzes we have we can accomplish the first way to filter. If I, as a user, click on one of the sub-category bars, it should filter the rest of the charts as well.

###### Only Copiers

![Profit and Sales Metrics display for copiers only.](https://moringa.instructure.com/courses/1426/files/631445/download)

###### Only One Postal Code

![Profit and Sales Metrics display for one postal code only.](https://moringa.instructure.com/courses/1426/files/631535/download)

###### Only November & Technology

![Profit and Sales Metrics display for November and technology only.](https://moringa.instructure.com/courses/1426/files/631488/download)

###### Only the Central Region

![Profit and Sales Metrics display for the central region only.](https://moringa.instructure.com/courses/1426/files/631540/download)

###### Only Accessories in Central Region from June

![Profit and Sales Metrics display for accessories from the central region in June only.](https://moringa.instructure.com/courses/1426/files/631492/download)

##### 8. Images and Text

To wrap things up let’s consider adding in just a little bit of graphic flair to our dashboard. You can add in text boxes for explanation, maybe explaining the filtering actions a user can take or really highlighting a particular point. You can also add in images and other graphics. Let’s keep it simple and add in a “logo” and some dollar signs for our fictitious company here.

1. The object card contains its own container for images and text as well as other elements to explore on your own.
2. We can drag in two image containers on either side of our title. The image container will prompt for an image upload or web url to display as well as centering and fit to container options.

![Final dashboard with images, titles, and chosen arrangement.](https://moringa.instructure.com/courses/1426/files/631466/download)

##### 9 and 10. Customize and Share/Save/Publish

We have only really introduced the tip of the iceberg here for what is possible in Tableau in terms of customizing style, colors, format, and layout. I would encourage you to step through some of the Tableau examples and training materials as well as the Viz of the Day regularly to get a good look at some of the advanced possibilities within Tableau. Pretty much every element of the dashboard from the container background color to advance interactivity is customizable in some capacity.

The final, and very important, step is to save our dashboard and connected worksheets so that it can be shared with the appropriate users/audience. On the newest version of Tableau Public you can both save locally as well as save or publish to your Tableau Public cloud account.

* This second option provides a great way for beginner users to share their dashboards not only with the large Tableau community but also with others, outside of any internal organization system or hosting.
* Clicking the Save icon within Tableau will default to Tableau Public, you can save locally by accessing the File menu dropdown and selecting Save As.
* When saving to Tableau Public it will prompt you for your account login and then open up the workbook (dashboard and sheets) in Tableau Public. From there you can create embedding or a share link for others. [Here is an example lesson to review.


  Links to an external site.](https://public.tableau.com/views/sample_17219484031700/ProfitandSalesMetrics?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

### Summary

In this lesson, we reviewed the essential steps for building a dashboard and walked through an example using data from Tableau. The steps include planning the dashboard, choosing a layout, adding sheets, arranging and resizing sheets, adding filters, adding titles and text, and customizing the appearance. Then, we walked through creating a simple dashboard for communicating Profit and Sales in three different ways.

We highlighted some crucial design formatting and filtering techniques that can allow you to incorporate user interactivity into your dashboard to improve user experience and broaden its potential use cases.

By now, you should have a fairly good understanding of dashboarding basics in Tableau. In the practice, you will have a chance to apply your skills and create an interactive dashboard on your own.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248381

Scraped At: 2026-05-15T10:00:25.800836
